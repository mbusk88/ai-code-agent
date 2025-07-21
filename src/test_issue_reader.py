from github_handler import GitHubHandler

# Test at læse en issue
handler = GitHubHandler()

# Brug dit eget repository
repo_name = "mbusk88/ai-code-agent"
issue_number = 1  # Ændr til et issue nummer der findes

try:
    issue = handler.get_issue(repo_name, issue_number)
    print(f"Issue #{issue.number}: {issue.title}")
    print(f"Beskrivelse: {issue.body}")
    print(f"Labels: {[label.name for label in issue.labels]}")
except:
    print(f"Kunne ikke finde issue #{issue_number}")
    print("Opret en test issue på GitHub først!")