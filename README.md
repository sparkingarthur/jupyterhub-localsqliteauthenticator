# Jupyterhub-SQLAuthenticator
> Authenticate Jupyterhub with a MySQL user database

## Installation

Run this command to install:

```
python setup.py install 
```

In your `jupyter_config.py` file, add or modify the following line to set the authentication method:

```
c.JupyterHub.authenticator_class = 'sqliteauthenticator.SQLiteAuthenticator'
```

Additionally, set the following environment variables to point to your MySQL users database:

- `JUPYTERHUB_SQLITEDB_PATH` - path of sqlite db-file 

## Usage

The database defined in `MYSQL_DB` should have a table called `users` which has columns `username` and `password`.

- `username` should contain the plaintext username to be used by Jupyterhub
- `password` should contain the user password with ASE method ( http://chrissimpkins.github.io/crypto/ )
	