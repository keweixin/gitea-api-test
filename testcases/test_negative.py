"""
Negative test cases for abnormal API scenarios.
"""

import pytest

from api.user_api import UserApi
from common.config import Config


class TestNegativeCases:
    @pytest.mark.issue
    def test_close_issue_nonexistent_repo(self, issue_api):
        response = issue_api.update_issue(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
            index=1,
            data={"state": "closed"},
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.issue
    def test_get_issue_nonexistent(self, issue_api, created_repo):
        response = issue_api.get_issue_detail(
            Config.OWNER,
            created_repo,
            index=999999,
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.issue
    def test_delete_label_nonexistent(self, issue_api, created_repo):
        response = issue_api.delete_label(
            Config.OWNER,
            created_repo,
            label_id=999999,
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.repo
    def test_get_repo_nonexistent(self, repo_api):
        response = repo_api.get_repo(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.repo
    def test_delete_repo_nonexistent(self, repo_api):
        response = repo_api.delete_repo(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.auth
    def test_get_public_user_nonexistent(self):
        user_api = UserApi()
        response = user_api.get_public_user("nonexistent_user_12345")
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.issue
    def test_get_issue_list_invalid_page_params(self, issue_api, created_repo):
        response = issue_api.get_issue_list(
            owner=Config.OWNER,
            repo=created_repo,
            params={"page": -1},
        )
        # Different Gitea versions may return 200/400/422 for invalid page values.
        assert response.status_code in [200, 400, 422], f"Unexpected status: {response.status_code}"

    @pytest.mark.repo
    def test_update_repo_nonexistent(self, repo_api):
        response = repo_api.update_repo(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
            data={"description": "test"},
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.repo
    def test_create_repo_invalid_private_type(self, repo_api):
        response = repo_api.create_repo(
            name=f"test-repo-invalid-{Config.REPO_NAME_TEMP}",
            description="test",
            private="invalid_string",
        )
        assert response.status_code in [400, 422], f"Expected 400/422, got {response.status_code}"

    @pytest.mark.issue
    def test_add_labels_to_nonexistent_issue(self, issue_api, created_repo):
        response = issue_api.add_issue_labels(
            owner=Config.OWNER,
            repo=created_repo,
            index=999999,
            data={"labels": [1]},
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
