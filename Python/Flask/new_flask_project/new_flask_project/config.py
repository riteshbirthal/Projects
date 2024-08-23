

class Config:
    SECRET_KEY = 'e497e8020eb5c230e63c92c232359575'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "test@gmail.com"
    MAIL_PASSWORD = "test1234"