#executer_client 
from .generated.executor_pb2_grpc import ExecutorServicer
from .generated.executor_pb2 import ExecuteRequest, ExecuteReply 
from .commons.globals import LiveStrategies
from .commons.status_codes import StatusCode
from .commons.decorators import timeit 
from .strategies.strategy import Strategy
import logging

not_valid = lambda value: True if len(value) == 0 else False

def generate_response(message: str, code: StatusCode, update_value: bool=None) -> (ExecuteReply):
    response = ExecuteReply(
                            value=update_value,
                            message=message,
                            code=code
                            )
    logging.debug(response)
    return response

class Executor(ExecutorServicer):

    @timeit
    def ExecuteStrategyUpdate(self, request: ExecuteRequest, context) -> (ExecuteReply):
        logging.debug(f"sessionID: {request.sessionID} , stratParams: {request.stratParams}, buyUpdate: {request.buyUpdate}")
        if not_valid(request.sessionID):
            return generate_response("sessionID missing", StatusCode.INVALID_ARGUMENT.value)

        if not_valid(request.stratParams):
            return generate_response("stratParams missing", StatusCode.INVALID_ARGUMENT.value)

        if request.sessionID not in LiveStrategies:
            return generate_response("sessionID not found", StatusCode.NOT_FOUND.value)
        
        strat_class = LiveStrategies[request.sessionID]
        
        update_value = None 

        try: 
            if request.buyUpdate is True: 
                update_value = strat_class.check_buy(request.stratParams)

            else:
                update_value = strat_class.check_sell(request.stratParams)

        except Strategy.IndicatorArgException as iae:
            logging.error(iae.message)
            return generate_response(iae.message, StatusCode.INVALID_ARGUMENT.value)

        return generate_response("ok", StatusCode.OK.value, update_value=update_value)