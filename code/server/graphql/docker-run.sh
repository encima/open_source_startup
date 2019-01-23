#! /bin/bash
docker run -p 9000:8080 \
       -e HASURA_GRAPHQL_DATABASE_URL=postgres://organic_almond_milk:chiaseeds@localhost:7000/bikehike \
       -e HASURA_GRAPHQL_ENABLE_CONSOLE=true \
       hasura/graphql-engine:v1.0.0-alpha35
