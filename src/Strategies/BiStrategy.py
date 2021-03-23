from .strategy_interface import StrategyInterface

class BiStrategy(StrategyInterface):

    def __init__(self):
        super().__init__()
        self.value_list = []

    def check_buy(self, params):
        if params['pedersen_confidence'] > .59:
            return True

    def check_sell(self, params):
        return False