import os


DOMAIN = os.environ.get('JIRA_DOMAIN', "jira-tt-123")
MAIN_URL = f"https://{DOMAIN}.atlassian.net"
SEARCH_URL = f"{MAIN_URL}/rest/api/3/search"

CONFIG = {
  'auth_params': (
    os.environ.get(
      'JIRA_EMAIL', "reznov110@gmail.com"
    ),
    os.environ.get(
      'JIRA_TOKEN', "aHU68ZWnWWXjoA07OXcND918"
    )
  ),
  'proxy': { 
    "http"  : os.environ.get('JIRA_HTTP_PROXY', ''),
    "https" : os.environ.get('JIRA_HTTPS_PROXY', '')
  },
  'headers': {
    "Accept": "application/json",
    "Content-Type": "application/json"
  },
  'query': {
    'jql': f'project = {os.environ.get("JIRA_PROJECT_KEY", "MYB")}'
  }
}
