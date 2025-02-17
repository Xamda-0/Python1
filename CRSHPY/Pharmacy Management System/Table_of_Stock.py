import pandas as pd
def StockTable():
    fileName = 'Medications_With_Price.csv'
    data = pd.read_csv(fileName)



    print(data)

