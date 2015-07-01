import pandas as pd
from sqlalchemy import create_engine, Table, MetaData, schema

class DB:
    def __init__(self, **kwargs):
        self.db_type = kwargs['db_type']
        self.username = kwargs['username']
        self.passwd = kwargs['passwd']
        self.host = kwargs['host']
        self.db_name = kwargs['db_name']

        return

    def getEngineConnector(self):
        engine_str = "%s://%s:%s@%s/%s" % (self.db_type,
                                         self.username,
                                         self.passwd,
                                         self.host,
                                         self.db_name)
        engine = create_engine(engine_str)
        return engine.connect()

    def setQueryResponseFormat(self, data_structure='dataframe'):
        ''' Setter for the data structure returned from a query.
            Default: Pandas Dataframe '''
        self.query_response_format = data_structure

    def runQuery(self, query):
        connection = self.getEngineConnector()
        results = connection.execute(query)
        if self.query_response_format == 'dataframe':
            df = pd.DataFrame(results.fetchall())
            df.columns = results.keys()
            return pd.DataFrame(df)
        else:
            return connection.execute(query)
