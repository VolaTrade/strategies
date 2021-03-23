#spawn_client.py 
from .generated import manager_pb2_grpc, manager_pb2
from .commons.globals import LiveStrategies, get_strategy
from .commons.status_codes import StatusCode
import logging

not_valid = lambda value: True if value is None else False

def generate_response(success: bool, message: str, code: StatusCode):
    response = manager_pb2.ManagerReply(
                            success=success,
                            message=message,
                            code=code
                            )
    logging.debug(response)
    return response

class Manager(manager_pb2_grpc.ManagerServicer):

    def SpawnStrategy(self, request, context):

        logging.debug(f"sessionID: {request.sessionID} , strategyID: {request.strategyID}")
        if not_valid(request.sessionID):
            return generate_response(False, "SessionID missing", StatusCode.INVALID_ARGUMENT.value)

        if not_valid(request.strategyID):
            return generate_response(False, "StrategyID missing", StatusCode.INVALID_ARGUMENT.value)

        if request.sessionID in LiveStrategies:
            return generate_response(False, "Session already exists", StatusCode.ALREADY_EXISTS.value)

        strategy_class = None 
        try: 
            strategy_class = get_strategy(request.strategyID)()

        except Exception as e:
            logging.error(e)
            return generate_response(False, "Strategy provided not found", StatusCode.NOT_FOUND.value)

        LiveStrategies[request.sessionID] = strategy_class
        return generate_response(True, "Ok", StatusCode.OK.value)
    
    def DeleteStrategy(self, request, context):
        logging.debug(f"sessionID: {request.sessionID}")

        if not_valid(request.sessionID):
            return generate_response(False, "SessionID missing", StatusCode.INVALID_ARGUMENT.value)


        if request.sessionID not in LiveStrategies:
            return generate_response(False, "SessionID not found", StatusCode.NOT_FOUND.value)

        del LiveStrategies[request.sessionID]
        logging.debug(f"Deleted session: {request.sessionID}")
        return generate_response(True, "Ok", StatusCode.OK.value)




