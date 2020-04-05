from application import app, db
from application.user_model import User

@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'User' : User}