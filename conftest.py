import pytest
from helpers.app import Application


@pytest.fixture
def app(request):
    baseurl = request.config.getoption('--baseUrl')
    api_version = request.config.getoption('--apiVersion')
    api_token = request.config.getoption('--apiToken')
    fixture = Application(baseurl=baseurl, api_version=api_version, api_token=api_token)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--baseUrl', action='store', default='https://api.getbase.com')
    parser.addoption('--apiVersion', action='store', default='/v2')
    parser.addoption('--apiToken', action='store', default='')

