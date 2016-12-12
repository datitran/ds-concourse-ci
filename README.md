# Data Science Continuous Integration (CI)

A simple example to test python scripts with [Concourse](https://concourse.ci/) which can be used as a skeleton for data science projects that are deployed via [Cloud Foundry](https://www.cloudfoundry.org/).

## Getting Started

#### Folder Structure
- Things that are created/needed during the exploratory phase should be put in `exploration/`
- Put production-ready code into `src/`

#### Concourse CI
1. Setup the CI with [docker](https://concourse.ci/docker-repository.html) and spin it up via `docker-compose up`
2. Connect to the CI: `fly -t example-ci login -c http://127.0.0.1:8080`
3. Fill in the credential details in `credentials.yml.example` and rename the file to `credentials.yml`
4. Register the pipeline: `fly -t example-ci set-pipeline -p data-science-ci -c pipeline.yml -l credentials.yml`
5. Unpause the pipeline: `fly -t example-ci unpause-pipeline -p data-science-ci`

## Dependencies
- [Anaconda](https://www.continuum.io/downloads) Python 3.5.2
- [Concourse](http://concourse.ci/index.html)
- [Docker](https://www.docker.com/)

## To-Do
- Add example for customized dockerfile which is used as a test container
- Combine the container with Anaconda Cloud i.e. automatically get the `environment.yml` file and include this in the container

## Copyright

See [LICENSE](LICENSE) for details.
Copyright (c) 2016 [Dat Tran](http://www.dat-tran.com/).