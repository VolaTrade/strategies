from __future__ import print_function
import logging

import grpc
import time
from src.commons.settings import SERVER_PORT
from src.generated import echo_pb2, manager_pb2, executor_pb2
from src.generated import echo_pb2_grpc, manager_pb2_grpc, executor_pb2_grpc
from src.commons.status_codes import StatusCode

def test_spawn_invalid_strategy():
  with grpc.insecure_channel(f'localhost:{SERVER_PORT}') as channel:
        stub = manager_pb2_grpc.ManagerStub(channel)
        response = stub.SpawnStrategy(manager_pb2.SpawnRequest(sessionID="101", strategyID="IDONTEXIST"))

        assert response.code == StatusCode.INVALID_ARGUMENT.value
        assert response.message == "StrategyID missing"
