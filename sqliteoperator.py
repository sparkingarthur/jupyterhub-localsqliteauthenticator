#coding=utf-8
import sqlite3
import os
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key='jupyterhubkeykey'):
        self.key = key
        self.mode = AES.MODE_CBC
        self.length = 16

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        count = len(text)
        # padding to length
        add = self.length - (count % self.length)
        text = text + ('\0' * add)
        #print(len(text))
        self.ciphertext = cryptor.encrypt(text)
        # turn to hex string
        return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))#strip padding
        return plain_text.rstrip(b'\0')



if __name__ == '__main__':
    def _verify_password(username,password):
        encryptor = prpcrypt()
        try:
            sql_cnn = sqlite3.connect(os.getenv('JUPYTERHUB_SQLITEDB_PATH'))
            #print("connect db sucessfully")
            cursor = sql_cnn.cursor()
            sql = ("SELECT password FROM users WHERE username = '{}'").format(username) # select from the database
            #print(sql)
            cursor.execute(sql)
            input_password = encryptor.encrypt(password).decode()
           #print(input_password)
            user_password = cursor.fetchone()[0]
           #print(user_password)
            if user_password == input_password:
                cursor.close()
                sql_cnn.close()
                return True
            else:
                cursor.close()
                sql_cnn.close()
                return False
        except:
            try:
                cursor.close()
                sql_cnn.close()
            except:
                pass
            finally:
                print("wrong database/username/password, "
                      "please check your JUPYTERHUB_SQLITEDB_PATH/username/password....")
                return False


    print(_verify_password('taop','987654321'))
    print(_verify_password('lishijie009', '123456'))

