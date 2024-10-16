#!/usr/bin/env bash
set -eo pipefail

COLOR_GREEN=`tput setaf 2;`
COLOR_NC=`tput sgr0;` # No Color

echo "Starting black"
poetry run black .
echo "OK"

echo "Starting isort"
poetry run isort .
echo "OK"

echo "Starting mypy"
poetry run mypy .
echo "OK"

echo "Sort pyproject.toml"
poetry run toml-sort pyproject.toml --all --in-place
echo "OK"

echo "Starting pytest with coverage"
MONGO_DATABASE="food_delivery_app_test" poetry run coverage run -m pytest --asyncio-mode=auto
poetry run coverage report -m
poetry run coverage html

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"
