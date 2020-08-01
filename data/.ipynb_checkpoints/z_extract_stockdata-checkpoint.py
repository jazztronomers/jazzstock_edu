import common.connector_db as db

stockcode= '079940'

def extract(stockcode):

    df = db.selectpd('''SELECT STOCKCODE, DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOLUME 
                        FROM jazzdb.T_STOCK_OHLC_MIN 
                        WHERE STOCKCODE='%s' 
                        AND DATE="2020-07-31"'''%(stockcode))
    df.to_csv('stock_ohlc_%s_200731.csv'%(stockcode), index=False)
                 

for eachcode in ['079940','093320','000020']:
    extract(eachcode)