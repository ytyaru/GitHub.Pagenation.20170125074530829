from github import GitHub
import json

username = "github_username"
db_path_account = "C:/GitHub.Accounts.sqlite3"
db_path_api = "C:/GitHub.Apis.sqlite3"

g = GitHub.GitHub(db_path_account, db_path_api, username)
res = g.repo.list(type='all', sort='created', direction='asc', per_page=100)

with open('GiHubApi.Repositories.{0}.json'.format(res[0]['owner']['login']), 'w') as f:
    f.write(json.dumps(res))
print(len(res))
