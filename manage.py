from app import create_app, db  
from flask_script import Manager,Server
from app.models import User, Role
from  flask_migrate import Migrate, MigrateCommand

#creating the app instance
app = create_app('development')

#create instances of imported flask_script classes
manager = Manager(app)
manager.add_command('server',Server)


#creating an instance of the app instance
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User ,Role = Role)

if __name__ == '__main__':
    manager.run()
