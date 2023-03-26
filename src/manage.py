from app import app, db, User, Category

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Category=Category)