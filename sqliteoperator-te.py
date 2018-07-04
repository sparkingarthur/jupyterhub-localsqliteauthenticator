#coding=utf-8
import sqlite3
import os
from optparse import OptionParser
from sqliteauthenticator import SQLiteAuthenticator
import traceback
def _test():
    authenticator = SQLiteAuthenticator()
    authenticator.login_as_admin()
    # authenticator.sqlite_add_user(username='test_1', password='789456123')  # passed
    # authenticator.sqlite_update_password('test_1') # passed
    # authenticator.sqlite_add_user(username='lishijie009', password='123456')
    # authenticator.sqlite_delete_user(username='test_1')   # passed
    # authenticator.sqlite_update_password_admin('test_1') #passed
    # authenticator.sqlite_add_user('test_2',password='789456123') #passed
    # authenticator.sqlite_update_password_admin('test_2') #passed
    pass

_test()





