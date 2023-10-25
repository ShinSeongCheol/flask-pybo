from config.default import *
from logging.config import dictConfig

SQLALCHEMY_DATABASE_URI = "sqlite:///{}".format(os.path.join(BASE_DIR, "pybo.db"))
SQLALCHEMY_MODIFICATIONS = False
SECRET_KEY = b"\x84\xdf\xb5\x13\xac\xfd\x8f[\xc2)<\xc9\xfb\xd8N\xb3"

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            }
        },
        "handler": {
            "file": {
                "level": "INFO",
                "class": "logging.handlers.RotatingFileHandler",
                "filename": os.path.join(BASE_DIR, "logs/myproject.log"),
                "maxBytes": 1024 * 1024 * 5,
                "backupCount": 5,
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["file"]},
    },
)
