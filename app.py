from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, template_mode='bootstrap4')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


class UserModelView(ModelView):
    details_modal = True
    create_modal = True
    edit_modal = True
    can_view_details = True


admin.add_view(UserModelView(User, db.session))
