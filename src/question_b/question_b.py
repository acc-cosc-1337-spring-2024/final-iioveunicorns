#write functions here, don't add input('') statements here!
class Stock():
    def __init__(self, symbol, name):
        self._symbol = symbol
        self._company_name = name
    
    def getSymbol(self):
        return(self._symbol)
    
    def getName(self):
        return(self._company_name)
    
def addToDict(stock, dictionary):
    dictionary[stock.getSymbol()]=stock.getName()

def stock_purchase_history():
    purchaseRecord = {}
    apple = Stock('AAPL','Apple Inc')
    cater = Stock('CAT','Caterpillar')
    kodak = Stock('EK','Eastman Kodak')
    google = Stock('GOOG','Google')
    MS = Stock('MSFT','Microsoft')
    addToDict(apple, purchaseRecord)
    addToDict(cater, purchaseRecord)
    addToDict(kodak, purchaseRecord)
    addToDict(google, purchaseRecord)
    for key, val in purchaseRecord.items():
        print(key, val)
        