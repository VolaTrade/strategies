#executer_client 
from .generated import executor_pb2, executor_pb2_grpc
from .commons.globals import LiveStrategies
from .commons.status_codes import StatusCode 
import logging

not_valid = lambda value: True if value is None else False
def generate_response(value: bool, message: str, code: StatusCode):
    response = executor_pb2.ExecuteReply(
                            value=value,
                            message=message,
                            code=code
                            )
    logging.debug(response)
    return response

class Executor(executor_pb2_grpc.ExecutorServicer):

    def ExecuteStrategyUpdate(self, request, context):
        logging.debug(f"sessionID: {request.sessionID} , stratParams: {request.stratParams}, buyUpdate: {request.buyUpdate}")
        if not_valid(request.sessionID):
            return generate_response(False, "sessionID missing", StatusCode.INVALID_ARGUMENT.value)

        if not_valid(request.stratParams):
            return generate_response(False, "stratParams missing", StatusCode.INVALID_ARGUMENT.value)

        if not_valid(request.buyUpdate):
            return generate_response(False, "buyUpdate missing", StatusCode.INVALID_ARGUMENT.value)

        if request.sessionID not in LiveStrategies:
            return generate_response(False, "SessionID not found", StatusCode.NOT_FOUND.value)

        
        strat_class = LiveStrategies[request.sessionID]

        if request.buyUpdate is True: 
            update_value = strat_class.check_buy(request.stratParams)

        else:
            update_value = strat_class.check_sell(request.stratParams)

        return generate_response(update_value, "Ok", StatusCode.OK.value)