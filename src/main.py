import os
from gemini_runner import run_agent_workflow

def main():
    issue_number = os.getenv('ISSUE_NUMBER')
    issue_title = os.getenv('ISSUE_TITLE')
    issue_body = os.getenv('ISSUE_BODY')
    repo_name = os.getenv('GITHUB_REPOSITORY')

    if not all([issue_number, issue_title, issue_body, repo_name]):
        print("Missing required environment variables.")
        return

    print(f"Processing issue #{issue_number}: {issue_title} in {repo_name}")

    success = run_agent_workflow(issue_title, issue_body)

    if success:
        print("Agent workflow completed successfully.")
    else:
        print("Agent workflow failed.")

if __name__ == "__main__":
    main()
