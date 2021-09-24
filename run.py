from flaskblog import create_app, db
import sys
import logging

app = create_app()
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run()
    with app.app_context():
        db.create_all()