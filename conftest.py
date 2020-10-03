
import pytest
from fixture.application import Application

fixture = None

@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        fixture = Application() #инициализация фикстуры
    else:
        if not fixture.is_valid():
            fixture = Application()  # инициализация фикстуры
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def end():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(end)
    return fixture