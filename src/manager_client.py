#spawn_client.py 
from .generated import manager_pb2_grpc, manager_pb2
from .commons.globals import LiveStrategies, get_strategy
from .commons.status_codes import StatusCode
import logging

not_valid = lambda value: True if len(value) == 0 else False

def generate_spawn_response(message: str, code: StatusCode, params:dict=None):
    response = manager_pb2.SpawnReply(
                            indicators=params,
                            message=message,
                            code=code
                            )
    logging.debug(response)
    return response

def generate_deletion_response(message: str, code: StatusCode):
    response = manager_pb2.DeletionReply(
                            message=message,
                            code=code
                            )
    logging.debug(response)
    return response

class Manager(manager_pb2_grpc.ManagerServicer):

    def SpawnStrategy(self, request, context):

        logging.debug(f"sessionID: {request.sessionID} , strategyID: {request.strategyID}")
        if not_valid(request.sessionID):
            return generate_spawn_response("sessionID missing", StatusCode.INVALID_ARGUMENT.value)

        if not_valid(request.strategyID):
            return generate_spawn_response("strategyID missing", StatusCode.INVALID_ARGUMENT.value)

        if request.sessionID in LiveStrategies:
            return generate_spawn_response("session already exists", StatusCode.ALREADY_EXISTS.value)

        strategy_class = None 
        try: 
            strategy_class = get_strategy(request.strategyID)()

        except Exception as e:
            logging.error(e)
            return generate_spawn_response("Strategy provided not found", StatusCode.NOT_FOUND.value)

        LiveStrategies[request.sessionID] = strategy_class
        return generate_spawn_response("ok", StatusCode.OK.value, params=strategy_class.indicators)
    
    def DeleteStrategy(self, request, context):
        logging.debug(f"sessionID: {request.sessionID}")

        if not_valid(request.sessionID):
            return generate_deletion_response("sessionID missing", StatusCode.INVALID_ARGUMENT.value)


        if request.sessionID not in LiveStrategies:
            return generate_deletion_response("sessionID not found", StatusCode.NOT_FOUND.value)

        del LiveStrategies[request.sessionID]
        logging.debug(f"Deleted session: {request.sessionID}")
        return generate_deletion_response("ok", StatusCode.OK.value)
