# Who's on what

Do you ever wonder why some people are so difficult to get time from? Well so did I, so I wrote a python script to see what they're working on

## Setup

1. `pip install -r requirements.txt`
2. `cp example.env .env` and then set your baseURL and Jira API token
3. edit `main.py` to update `USERS` to your own list of users

## Running

Running `python main.py` will give you a nice list of who's on what:


```
+-------------------+---------+----------------------+
|        user       |   key   |        ticket        |
+-------------------+---------+----------------------+
| alice@example.com | ABC-123 | writing lots of code |
| alice@example.com | ABC-456 |    creating bugs     |
+-------------------+---------+----------------------+
```
