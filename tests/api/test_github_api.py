import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user('fvefvefvdfvr')
    assert user['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert  r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('uugiuhoijopi')
    assert  r['total_count'] == 0

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('u')
    assert  r['total_count'] != 0