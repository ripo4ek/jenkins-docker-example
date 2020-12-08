#!/bin/bash
docker network create -d bridge app-network
docker run  --network=app-network --name redis -d redis:3.0 
docker run  --network=app-network --name dnmonster -d amouat/dnmonster:1.0
docker run  --network=app-network -p 6565:9090 --name identidock -d ripo4ek/flask-redis-avatar:latest
