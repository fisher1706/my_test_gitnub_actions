# Description Automated UI and API tests for project.

# High level project structure:

    .
    ├── data                    # Methods and files for generating various test data
    ├── src                     # Test framework source files with tests implementation
    │   ├── tests               # Test files stored in separate folder for each service
    │   ├── api                 # API tests
    │   └── ui                  # UI tests
    ├── conftest.py             # Pytest related fixtures
    ├── utils                   # Different utils such as logger, assertions, discord manager, etc.
    ├── .env.qa                 # Environment variables for run on qa env
    ├── .gitlab-ci.yml          # Config file for gitlab ci with pipeline for tests repository
    ├── Dockerfile              # DevOps config files
    ├── README.md               # Project description
    └── config.py               # Key config file for the framework


# install and setup virtualenv for the project
```shell
pip install virtualenv
virtualenv --python python3 venv
source venv/bin/activate
```

# install requirements
```shell
pip install -r requirements.txt
```

# run tests with create allure report
```shell
pytest tests/ --alluredir=allure-results
```

# open allure report
```shell
allure serve allure-results
```

# start tests from docker-compose
```shell
docker-compose build && docker-compose up
```

# start mock server
```shell
docker build -t mock-server ./mock_emulator && docker run --name mock-server -p 5000:5000 mock-server
```

# stop and kill mock-server
```shell
docker stop mock-server
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
```

# generate allure-report
```shell
allure generate allure-results --clean -o allure-report
```