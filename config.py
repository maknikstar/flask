import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
# 'sqlite:///' + os.path.join(basedir, 'app.db')
  DB_NAME = 'flaskdb'
  DB_USER = 'flaskuser'
  DB_PASS = 'flaskpassword'
  DB_PORT = "5432"
  SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASS}@localhost:{DB_PORT}/{DB_NAME}'
  # SQLALCHEMY_DATABASE_URI = 'postgresql://flaskuser:flaskpassword@localhost:5432/postgres'