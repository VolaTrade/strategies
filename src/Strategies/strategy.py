from src.profitmargin.stoploss import StopLoss as SL
from typing import Any, Callable, TypeVar, Union

F = TypeVar('F', bound=Callable[..., Any])
PRICE: str = "price"

class Strategy():

    class IndicatorArgException(Exception):
        def __init__(self, message: str):
            super().__init__(message)

    def __init__(self, stoploss: bool=None, trailing: bool=None, percent: float=10):
        self.buy_indicators, self.sell_indicators  = [], []

        self.stop_logic = SL(trailing=trailing, 
                             percent=percent
                            ) if stoploss is True else None

        if self.stop_logic is not None: 
            self.sell_indicators.append(PRICE)
    
    @staticmethod 
    def validate_params(buy: bool) -> (F):
        def validate_decorator(func: F) -> (F):
            def validation_wrapper(self, *args, **kw) -> (F):
                provided_indicators = set([e for e in args[0].keys()])
                desired_indicators = set(self.buy_indicators if buy else self.sell_indicators)

                if provided_indicators != desired_indicators:
                    raise self.IndicatorArgException(f"""
                                                        Provided indicator keys don't match desired ones by strategy\n
                                                        Expected: {desired_indicators}\n
                                                        Actual: {provided_indicators}
                                                      """
                                                    )
                
                return func(self, *args, **kw)
            return validation_wrapper
        return validate_decorator

    @staticmethod
    def profit_margin(func: F) -> (Union[bool, F]):
        def stop_wrapper(self, *args, **kw):
            if self.stop_logic is not None and self.stop_logic.update(args[0][PRICE]) is True:
                return True
            
            return func(self, *args, **kw)

        return stop_wrapper
