# Flaskr

Inspired by [Flask's](https://pypi.org/project/Flask/) amazing [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/).

## Changes

1. Used [W3.CSS](https://www.w3schools.com/w3css/default.asp) for basic UI and ability to change colour themes
2. Used layout UI from [What's the Scoop™](https://github.com/Woz-U-Group-Projects/team-glampfire-trail-mix)
3. [Markdown](https://pypi.org/project/Markdown/) - type [Markdown](https://daringfireball.net/projects/markdown/) text into the `textarea` and the blog post displays as HTML
4. Added [_The MIT License_](https://opensource.org/license/mit) to the main project so that it's the same license as Flask
5. Added more config variables (with sane defaults) to the [`flasker/__init__.py`](https://github.com/SarahRogue81/Flaskr/blob/main/flaskr/__init__.py) file
6. Changed font to Raleway for a more professional look
7. Added footer displaying copyright, [Creative Commons](https://creativecommons.org/) license line, and Powered By line pointing to the inspiration for the blog layout

## Dynamic Blog

To make the Flaskr blog server dynamic, the following variables are set, by default and can be overridden in the `instance/config.py` file:

- __BLOG_LICENSE__ &ndash; the name of the [Creative Commons](https://creativecommons.org/) license for your blog
    - __default__: _Creative Commons Attribution-NoDerivatives 4.0 International License_
- __BLOG_LICENSE_URL__: &ndash; the URL to the License Deed
    - __default__: [https://creativecommons.org/licenses/by-nc-nd/4.0/](https://creativecommons.org/licenses/by-nc-nd/4.0)
- __BLOG_OWNER__ &ndash; you or the owner of the blog
    - __default__: Pallets
- __BLOG_TITLE__ &ndash; the title of your blog
    - __default__: Flaskr
- __SECRET_KEY__ &ndash; The Flask secret key which should be changed for production, see the [Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/deploy/#configure-the-secret-key) for further instructions
    - __default__: dev
- __W3_CSS_COLOUR_THEME__ &ndash; the [W3.CSS Colour Template](https://www.w3schools.com/w3css/w3css_color_themes.asp) that you want to use
    - __default__: https://www.w3schools.com/lib/w3-theme-w3schools.css

## Installation

Fortunately, installation is very simple.

Git the code from GitHub:

        git clone git@github.com:SarahRogue81/Flaskr.git Flaskr

Setup Python environment:

        cd Flaskr

        python -m venv .venv

        source .venv/bin/activate

Initialize database:

        flask init-db

Configure the blog:

        vi instance/config.py

Run the blog on a dev server:

        flask run

For information on running on a production server, please consult the [_Deploy to Production_](https://flask.palletsprojects.com/en/stable/tutorial/deploy/) section of the [Flaskr Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/).

## Online Dev and Hosting environments

There are many to choose from but Flaskr has been setup to be developed and deployed to [Replit](https://replit.com/) as well as [PythonAnywhere](https://pythonanywhere.com).

There's nothing that needs be changed to get this to work on either. The `uv.log` is for Replit and the `flask_app.py` is for PythonAnywhere. Again, this is all setup for you.

Also, GitHub Codespaces is pretty sweet to develop on as well. It's like an online VS Code editor. And with their CI/CD cycle, you can't go wrong for any project.

## Offline Development

You can't go wrong with `vi`. It's the only editor that's 100% guaranteed to be there when you SSH into a server, unlike `atom`. Yes, there's a steep learning curve but at least learn enough for basic editing.

My personal favorite is [Zed](https://zed.dev/). It's super light weight and works on any platform.

And, of course, [VS Code](https://code.visualstudio.com/) works as well. It's big plus is the use of Copilot, which is also on GitHub.

There are others but those are the two I use most.
