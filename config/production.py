from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR), 'pybo.db')
SQLALCHEMY_MODIFICATIONS = False
SECRET_KEY = b'\x84\xdf\xb5\x13\xac\xfd\x8f[\xc2)<\xc9\xfb\xd8N\xb3'