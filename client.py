from __future__ import print_function
import logging

import grpc
import time
from src.commons.settings import SERVER_PORT
from src.generated import echo_pb2, manager_pb2, executor_pb2
from src.generated import echo_pb2_grpc, manager_pb2_grpc, executor_pb2_grpc


def run():
    with grpc.insecure_channel(f'localhost:{SERVER_PORT}') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.SpawnStrategy(manager_pb2.SpawnRequest(sessionID="101", strategyID="TestStrategy"))
    print("Response --> ", response)

    with grpc.insecure_channel(f'localhost:{SERVER_PORT}') as channel:
        stub = executor_pb2_grpc.ExecutorStub(channel)
        start = time.time()

        response = stub.ExecuteStrategyUpdate(executor_pb2.ExecuteRequest(sessionID="101", stratParams={"pederson_confidence": .4}, buyUpdate=True))
    
        print(time.time()-start)
    print("Response msg --> ", response.message)
    print("Response value --> ", response.value)
    
if __name__ == '__main__':
    logging.basicConfig()
    run()