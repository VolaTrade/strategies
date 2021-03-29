
"""
Stop Loss Logic
"""


class StopLoss:

    def __init__(self, trailing: bool=True, percent: float=10.0):
        # Global variables
        self.percent: float = percent  # PercentSL...input by user : DEFAULT 0
        self.global_high: float = 0  # global high ..ie highest value found in session : DEFAULT 0
        self.current_price: float = 0  # current price... obtained by CCXT API : DEFAULT 0
        self.last_price: float = 0  # last given price... updated in function call : DEFAULT 0
        self.stop_value: float = 0  # Value that program will sell upon
        self.sold = False  # boolean to tell whether sell should be made or not
        self.stop_loss_func = lambda price: float((float(price) * float("." + f"{100 - self.percent}".replace(".", ""))))
        self.trail = trailing

    def reset(self):
        """
        Resets values after sell is made
        """
        self.global_high: float = 0  # global high ..ie highest value found in session : DEFAULT 0
        self.current_price: float = 0  # current price... obtained by CCXT API : DEFAULT 0
        self.last_price: float = 0  # last given price... updated in function call : DEFAULT 0
        self.stop_value: float = 0  # Value that program will sell upon

    def __repr__(self) -> (str):
        """
        string representation
        """
        return str(f"""
                       Current price : {str(self.current_price)}\n 
                       Global high : {str(self.global_high)}\n 
                       Stop loss value : {str(self.stop_value)}\n 
                       Stop loss percent : {str(self.percent)}\n
                    """
                  )

    def update(self, price: float) -> (bool):
        """
        @:param price
        @:returns boolean based on percentageSL
        """
        if not isinstance(price, float):
            raise TypeError(f"Wrong parameter... expecting float, got {type(price)} instead")

        self.last_price, self.current_price = price, price

        if self.global_high == 0:
            self.global_high = self.current_price

        if self.trail and self.current_price > self.global_high:
            self.global_high = price

        self.stop_value = self.stop_loss_func(float(self.global_high))
        
        if self.current_price <= self.stop_value:
            self.reset()
            return True

        return False   
