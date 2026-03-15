"""
负向测试用例 - 异常场景覆盖
"""

import pytest

from api.issue_api import IssueApi
from api.repo_api import RepoApi
from api.user_api import UserApi
from common.config import Config


class TestNegativeCases:
    """负向测试用例集"""

    @pytest.mark.issue
    def test_delete_issue_nonexistent_repo(self, issue_api):
        """仓库不存在时删 issue -> 404"""
        response = issue_api.update_issue(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
            issue_index=1,
            {"state": "closed"},
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.issue
    def test_get_issue_nonexistent(self, issue_api, created_repo):
        """获取不存在的 issue -> 404"""
        response = issue_api.get_issue_detail(
            Config.OWNER,
            created_repo,
            issue_index=999999,
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.issue
    def test_delete_label_nonexistent(self, issue_api, created_repo):
        """删除不存在的标签 -> 404"""
        response = issue_api.delete_label(
            Config.OWNER,
            created_repo,
            label_id=999999,
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.repo
    def test_get_repo_nonexistent(self, repo_api):
        """获取不存在的仓库 -> 404"""
        response = repo_api.get_repo(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.repo
    def test_delete_repo_nonexistent(self, repo_api):
        """删除不存在的仓库 -> 404"""
        response = repo_api.delete_repo(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.user
    def test_get_public_user_nonexistent(self):
        """获取不存在的用户 -> 404"""
        user_api = UserApi()
        response = user_api.get_public_user("nonexistent_user_12345")
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.issue
    def test_create_issue_invalid_page_params(self, issue_api, created_repo):
        """非法参数格式（负数页码）-> 422 或其他错误"""
        response = issue_api.get_issue_list(
            owner=Config.OWNER,
            repo=created_repo,
            page=-1,
        )
        # 负数页码应该返回错误或被忽略
        assert response.status_code in [200, 400, 422], f"Unexpected status: {response.status_code}"

    @pytest.mark.repo
    def test_update_repo_nonexistent(self, repo_api):
        """更新不存在的仓库 -> 404"""
        response = repo_api.update_repo(
            owner="nonexistent_owner_12345",
            repo="nonexistent_repo_12345",
            data={"description": "test"},
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    @pytest.mark.repo
    def test_create_repo_invalid_private_type(self, repo_api):
        """创建仓库时 private 字段传非法值 -> 422"""
        response = repo_api.create_repo(
            name=f"test-repo-invalid-{Config.REPO_NAME_TEMP}",
            description="test",
            private="invalid_string",  # 应该传 bool
        )
        assert response.status_code in [400, 422], f"Expected 400/422, got {response.status_code}"

    @pytest.mark.issue
    def test_add_labels_to_nonexistent_issue(self, issue_api, created_repo):
        """给不存在的 issue 添加标签 -> 404"""
        response = issue_api.add_issue_labels(
            owner=Config.OWNER,
            repo=created_repo,
            issue_index=999999,
            data={"labels": [1]},
        )
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
