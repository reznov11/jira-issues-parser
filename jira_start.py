from jira_module import JiraTest
from config.settings import CONFIG as config
from config.settings import MAIN_URL, SEARCH_URL


jira_test = JiraTest(
  domain=MAIN_URL,
  search_url=SEARCH_URL,
  config=config
)
jira_test.start()
