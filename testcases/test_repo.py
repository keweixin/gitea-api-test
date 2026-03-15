import pytest

from common.config import Config
from utils.random_util import build_repo_name
from utils.yaml_util import load_yaml_cases


CREATE_REPO_CASES = load_yaml_cases("data/repo.yaml", "create_repo_cases")


def build_repo_name_by_type(name_type):
    if name_type == "random":
        return build_repo_name()
    if name_type == "empty":
        return ""
    if name_type == "duplicate":
        return Config.REPO_NAME_BASE
    return build_repo_name()


@pytest.mark.repo
@pytest.mark.parametrize(
    "case",
    CREATE_REPO_CASES,
    ids=[case["title"] for case in CREATE_REPO_CASES],
)
def test_create_repo_data_driven(repo_api, case):
    repo_name = build_repo_name_by_type(case["name_type"])

    response = repo_api.create_repo(
        name=repo_name,
        description=case["description"],
        private=case["private"],
    )

    assert response.status_code == case["expected_status"], response.text

    if case["name_type"] == "random":
        data = response.json()
        assert data["name"] == repo_name
        assert data["owner"]["login"] == Config.OWNER

        cleanup_response = repo_api.delete_repo(Config.OWNER, repo_name)
        assert cleanup_response.status_code in [200, 204, 404], cleanup_response.text


@pytest.mark.repo
@pytest.mark.smoke
def test_get_repo_detail_success(repo_api, created_repo):
    response = repo_api.get_repo(Config.OWNER, created_repo)

    assert response.status_code == 200, response.text

    data = response.json()
    assert data["name"] == created_repo
    assert data["owner"]["login"] == Config.OWNER


@pytest.mark.repo
def test_update_repo_success(repo_api, created_repo):
    new_description = "updated by pytest"

    response = repo_api.update_repo(
        Config.OWNER,
        created_repo,
        {"description": new_description},
    )

    assert response.status_code == 200, response.text

    data = response.json()
    assert data["description"] == new_description


@pytest.mark.repo
def test_delete_repo_success(repo_api, created_repo):
    response = repo_api.delete_repo(Config.OWNER, created_repo)

    assert response.status_code in [200, 204], response.text

    check_response = repo_api.get_repo(Config.OWNER, created_repo)
    assert check_response.status_code == 404, check_response.text


@pytest.mark.repo
def test_get_repo_languages_success(repo_api, created_repo):
    response = repo_api.get_repo_languages(Config.OWNER, created_repo)

    assert response.status_code == 200, response.text
    assert isinstance(response.json(), dict)


@pytest.mark.repo
def test_get_collaborators_success(repo_api, created_repo):
    response = repo_api.get_collaborators(Config.OWNER, created_repo)

    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)


@pytest.mark.db
@pytest.mark.repo
def test_create_repo_and_check_db_success(repo_api, temp_repo_name, db):
    description = "created by pytest db check"

    response = repo_api.create_repo(
        name=temp_repo_name,
        description=description,
        private=False,
    )

    assert response.status_code in [200, 201], response.text

    row = db.query_one(
        """
        SELECT owner_name, name, description, is_private
        FROM repository
        WHERE owner_name = %s AND name = %s
        """,
        (Config.OWNER, temp_repo_name),
    )

    assert row is not None, "Repository record not found in database"
    assert row["owner_name"] == Config.OWNER
    assert row["name"] == temp_repo_name
    assert row["description"] == description
    assert row["is_private"] == 0

    cleanup_response = repo_api.delete_repo(Config.OWNER, temp_repo_name)
    assert cleanup_response.status_code in [200, 204, 404], cleanup_response.text
