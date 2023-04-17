#!/bin/sh

set -eu pipefail

echo "Attempting to connect to cicd-postman-tests-api"
until $(nc -zv web 8000); do
    printf '.'
    sleep 5
done
echo "Connected to cicd-postman-tests-api!"

newman run /src/postman-collection.json -e /src/docker.environment.json

exit 0
