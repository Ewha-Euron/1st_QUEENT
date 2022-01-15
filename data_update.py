import pandas as pd
import yfinance as yf
from yfinance import shared
from datetime import datetime

def updates():
    #기존 데이터 주소 입력!!!!
    df = pd.read_csv("./preprocessed_data.csv")
    # 당일 데이터 저장
    date = datetime.today().strftime('%Y.%m.%d')
    date_for_download = datetime.today().strftime('%Y-%m-%d')

    li = yf.download(['AAPL', 'AMZN','^IXIC','^NYA','^GSPC','^FTSE','^BSESN','^RUT','000001.SS','CL=F','GC=F','^VIX','DX=F','GOOG','MSFT'],start = date_for_download)
    
    ################ error handling 
    errors = shared._ERRORS

    if errors:
        print(errors)
    
    if 'AMZN' in errors.keys():
        amzn_open = '#N/A'
        amzn_High = '#N/A'
        amzn_Low = '#N/A'
        amzn_Close = '#N/A'
        amzn_Volume ='#N/A'
    else:
        amzn_open = (li['Open']['AMZN'].values)[0]
        amzn_High = (li['High']['AMZN'].values)[0]
        amzn_Low = (li['Low']['AMZN'].values)[0]
        amzn_Close = (li['Close']['AMZN'].values)[0]
        amzn_Volume = (li['Volume']['AMZN'].values)[0]
    
    if 'AAPL' in errors.keys():
        appl = '#N/A'
    else:
        appl = (li['Close']['AAPL'].values)[0]
    
    if 'GOOG' in errors.keys():
        google = '#N/A'
    else:
        google = (li['Close']['GOOG'].values)[0]
    
    if '^BSESN' in errors.keys():
        bse = '#N/A'
    else:
        bse = (li['Close']['^BSESN'].values)[0]
    
    if '^GSPC' in errors.keys():
        snp = '#N/A'
    else:
        snp = (li['Close']['^GSPC'].values)[0]
    
    if '^RUT' in errors.keys():
        russell = '#N/A'
    else:
        russell = (li['Close']['^RUT'].values)[0]
    
    if 'CL=F' in errors.keys():
        oil = '#N/A'
    else:
        oil = (li['Close']['CL=F'].values)[0]
    
    if '^IXIC' in errors.keys():
        nasdaq = '#N/A'
    else:
        nasdaq = (li['Close']['^IXIC'].values)[0]
    
    if 'MSFT' in errors.keys():
        msft = '#N/A'
    else:
        msft = (li['Close']['MSFT'].values)[0]
    
    if '^FTSE' in errors.keys():
        ftse = '#N/A'
    else:
        ftse = (li['Close']['^FTSE'].values)[0]
    
    if '^VIX' in errors.keys():
        vix = '#N/A'
    else:
        vix = (li['Close']['^VIX'].values)[0]
    
    if '000001.SS' in errors.keys():
        sse = '#N/A'
    else:
        sse = (li['Close']['000001.SS'].values)[0]
    
    if 'GC=F' in errors.keys():
        gold = '#N/A'
    else:
        gold = (li['Close']['GC=F'].values)[0]
    
    if 'DX=F' in errors.keys():
        usd = '#N/A'
    else:
        usd = (li['Close']['DX=F'].values)[0]
    if '^NYA' in errors.keys():
        nyse = '#N/A'
    else:
        nyse = (li['Close']['^NYA'].values)[0]
    


    row = {'Date':date, 'Open':amzn_open, 'High':amzn_High, 'Low':amzn_Low, 'Close':amzn_Close, 'Volume':amzn_Volume, 'NASDAQ':nasdaq, 'NYSE':nyse,'S&P 500':snp, 'FTSE100':ftse, 'BSE SENSEX':bse, 'RUSSELL2000':russell, 'SSE':sse, 'Crude Oil':oil,'Gold':gold, 'VIX':vix, 'USD index':usd, 'Apple':appl, 'Google':google, 'Microsoft':msft}

    df=df.append(row, ignore_index=True)

    #저장하고싶은 파일 이름 저장
    df.to_csv('./preprocessed_data.csv',index = False)
    return row