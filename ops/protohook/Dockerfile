FROM python:3.9-alpine AS base

ARG GITHUB_TOKEN

RUN apk add bash ca-certificates git protoc go 

ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /go/bin:$PATH

RUN mkdir -p ${GOPATH}/src ${GOPATH}/bin

RUN go get -u github.com/golang/protobuf/protoc-gen-go


RUN git config --global url."https://${GITHUB_TOKEN}:x-oauth-basic@github.com/volatrade/".insteadOf "https://github.com/volatrade/"

# Set the working directory to /app
WORKDIR /app

COPY src/proto proto_files
COPY ops/protohook/gitman.yaml . 
COPY ops/protohook/write_protos.py . 
COPY ops/protohook/git.py . 

RUN pip install gitman
RUN gitman update

RUN ls *

RUN git config --global user.email "donotreply@volatrade.org"
RUN git config --global user.name "Automation Bot"

RUN python write_protos.py
RUN cd protobufs && python gen_protos.py
RUN python git.py 