from github import Github
from config import GITHUB_TOKEN

class GitHubHandler:
    def __init__(self):
        self.g = Github(GITHUB_TOKEN)
    
    def get_repo(self, repo_name):
        return self.g.get_repo(repo_name)
    
    def get_issue(self, repo_name, issue_number):
        repo = self.get_repo(repo_name)
        return repo.get_issue(issue_number)