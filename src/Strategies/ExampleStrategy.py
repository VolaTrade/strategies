from .strategy_interface import StrategyInterface

class ExampleStrategy(StrategyInterface):

    def __init__(self):
        super().__init__()
        self.indicators = ['pederson_confidence']
        self.buyHit, self.sellHit = None, None 

    def check_buy(self, params):
        self.buyHit = True 
        if params['pederson_confidence'] > .59:
            return True

    def check_sell(self, params):
        self.sellHit = True 
        return False