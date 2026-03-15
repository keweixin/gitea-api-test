import pytest
from common.mysql_helper import MySQLHelper

from api.issue_api import IssueApi
from api.repo_api import RepoApi
from common.config import Config
from utils.random_util import build_repo_name



@pytest.fixture
def repo_api():
    return RepoApi()


@pytest.fixture
def temp_repo_name():
    return build_repo_name()


@pytest.fixture
def created_repo(repo_api):
    repo_name = build_repo_name()

    response = repo_api.create_repo(
        name=repo_name,
        description="created by pytest",
        private=False,
    )
    assert response.status_code in [200, 201], f"Create repo failed: {response.text}"

    yield repo_name

    cleanup_response = repo_api.delete_repo(Config.OWNER, repo_name)
    assert cleanup_response.status_code in [200, 204, 404], (
        f"Cleanup repo failed: {cleanup_response.text}"
    )


@pytest.fixture
def issue_api():
    return IssueApi()


@pytest.fixture
def created_issue(issue_api):
    response = issue_api.create_issue(
        owner=Config.OWNER,
        repo=Config.REPO_NAME_BASE,
        title="issue created by pytest",
        body="issue body from pytest",
    )
    assert response.status_code in [200, 201], f"Create issue failed: {response.text}"

    data = response.json()
    issue_index = data.get("number") or data.get("index")
    assert issue_index, f"Issue index not found: {response.text}"

    return issue_index
@pytest.fixture
def db():
    helper = MySQLHelper()
    yield helper
    helper.close()

