docker-compose exec api flake8 src
docker-compose exec api black src --check
docker-compose exec api isort src --check-only
