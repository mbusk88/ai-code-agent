import os
from github_handler import GitHubHandler

def main():
    issue_number = int(os.getenv('ISSUE_NUMBER', '1'))
    repo_name = os.getenv('GITHUB_REPOSITORY')
    
    handler = GitHubHandler()
    issue = handler.get_issue(repo_name, issue_number)
    
    print(f"Processing issue #{issue.number}: {issue.title}")
    print(f"Description: {issue.body}")
    
    # TODO: Her skal Gemini CLI kaldes senere

if __name__ == "__main__":
    main()