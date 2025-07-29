import os
import sqlite3
from argparse import ArgumentParser

# setup parser
parser = ArgumentParser(prog = 'userdel',
                        description = f'delete existing user in the database',
                        epilog='this is final')

parser.add_argument('username', help='user to be deleted')
parser.add_argument('-f', '--force', help='definitely delete this user ', action='store_true')

# get arguments
args = parser.parse_args()
username = args.username
forced = True if args.force else False

if not forced:
    answer = input('Are you sure you want to delete this user? (y/n) ').lower()

    if answer not in ('y', 'yes'):
        quit(1)

# delete user
DATABASE = os.path.join('instance', 'flaskr.sqlite')
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute('DELETE FROM user WHERE username = ?', (username,))

connection.commit()
connection.close()

# display information deleted from database
print(f'Deleted {username}')

