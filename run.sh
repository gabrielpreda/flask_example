#!/usr/bin/env bash
docker build -t iris-model-api:dev .
docker run -d -P -p 0.0.0.0:8000:8000 --rm  --name iris-model-api iris-model-api:dev
