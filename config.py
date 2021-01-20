class Development:
    """ Development config. We use Debug mode """

    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    APPNAME = "OpenMonitoringDev"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


class Production:
    """ Production config. We use Debug mode false """

    PORT = 8080
    DEBUG = False
    TESTING = False
    ENV = 'production'
    APPNAME = "OpenMonitoringProd"