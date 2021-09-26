import os


DOMAIN = os.environ.get('JIRA_DOMAIN', "jira-tt-123")
MAIN_URL = f"https://{DOMAIN}.atlassian.net"
SEARCH_URL = f"{MAIN_URL}/rest/api/3/search"

CONFIG = {
  "key_file": os.environ.get('PVT_FILE', "jira_privatekey.pcks8"),
  "access_token": os.environ.get('ACCESS_TOKEN', "hqZXIowUGG5UOSW1EEjJc5kooDP8XJYe"),
  "secret_token": os.environ.get('SECRET_TOKEN', "HBGpmwwr2RlVUuw3vNUFHTISzMLMtEcm"),
  "consumer_key": f'{os.environ.get("JIRA_CON_KEY", "OauthKey")}',
  "project_key": f'{os.environ.get("JIRA_PROJECT_KEY", "MYB")}',
}
