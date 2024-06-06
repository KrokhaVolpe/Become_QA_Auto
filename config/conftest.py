import pytest

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None


    def remove(self):
        self.name = ''
        self.second_name = ''


    def create(self):
        self.name = 'Katarina'
        self.second_name = 'Krokhmal'


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()