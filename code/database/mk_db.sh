#!/bin/sh

docker run --name pgpantech -e POSTGRES_DB=pantech -e POSTGRES_USER=organic_almond_milk -e POSTGRES_PASSWORD=chiaseeds -p "5432:5432" -d postgres
