class Config:
    DEBUG = True
    SECRET_KEY = r'cyL\x9a\xc2\x9eR\x82\xbf\xbb\x8aX'

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/facebook'

class Production(Config):
    DEBUG = False
    

app_config = {
    'production': Production,
    'development': Development
}