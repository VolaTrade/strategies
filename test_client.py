from src.executor_client import Executor
from src.manager_client import Manager 
from src.generated import executor_pb2, manager_pb2
from src.commons.status_codes import StatusCode 
from src.commons.globals import LiveStrategies
from src.strategies.ExampleStrategy import ExampleStrategy


class TestManagerSpawn:

    def test_session_id_invalid(self):
        man = Manager()
        resp = man.SpawnStrategy(manager_pb2.SpawnRequest(strategyID="Test"), None)
        assert resp.code == StatusCode.INVALID_ARGUMENT.value
        assert "sessionID missing" == resp.message 

    def test_strategy_id_invalid(self):
        man = Manager()
        resp = man.SpawnStrategy(manager_pb2.SpawnRequest(sessionID="123"), None)
        assert resp.code == StatusCode.INVALID_ARGUMENT.value
        assert "strategyID missing" == resp.message 

    def test_session_id_exists(self):
        man = Manager()
        es = ExampleStrategy()
        LiveStrategies["123"] = es
        resp = man.SpawnStrategy(manager_pb2.SpawnRequest(sessionID="123", strategyID="ExampleStrategy"), None)

        del LiveStrategies["123"]
        assert resp.code == StatusCode.ALREADY_EXISTS.value
        assert "session already exists" == resp.message   

    def test_strategy_not_found_for_id(self):
        man = Manager()
        resp = man.SpawnStrategy(manager_pb2.SpawnRequest(sessionID="123", strategyID="IDONTEXIST"), None)

        assert resp.code == StatusCode.NOT_FOUND.value
        assert "Strategy provided not found" == resp.message   

    def test_success(self):
        man = Manager()
        resp = man.SpawnStrategy(manager_pb2.SpawnRequest(sessionID="123", strategyID="ExampleStrategy"), None)

        assert resp.code == StatusCode.OK.value 
        assert resp.message == "ok"
        assert "123" in LiveStrategies
        del LiveStrategies["123"]

class TestManagerDeletion:
    def test_session_id_invalid(self):
        man = Manager()
        resp = man.DeleteStrategy(manager_pb2.DeletionRequest(), None)
        assert resp.code == StatusCode.INVALID_ARGUMENT.value
        assert "sessionID missing" == resp.message 

    def test_session_id_missing(self):
        man = Manager()
        resp = man.DeleteStrategy(manager_pb2.DeletionRequest(sessionID="111"), None)
        assert resp.code == StatusCode.NOT_FOUND.value
        assert "sessionID not found" == resp.message 

    def test_delete_success(self):
        es = ExampleStrategy()
        LiveStrategies["1"] = es
        man = Manager()
        resp = man.DeleteStrategy(manager_pb2.DeletionRequest(sessionID="1"), None)
        assert resp.code == StatusCode.OK.value
        assert "ok" == resp.message 
        assert "1" not in LiveStrategies 

class TestExecutor:

    def test_session_id_invalid(self):
        ex = Executor()
        resp = ex.ExecuteStrategyUpdate(executor_pb2.ExecuteRequest(stratParams={}, buyUpdate=True), None)
        assert resp.code == StatusCode.INVALID_ARGUMENT.value
        assert "sessionID missing" == resp.message 

    def test_strat_params_invalid(self):
        ex = Executor()
        req = executor_pb2.ExecuteRequest(sessionID="111", buyUpdate=True)
        resp = ex.ExecuteStrategyUpdate(req, None)

        assert resp.code == StatusCode.INVALID_ARGUMENT.value
        assert "stratParams missing" == resp.message

    def test_session_id_missing(self):
        ex = Executor()
        resp = ex.ExecuteStrategyUpdate(executor_pb2.ExecuteRequest(sessionID="111", stratParams={"ads": 23.5}, buyUpdate=True), None)
        assert resp.code == StatusCode.NOT_FOUND.value
        assert "sessionID not found" == resp.message 

    def test_strategy_params_mismatch(self):
        ex = Executor()
        resp = ex.ExecuteStrategyUpdate(executor_pb2.ExecuteRequest(sessionID="111", stratParams={"ads": 23.5}, buyUpdate=True), None)

        assert resp.code == StatusCode.NOT_FOUND.value
        assert "sessionID not found" == resp.message 

    def test_buy_update_success(self):
        es = ExampleStrategy()
        LiveStrategies["1"] = es
        ex = Executor()
        resp = ex.ExecuteStrategyUpdate(executor_pb2.ExecuteRequest(sessionID="1", stratParams={"pederson_confidence": .9}, buyUpdate=True), None)

        assert resp.message == "ok" 
        assert resp.code == StatusCode.OK.value
        assert resp.value == True
        assert es.buyHit == True 
        assert es.sellHit == None 

    def test_sell_update_success(self):
        es = ExampleStrategy()
        LiveStrategies["1"] = es
        ex = Executor()
        resp = ex.ExecuteStrategyUpdate(executor_pb2.ExecuteRequest(sessionID="1", stratParams={"pederson_confidence": .9}, buyUpdate=False), None)

        assert resp.message == "ok" 
        assert resp.code == StatusCode.OK.value
        assert resp.value == False
        assert es.buyHit == None 
        assert es.sellHit == True