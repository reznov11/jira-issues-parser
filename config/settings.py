import os


DOMAIN = os.environ.get('JIRA_DOMAIN', "jira-tt-123")
MAIN_URL = f"https://{DOMAIN}.atlassian.net"
SEARCH_URL = f"{MAIN_URL}/rest/api/3/search"

CONFIG = {
  "key_file": os.environ.get('PVT_FILE', "jira_privatekey.pcks8"),
  "access_token": os.environ.get('ACCESS_TOKEN', "Mq2mmRgcQrzechQJNtEuiQHc181fNFQf"),
  "secret_token": os.environ.get('SECRET_TOKEN', "3yKd2IJz400oGMb8zeR2FkmR7yF1cEX5"),
  "consumer_key": f'{os.environ.get("JIRA_CON_KEY", "OauthKey")}',
  "project_key": f'{os.environ.get("JIRA_PROJECT_KEY", "MYB")}',
}
