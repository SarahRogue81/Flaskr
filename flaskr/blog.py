import os
import markdown

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
@bp.route('/page/<int:page>')
def index(page=1):
    db = get_db()

    # Get total count of posts
    total_posts = db.execute('SELECT COUNT(*) FROM post').fetchone()[0]

    if total_posts == 0:
        return render_template('blog/index.html', post=None, md=markdown, app=current_app,
                               current_page=1, total_pages=0, has_prev=False, has_next=False)

    # Calculate offset for pagination (page numbers start at 1)
    offset = (page - 1)

    # Get single post for current page
    post = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
        ' LIMIT 1 OFFSET ?',
        (offset,)
    ).fetchone()

    # If no post found for this page, redirect to last valid page
    if post is None:
        if page > total_posts:
            return redirect(url_for('blog.index', page=total_posts))
        else:
            return redirect(url_for('blog.index'))

    # Calculate pagination info
    has_prev = page > 1
    has_next = page < total_posts

    return render_template('blog/index.html', post=post, md=markdown, app=current_app,
                           current_page=page, total_pages=total_posts,
                           has_prev=has_prev, has_next=has_next)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if not body:
            error = 'Body is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html', app=current_app)


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post, app=current_app)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))


@bp.route('/<int:id>/permalink', methods=('GET',))
def permalink(id):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    page = request.args.get('from_page', 1)

    home_url = f'/page/{page}'

    return render_template('blog/permalink.html', home_url=home_url, post=post, md=markdown, app=current_app)
