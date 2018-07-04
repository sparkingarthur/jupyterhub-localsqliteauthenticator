# coding=utf-8
from jupyterhub.auth import Authenticator
from tornado import gen

import os
import sys
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

import sqlite3


class prpcrypt():
    def __init__(self, key='jupyterhubkeykey'):
        self.key = key
        self.mode = AES.MODE_CBC
        self.length = 16
    #used to turn a explicit code to an encoded code
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        count = len(text)
        # padding to length
        add = self.length - (count % self.length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # turn to hex string
        return b2a_hex(self.ciphertext)


class SQLiteAuthenticator(Authenticator):
    def __init__(self):
        super(SQLiteAuthenticator,self).__init__()
        self.admin_mode = False
    def _verify_password(self, username, password):
        #connect to the sqlite-db
        encryptor = prpcrypt()
        sql_cnn = sqlite3.connect(os.getenv('JUPYTERHUB_SQLITEDB_PATH'))
        #print("connect sqlite-db sucessfully")
        cursor = sql_cnn.cursor()
        sql = ("SELECT `password` FROM `users` WHERE `username` = '{}'").format(username)  # select from the database
        # print(sql)
        cursor.execute(sql)
        user_password = cursor.fetchone()[0]  # first to check the username
        #print(user_password)
        input_password = encryptor.encrypt(password).decode()
        #print(input_password)
        #print(user_password == input_password)
        if user_password == input_password:
            cursor.close()
            sql_cnn.close()
            return True
        else:
            print("wrong database/username/password, "
                  "please check your JUPYTERHUB_SQLITEDB_PATH/username/password....")
            cursor.close()
            sql_cnn.close()
            return False

    @gen.coroutine
    def authenticate(self, handler, data):
        username = data['username']
        passwd = data['password']
        # print(passwd)
        if self._verify_password(username, passwd):
            return data['username']
        else:
            return None

    def login_as_admin(self):
        admin_password = input("input password of user 'admin':")
        if self._verify_password('admin', admin_password):
            self.admin_mode = True
            return True
        else:
            self.admin_mode = False
            print("wrong admin password!")
            return False

    def sqlite_add_user(self,username,password):
        if self.admin_mode == True or self.login_as_admin():
            encryptor = prpcrypt()
            sql_cnn = sqlite3.connect(os.getenv('JUPYTERHUB_SQLITEDB_PATH'))
            c = sql_cnn.cursor()
            input_password = encryptor.encrypt(password).decode()
            query = "INSERT INTO `users` VALUES ('{}','{}') ".format(username,input_password)
            c.execute(query)
            sql_cnn.commit()
            c.close()
            sql_cnn.close()
            userpath = ('/home/{}').format(username)
            if not os.path.exists(userpath):
                os.makedirs(userpath)
        else:
            print("only admin has the privilege")

    def sqlite_delete_user(self,username):
        if self.admin_mode == True or self.login_as_admin():
            sql_cnn = sqlite3.connect(os.getenv('JUPYTERHUB_SQLITEDB_PATH'))
            c = sql_cnn.cursor()
            query = "DELETE FROM `users` WHERE `username`='{}' ".format(username)
            c.execute(query)
            sql_cnn.commit()
            c.close()
            sql_cnn.close()
        else:
            print("only admin has the privilege")

    def sqlite_update_password(self,username):
        origin_password = input("input origin password of '{}':".format(username))
        if self._verify_password(username,origin_password):
            encryptor = prpcrypt()
            new_password = input("input new password:")
            input_password = encryptor.encrypt(new_password).decode()
            sql_cnn = sqlite3.connect(os.getenv('JUPYTERHUB_SQLITEDB_PATH'))
            c = sql_cnn.cursor()
            query = "UPDATE `users` SET `password`= '{}'WHERE `username`='{}' ".format(input_password,username)
            c.execute(query)
            sql_cnn.commit()
            c.close()
            sql_cnn.close()
        else:
            print("origin password is wrong!")

    def sqlite_update_password_admin(self,username):
        if self.admin_mode == True or self.login_as_admin():
            encryptor = prpcrypt()
            new_password = input("input new password of {}:".format(username))
            input_password = encryptor.encrypt(new_password).decode()
            sql_cnn = sqlite3.connect(os.getenv('JUPYTERHUB_SQLITEDB_PATH'))
            c = sql_cnn.cursor()
            query = "UPDATE `users` SET `password`= '{}'WHERE `username`='{}' ".format(input_password, username)
            c.execute(query)
            sql_cnn.commit()
            c.close()
            sql_cnn.close()
        else:
            print("only admin has the privilege")



