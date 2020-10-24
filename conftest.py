
import pytest
from fixture.application import Application
import json
import os.path
import importlib

fixture = None
target = None

@pytest.fixture()
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target")) #путь к файлу
        with open(config_file) as f: #переменная f содержит объект, который указывает на открытый файл
            target = json.load(f)
    if fixture is None or not fixture.is_valid:
        fixture = Application(browser=browser, base_url=target['baseUrl'], login=target['username'],
                              password=target['password']) #создаём фикстуру если она None или не валидная
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(end)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--login", action="store")
    parser.addoption("--password", action="store")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata

