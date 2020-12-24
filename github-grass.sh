#!/bin/bash

./src/get-github-grass.sh $1 | python3 ./src/echo-github-grass.py
