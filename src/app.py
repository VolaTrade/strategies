# app.py
from concurrent import futures
import grpc
import logging
from .generated import echo_pb2_grpc, manager_pb2_grpc, executor_pb2_grpc
from .echo_client import Echoer
from .manager_client import Manager
from .executor_client import Executor 
from .commons.settings import SERVER_PORT, MAX_THREADS
class Server:
    
    @staticmethod
    def run():
        logging.debug(f"Setting max threads to: {MAX_THREADS}")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_THREADS))
        echo_pb2_grpc.add_EchoServicer_to_server(Echoer(), server)
        manager_pb2_grpc.add_ManagerServicer_to_server(Manager(), server)
        executor_pb2_grpc.add_ExecutorServicer_to_server(Executor(), server)
        server.add_insecure_port(f"[::]:{SERVER_PORT}")
        logging.debug("Server started")
        server.start()
        server.wait_for_termination()
