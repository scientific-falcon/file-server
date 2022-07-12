<div align="center">
    <img src="docs/assets/Logo.png" height="100px">
    <h1>Fastapi file server</h1>
    <p>File storage with web view</p>
    <a href="https://github.com/segmentation-error-cpp/python-template/actions/workflows/pdoc.yml">
        <img src="https://github.com/segmentation-error-cpp/python-template/actions/workflows/pdoc.yml/badge.svg">
    </a>
    <a href="https://github.com/segmentation-error-cpp/python-template/actions/workflows/test_ci.yml">
        <img src="https://github.com/segmentation-error-cpp/python-template/actions/workflows/test_ci.yml/badge.svg">
    </a>
    <a href="https://github.com/segmentation-error-cpp/python-template/actions/workflows/lint.yml">
        <img src="https://github.com/segmentation-error-cpp/python-template/actions/workflows/lint.yml/badge.svg">
    </a>
</div>

## Table of content
- [Table of content](#table-of-content)
- [Requirements](#requirements)
- [Description](#description)
  - [Architecture](#architecture)
  - [Packages](#packages)
  - [Lang requirements](#lang-requirements)
- [Deployment](#deployment)

## Requirements

| name   | version | description                      |
| ------ | ------- | -------------------------------- |
| Python | 3.9.0   | Main implementation language     |

## Description
File-server is a Python package wich implements file-server as part of some server. It designed
to be as much extendable and usable as it is possible. By default, runs as standalone self-hosted
server, without web client, but running `prod_view` will create a SSR model of working with all
files, hosted by the server. Authentification is included, based on sessions.

### Architecture
Package uses state machine pattern inside, which makes it easiear to handle some specific features
like file compressing, reloading and so on.

### Packages
See release in github

### Lang requirements

| Name              | Version | Description                     | Requirements |
| ----------------- | ------- | ------------------------------- | ------------ |
| Pipenv            | Any     | Package manager                 | 🟩           |

## Deployment
1. As self hosted
   1. Enter the folder from terminal
   2. Run `pipenv install`
   3. For web view `pipenv run prod_view`, without `pipenv run prod`
