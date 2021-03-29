from src.executor_client import Executor
from src.manager_client import Manager 
from src.generated import executor_pb2, manager_pb2
from src.commons.status_codes import StatusCode 
from src.commons.globals import LiveStrategies
from src.strategies.ExampleStrategy import ExampleStrategy
from src.profitmargin.stoploss import StopLoss
from src.strategies.strategy import Strategy 


class DummyStrategy(Strategy):

    def __init__(self, stoploss=None, trailing=None, percent=10):
        super().__init__(stoploss, trailing, percent)
    
        self.buy_indicators.extend(["EMA"])
        self.sell_indicators.extend(["EMA"])


    @Strategy.validate_params(buy=True)
    def check_buy(self, params):
        return True 
    
    @Strategy.validate_params(buy=False)
    @Strategy.profit_margin        
    def check_sell(self, params):
            return False 
class TestStrategy: 
    class TestDecorators:
        
        def test_validation_success(self):
            strat = DummyStrategy(stoploss=True)

            test_passed = True 

            try:
                strat.check_buy(
                    {
                        "EMA": 32,
                    }
                )
            
            except Strategy.IndicatorArgException:
                test_passed = False 

            assert test_passed is True

        def test_validation_fail(self):

            strat = DummyStrategy(stoploss=True)

            test_passed = False 

            try:
                strat.check_sell(
                    {
                        "EMA": 32,
                    }
                )
            
            except Strategy.IndicatorArgException:
                test_passed = True 

            
            assert test_passed is True
        


class TestStopLoss:
    class TestStopWithStrategy:

        def test_stop_loss_returns_sell_upon_criteria_meet(self):
            ex = ExampleStrategy(stoploss=True, trailing=True, percent=25.5)

            iter1 = ex.check_sell(
                {
                    "pederson_confidence": .9, 
                    "price":    100.0,
                },
            )
            assert iter1 is False

            iter2 = ex.check_sell(
                {
                    "pederson_confidence": .9, 
                    "price":    74.5,
                },
            )
            assert iter2 is True

        def test_stop_loss_doesnt_work_when_not_activated(self):
            ex = ExampleStrategy(stoploss=False)

            pass_test = False 
            try:
                ex.check_sell(
                        {"price":    100.0},
                    )
            except Strategy.IndicatorArgException as e:
                pass_test = True 

            assert pass_test



    class TestStopLossNonTrailing:

        def test_non_trailing_works(self):
            sl = StopLoss(percent=10.0, trailing=False)
            sl.percent = 10.0
            sl.update(100.0)
            sl.update(150.0)
            expected = True 
            actual = sl.update(89.99)

            assert expected == actual 

    class TestTrailingStop:

            def test_sell_logic_float_greater_than_ten(self):
                sl = StopLoss()
                sl.percent = 25.5
                sl.update(100.0)
                expected = True 
                actual = sl.update(74.5)

                assert expected ==  actual


            def test_sell_logic_int_greater_than_ten(self):
                sl = StopLoss()
                sl.percent = 25
                sl.update(100.0)
                expected = True 
                actual = sl.update(75.0)

                assert expected ==  actual

            def test_sell_logic_float_less_than_ten(self):
                sl = StopLoss()
                sl.percent = 1.1
                sl.update(100.0)
                expected = 98.9 
                actual = sl.stop_value
                
                assert expected ==  actual


            def test_sell_logic_int_less_than_ten(self):
                sl = StopLoss()
                sl.percent = 1
                sl.update(100.0)
                expected = 99.0
                actual = sl.stop_value

                assert expected ==  actual

            
            def test_sel_lLogic_int_equal_ten(self):
                sl = StopLoss()
                sl.percent = 10
                sl.update(100.0)
                expected = 90.0
                actual = sl.stop_value

                assert expected ==  actual

class TestServerLogic:
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
            assert resp.value is True
            assert es.buyHit is True 
            assert es.sellHit is None 

        def test_sell_update_success(self):
            es = ExampleStrategy()
            LiveStrategies["1"] = es
            ex = Executor()
            resp = ex.ExecuteStrategyUpdate(executor_pb2.ExecuteRequest(sessionID="1", stratParams={"pederson_confidence": .9}, buyUpdate=False), None)

            assert resp.message == "ok" 
            assert resp.code == StatusCode.OK.value
            assert resp.value is False
            assert es.buyHit is None 
            assert es.sellHit is True