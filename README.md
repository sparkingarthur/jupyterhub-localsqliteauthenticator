# Jupyterhub-SQLiteAuthenticator
> Authenticate Jupyterhub with a sqlite3 user database.
> Author: sparkingarthur@163.com
## Installation
Run this command to install:

```
git clone https://github.com/sparkingarthur/jupyterhub-localsqliteauthenticator.git
cd jupyterhub-localsqliteauthenticator
python setup.py install 
```

In your `jupyter_config.py` file, add or modify the following line to set the authentication method:

```
c.JupyterHub.authenticator_class = 'sqliteauthenticator.SQLiteAuthenticator'
```

Additionally, set the following environment variables to point to your Sqlite3 users database:

- `JUPYTERHUB_SQLITEDB_PATH` - path of sqlite db-file.
e.g. 
```
export JUPYTERHUB_SQLITEDB_PATH=/etc/jupyterhub/jupyterhub-users.db 
```
or you can do this in your python script like this:
```
os.environ["JUPYTERHUB_SQLITEDB_PATH"]="/etc/jupyterhub/jupyterhub-users.db"
```
## Usage

The database defined in `JUPYTERHUB_SQLITEDB_PATH` should have a table called `users` which has columns `username` and `password`.

- `username` should contain the plaintext username to be used by Jupyterhub
- `password` should contain the user password with ASE method ( http://chrissimpkins.github.io/crypto/ )
-  The setup.py script will setup a default sqlite db (with path in /etc/jupyterhub/jupyterhub-users.db), where the table `users` will have only one user 'admin' with password '' (blank string) ,you can change the password of 'admin' and try to use the methods in sqliteoperator-te.py to add more users (see test examples shown in sqliteoperator-te.py).
	
