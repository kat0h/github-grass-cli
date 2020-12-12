#!/bin/bash

./src/get-github-glass.sh $1 | python3 ./src/echo-github-glass.py
