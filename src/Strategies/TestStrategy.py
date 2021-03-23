from .strategy_interface import StrategyInterface

class TestStrategy(StrategyInterface):

    def __init__(self):
        super().__init__()
        self.indicators = ['pederson_confidence']

    def check_buy(self, params):
        if params['pederson_confidence'] > .59:
            return True

    def check_sell(self, params):
        return False