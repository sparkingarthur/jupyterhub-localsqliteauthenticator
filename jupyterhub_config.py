c.JupyterHub.bind_url = 'http://:9002'
c.LocalAuthenticator.create_system_users = True
c.Authenticator.delete_invalid_users = True
c.JupyterHub.authenticator_class = 'sqliteauthenticator.SQLiteAuthenticator'

