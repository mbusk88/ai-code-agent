from github import Github
from config import GITHUB_TOKEN

# Test om vi kan forbinde til GitHub
g = Github(GITHUB_TOKEN)
user = g.get_user()
print(f"Forbundet som: {user.login}")
print(f"Navn: {user.name}")