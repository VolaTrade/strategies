#spawn_client.py 
from .generated.manager_pb2_grpc import ManagerServicer
from .generated.manager_pb2 import SpawnRequest, SpawnReply, DeletionRequest, DeletionReply
from .commons.globals import LiveStrategies, get_strategy
from .commons.status_codes import StatusCode
from .commons.decorators import timeit

import logging

not_valid = lambda value: True if len(value) == 0 else False

def generate_spawn_response(message: str, code: StatusCode, 
                            buy_params: dict=None, sell_params: dict=None,
                           ) -> (SpawnReply):

    response = SpawnReply(
                            buyIndicators=buy_params,
                            sellIndicators=sell_params,
                            message=message,
                            code=code
                            )
    logging.debug(response)
    return response

def generate_deletion_response(message: str, code: StatusCode) -> (DeletionReply):

    response = DeletionReply(
                            message=message,
                            code=code
                            )
    logging.debug(response)
    return response

class Manager(ManagerServicer):
    
    @timeit
    def SpawnStrategy(self, request: SpawnRequest, context) -> (SpawnReply):

        logging.debug(f"sessionID: {request.sessionID} , strategyID: {request.strategyID}")
        if not_valid(request.sessionID):
            return generate_spawn_response("sessionID missing", StatusCode.INVALID_ARGUMENT.value)

        if not_valid(request.strategyID):
            return generate_spawn_response("strategyID missing", StatusCode.INVALID_ARGUMENT.value)

        if request.sessionID in LiveStrategies:
            return generate_spawn_response("session already exists", StatusCode.ALREADY_EXISTS.value)

        strategy_class = None 
        try: 
            strategy_class = get_strategy(request.strategyID)(
                request.stopLoss,
                request.trailing,
                request.percent,
            )

        except Exception as e:
            logging.error(e)
            return generate_spawn_response("Strategy provided not found", StatusCode.NOT_FOUND.value)

        LiveStrategies[request.sessionID] = strategy_class
        return generate_spawn_response(
                                    "ok",
                                    StatusCode.OK.value,
                                    buy_params=strategy_class.buy_indicators,
                                    sell_params=strategy_class.sell_indicators
                                    )

    @timeit
    def DeleteStrategy(self, request: DeletionRequest, context) -> (DeletionReply):

        logging.debug(f"sessionID: {request.sessionID}")
        if not_valid(request.sessionID):
            return generate_deletion_response("sessionID missing", StatusCode.INVALID_ARGUMENT.value)

        if request.sessionID not in LiveStrategies:
            return generate_deletion_response("sessionID not found", StatusCode.NOT_FOUND.value)

        del LiveStrategies[request.sessionID]
        logging.debug(f"Deleted session: {request.sessionID}")
        return generate_deletion_response("ok", StatusCode.OK.value)
