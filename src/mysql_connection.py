from sqlalchemy import create_engine
def connection_mysql():
    engine =create_engine("mysql+pymysql://root:password@localhost/datamining")
    return engine