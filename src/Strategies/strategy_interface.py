from abc import ABC, abstractmethod

class StrategyInterface(ABC):

    def __init__(self):
        self.indicators = []
    
    @abstractmethod
    def check_buy(self, indicators):
        return True 

    @abstractmethod
    def check_sell(self, indicators):
        return False



