c.JupyterHub.bind_url = 'http://:9002'
c.Authenticator.add_user_cmd =  ['adduser', '--home', '/home/USERNAME']
c.LocalAuthenticator.create_system_users = True
c.Authenticator.delete_invalid_users = True
c.JupyterHub.authenticator_class = 'sqliteauthenticator.SQLiteAuthenticator'
c.Authenticator.admin_users = {'admin'}

from jupyterhub.spawner import LocalProcessSpawner
class MySpawner(LocalProcessSpawner):
    def _notebook_dir_default(self):
        return '/home/' + self.user.name

c.JupyterHub.spawner_class = MySpawner
