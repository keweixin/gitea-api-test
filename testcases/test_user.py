import pytest

from api.user_api import UserApi
from common.config import Config
from common.request_handler import RequestHandler
from utils.yaml_util import load_yaml_cases


AUTH_CASES = load_yaml_cases("data/auth.yaml", "get_current_user_cases")


def build_headers_by_type(headers_type):
    if headers_type == "valid":
        return Config.auth_headers()
    if headers_type == "none":
        return {}
    if headers_type == "invalid":
        return {
            "Authorization": "token fake-token",
            "Content-Type": "application/json",
        }
    return {}


def build_public_username():
    return Config.PUBLIC_USER or Config.OWNER


@pytest.mark.auth
@pytest.mark.smoke
def test_get_current_user_smoke_success():
    user_api = UserApi()
    response = user_api.get_current_user()

    assert response.status_code == 200, response.text

    data = response.json()
    assert "login" in data
    assert data["login"] != ""


@pytest.mark.auth
def test_get_current_user_repos_success():
    user_api = UserApi()
    response = user_api.get_current_user_repos()

    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)


@pytest.mark.auth
def test_get_public_user_success():
    username = build_public_username()
    user_api = UserApi()
    response = user_api.get_public_user(username)

    assert response.status_code == 200, response.text

    data = response.json()
    assert data.get("login") == username or data.get("username") == username


@pytest.mark.auth
def test_get_public_user_repos_success():
    username = build_public_username()
    user_api = UserApi()
    response = user_api.get_public_user_repos(username)

    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)


@pytest.mark.auth
@pytest.mark.parametrize("case", AUTH_CASES, ids=[case["title"] for case in AUTH_CASES])
def test_get_current_user_data_driven(case):
    headers = build_headers_by_type(case["headers_type"])
    request_handler = RequestHandler(headers=headers)
    user_api = UserApi(request_handler=request_handler)

    response = user_api.get_current_user()

    assert response.status_code == case["expected_status"], response.text

    if case["expected_status"] == 200:
        data = response.json()
        assert "login" in data

        if case.get("expected_login_not_empty"):
            assert data["login"] != ""
