from abc import ABC, abstractmethod
from src.profitmargin.stoploss import StopLoss as SL

price = "price"

class Strategy():

    class IndicatorArgException(Exception):
        def __init__(self, message):
            super().__init__(message)

    def __init__(self, stoploss=None, trailing=None, percent=10):
        self.buy_indicators, self.sell_indicators  = [], []
        self.stop_logic = SL(
                            trailing=trailing, 
                            percent=percent
                            ) if stoploss is True else None

        if self.stop_logic is not None:
            self.sell_indicators.append(price)
    
    def buy_check(self, indicators):
        return True 
    
    @staticmethod 
    def validate_params(buy):
        def validate_decorator(fn):
            def validation_wrapper(self, *args, **kw):
                provided_indicators = set([e for e in args[0].keys()])
                desired_indicators = set(self.buy_indicators if buy else self.sell_indicators)

                if provided_indicators != desired_indicators:
                    raise self.IndicatorArgException(
                                                        f"""Provided indicator keys don't match desired ones by strategy \n
                                                        Expected: {desired_indicators}\n
                                                        Actual: {provided_indicators}"""
                                                    )
                
                return fn(self, *args, **kw)
            return validation_wrapper
        return validate_decorator

    @staticmethod
    def profit_margin(fn):
        def stop_wrapper(self, *args, **kw):
            if self.stop_logic is not None and self.stop_logic.update(args[0]['price']) is True:
                return True 
            else: 
                return fn(self, *args, **kw)

        return stop_wrapper
