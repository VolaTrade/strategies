
FROM python:3.9-alpine AS base


ARG GITHUB_TOKEN

RUN apk add bash ca-certificates git
RUN git config --global url."https://${GITHUB_TOKEN}:x-oauth-basic@github.com/volatrade/".insteadOf "https://github.com/volatrade/"

# Set the working directory to /app
WORKDIR /app
COPY ops/protohook/gitman.yaml . 
COPY ops/protohook/write_protos.py . 
COPY src/proto proto_files

RUN pip install gitman
RUN gitman update

RUN git config --global user.email "donotreply@volatrade.org"
RUN git config --global user.name "Automation Bot"
RUN python write_protos.py
