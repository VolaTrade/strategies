
# echo_handler.py
from .generated import echo_pb2_grpc, echo_pb2
from .commons.decorators import timeit
import logging

class Echoer(echo_pb2_grpc.EchoServicer):

    @timeit
    def Reply(self, request, context):

        logging.debug(f"Received request with message {request.message}")
        return echo_pb2.EchoReply(message=f'You said: {request.message}')
