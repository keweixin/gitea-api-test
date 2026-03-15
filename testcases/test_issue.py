import pytest

from common.config import Config
from utils.random_util import build_repo_name
from utils.yaml_util import load_yaml_cases


CREATE_ISSUE_CASES = load_yaml_cases("data/issue.yaml", "create_issue_cases")


def build_issue_title_by_type(issue_title_type):
    if issue_title_type == "random":
        return f"issue-{build_repo_name('title')}"
    if issue_title_type == "empty":
        return ""
    return f"issue-{build_repo_name('title')}"


@pytest.mark.issue
@pytest.mark.parametrize(
    "case",
    CREATE_ISSUE_CASES,
    ids=[case["title"] for case in CREATE_ISSUE_CASES],
)
def test_create_issue_data_driven(issue_api, case):
    issue_title = build_issue_title_by_type(case["issue_title_type"])

    response = issue_api.create_issue(
        owner=Config.OWNER,
        repo=Config.REPO_NAME_BASE,
        title=issue_title,
        body=case["body"],
    )

    assert response.status_code == case["expected_status"], response.text

    if case["issue_title_type"] == "random":
        data = response.json()
        assert data["title"] == issue_title
        assert data["state"] == "open"


@pytest.mark.issue
def test_get_issue_list_success(issue_api):
    response = issue_api.get_issue_list(Config.OWNER, Config.REPO_NAME_BASE)

    assert response.status_code in [200, 201], response.text
    assert isinstance(response.json(), list)


@pytest.mark.issue
def test_get_issue_detail_success(issue_api, created_issue):
    response = issue_api.get_issue_detail(
        Config.OWNER,
        Config.REPO_NAME_BASE,
        created_issue,
    )

    assert response.status_code in [200, 201], response.text

    data = response.json()
    assert data["number"] == created_issue or data["index"] == created_issue


@pytest.mark.issue
def test_get_repo_labels_success(issue_api, created_repo):
    response = issue_api.get_labels(Config.OWNER, created_repo)

    assert response.status_code == 200, response.text
    assert isinstance(response.json(), list)


@pytest.mark.issue
@pytest.mark.smoke
def test_close_issue_success(issue_api, created_issue):
    response = issue_api.update_issue(
        Config.OWNER,
        Config.REPO_NAME_BASE,
        created_issue,
        {"state": "closed"},
    )

    assert response.status_code in [200, 201], response.text

    data = response.json()
    assert data["state"] == "closed"
    assert data["closed_at"] is not None


@pytest.mark.issue
def test_issue_label_lifecycle_success(issue_api, created_repo):
    label_name = f"label-{build_repo_name('tag')}"

    create_label_response = issue_api.create_label(
        Config.OWNER,
        created_repo,
        name=label_name,
        color="F29513",
        description="created by pytest",
    )
    assert create_label_response.status_code in [200, 201], create_label_response.text
    label_data = create_label_response.json()
    label_id = label_data["id"]

    get_label_response = issue_api.get_label(Config.OWNER, created_repo, label_id)
    assert get_label_response.status_code == 200, get_label_response.text
    assert get_label_response.json()["name"] == label_name

    issue_response = issue_api.create_issue(
        owner=Config.OWNER,
        repo=created_repo,
        title=f"issue-{build_repo_name('label')}",
        body="issue for label lifecycle",
    )
    assert issue_response.status_code in [200, 201], issue_response.text
    issue_data = issue_response.json()
    issue_index = issue_data.get("number") or issue_data.get("index")

    add_labels_response = issue_api.add_issue_labels(
        Config.OWNER,
        created_repo,
        issue_index,
        {"labels": [label_id]},
    )
    assert add_labels_response.status_code in [200, 201], add_labels_response.text
    add_data = add_labels_response.json()
    assert any(label["id"] == label_id for label in add_data)

    get_issue_labels_response = issue_api.get_issue_labels(Config.OWNER, created_repo, issue_index)
    assert get_issue_labels_response.status_code == 200, get_issue_labels_response.text
    assert any(label["id"] == label_id for label in get_issue_labels_response.json())

    replace_labels_response = issue_api.replace_issue_labels(
        Config.OWNER,
        created_repo,
        issue_index,
        [label_id],
    )
    assert replace_labels_response.status_code == 200, replace_labels_response.text

    clear_labels_response = issue_api.clear_issue_labels(Config.OWNER, created_repo, issue_index)
    assert clear_labels_response.status_code in [200, 204], clear_labels_response.text

    labels_after_clear_response = issue_api.get_issue_labels(Config.OWNER, created_repo, issue_index)
    assert labels_after_clear_response.status_code == 200, labels_after_clear_response.text
    assert labels_after_clear_response.json() == []

    delete_label_response = issue_api.delete_label(Config.OWNER, created_repo, label_id)
    assert delete_label_response.status_code in [200, 204], delete_label_response.text


@pytest.mark.db
@pytest.mark.issue
def test_close_issue_and_check_db_success(issue_api, created_issue, db):
    response = issue_api.update_issue(
        Config.OWNER,
        Config.REPO_NAME_BASE,
        created_issue,
        {"state": "closed"},
    )

    assert response.status_code in [200, 201], response.text

    row = db.query_one(
        """
        SELECT i.`index`, i.is_closed, i.closed_unix, r.name AS repo_name
        FROM issue i
        JOIN repository r ON i.repo_id = r.id
        WHERE r.owner_name = %s AND r.name = %s AND i.`index` = %s
        """,
        (Config.OWNER, Config.REPO_NAME_BASE, created_issue),
    )

    assert row is not None, "Issue record not found in database"
    assert row["repo_name"] == Config.REPO_NAME_BASE
    assert row["index"] == created_issue
    assert row["is_closed"] == 1
    assert row["closed_unix"] > 0
