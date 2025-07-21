import os
from github_handler import GitHubHandler

handler = GitHubHandler()

repo_name = os.getenv('GITHUB_REPOSITORY', 'mbusk88/ai-code-agent')

issue_number = 1  # Vi fikser dette senere

try:
    issue = handler.get_issue(repo_name, issue_number)
    print(f"Issue #{issue.number}: {issue.title}")
    print(f"Beskrivelse: {issue.body}")
    print(f"Labels: {[label.name for label in issue.labels]}")
except Exception as e:
    print(f"Fejl: {e}")