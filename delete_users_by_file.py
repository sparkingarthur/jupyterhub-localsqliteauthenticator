#coding=utf-8
import sqlite3
import os
from optparse import OptionParser
from sqliteauthenticator import SQLiteAuthenticator
import traceback

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE")
(options, args) = parser.parse_args()

filename = options.filename
if filename == "" or filename == None:
    filename = "users.txt"


authenticator = SQLiteAuthenticator()
authenticator.login_as_admin()

with open(filename,"r") as f:
    try:
        for user in f.readlines():
            username = user.strip()
            print("delete user: %s"%(username))
            authenticator.sqlite_delete_user(username=username)  # password
            # os.system('rm -rf /home/%s' % (username))
            # os.system('rm -rf /var/spool/mail/%s' % (username))
            # os.system('userdel %s ' % (username))
    except:
        traceback.print_exc()