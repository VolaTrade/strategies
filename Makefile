IMG=strat_api
APP=strategies_api

.PHONY: run 
run: 
	python3 main.py

.PHONY: gen-protos 
gen-protos:
	@python -m grpc_tools.protoc -I.\
	       	--python_out=./src/generated --grpc_python_out=./src/generated \
		./src/proto/*.proto
	@echo "Generated protobufs"
	@mv src/generated/src/proto/*.py src/generated
	@rm -rf src/generated/src/

.PHONY: docker-build 
docker-build: 
	docker build -t $(IMG):latest . 

.PHONY: docker-run 
docker-run: 
	docker run -d --name $(APP) -p 9000:9000 $(IMG)

.PHONY: docker-down
docker-down:
	docker stop $(APP)
	docker rm $(APP)

.PHONY: test
test:
	pytest -v -rx tests.py

.PHONY: upload-protos 
upload-protos:
	@cd ops/protohook && docker-compose build

