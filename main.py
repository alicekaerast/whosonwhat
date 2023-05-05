from dotenv import dotenv_values
from jira import JIRA
from prettytable import PrettyTable

USERS = [
    "alice@example.com"
]


config = dotenv_values(".env")

jac = JIRA(config['baseUrl'], token_auth=(config['password']))

tab = PrettyTable(["user", "key", "ticket"])
for user in USERS:
    for issue in jac.search_issues(f"assignee = '{user}' AND statusCategory = 'In Progress'"):
        tab.add_row([user, issue.key, issue.fields.summary])

print(tab)
