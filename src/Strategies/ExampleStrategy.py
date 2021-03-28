from .strategy import Strategy

class ExampleStrategy(Strategy):

    def __init__(self, stoploss=None, trailing=None, percent=10):
        super().__init__(stoploss=stoploss, trailing=trailing, percent=percent)
        self.buy_indicators.extend(['pederson_confidence'])
        self.sell_indicators.extend(['pederson_confidence'])
        self.buyHit, self.sellHit = None, None 

    @Strategy.validate_params(buy=True)
    def check_buy(self, params):
        self.buyHit = True 
        if params['pederson_confidence'] > .59:
            return True

    @Strategy.validate_params(buy=False)
    @Strategy.profit_margin
    def check_sell(self, params):
        self.sellHit = True 
        return False