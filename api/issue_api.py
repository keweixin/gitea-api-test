from common.config import Config
from common.request_handler import RequestHandler


class IssueApi:
    def __init__(self, request_handler=None):
        self.request_handler = request_handler or RequestHandler()
        self.base_url = Config.BASE_URL.rstrip("/")

    def create_issue(self, owner, repo, title, body=""):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        payload = {
            "title": title,
            "body": body,
        }
        return self.request_handler.post(url, json=payload)

    def get_issue_list(self, owner, repo, params=None):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        return self.request_handler.get(url, params=params)

    def get_issue_detail(self, owner, repo, index):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{index}"
        return self.request_handler.get(url)

    def update_issue(self, owner, repo, index, data):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{index}"
        return self.request_handler.patch(url, json=data)

    def get_labels(self, owner, repo):
        url = f"{self.base_url}/repos/{owner}/{repo}/labels"
        return self.request_handler.get(url)

    def create_label(self, owner, repo, name, color="F29513", description=""):
        url = f"{self.base_url}/repos/{owner}/{repo}/labels"
        payload = {
            "name": name,
            "color": color,
            "description": description,
        }
        return self.request_handler.post(url, json=payload)

    def get_label(self, owner, repo, label_id):
        url = f"{self.base_url}/repos/{owner}/{repo}/labels/{label_id}"
        return self.request_handler.get(url)

    def delete_label(self, owner, repo, label_id):
        url = f"{self.base_url}/repos/{owner}/{repo}/labels/{label_id}"
        return self.request_handler.delete(url)

    def add_issue_labels(self, owner, repo, index, data):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{index}/labels"
        return self.request_handler.post(url, json=data)

    def get_issue_labels(self, owner, repo, index):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{index}/labels"
        return self.request_handler.get(url)

    def replace_issue_labels(self, owner, repo, index, labels):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{index}/labels"
        payload = {"labels": labels}
        return self.request_handler.put(url, json=payload)

    def clear_issue_labels(self, owner, repo, index):
        url = f"{self.base_url}/repos/{owner}/{repo}/issues/{index}/labels"
        return self.request_handler.delete(url)
