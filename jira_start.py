from jira import JIRA
from jira_module import JiraTest
from config.settings import MAIN_URL
from config.settings import CONFIG as config

key_cert_data = None

with open(config['key_file'], 'r') as key_cert_file:
  key_cert_data = key_cert_file.read()

oauth_dict = {
	'access_token': config['access_token'],
	'access_token_secret': config['secret_token'],
	'consumer_key': config['consumer_key'],
	'key_cert': key_cert_data
}

auth_jira = JIRA(MAIN_URL, oauth=oauth_dict)

jira_test = JiraTest(auth_jira=auth_jira)

# Get issues
jira_test.get_issues()

# issues_list = [
# 	{
# 		'project': {'key': config['project_key']},
# 		'summary': 'Hello Askar!',
# 		'description': 'This is just a test 1',
# 		'issuetype': {'name': 'Bug'},
# 	},
# 	{
# 		'project': {'key': config['project_key']},
# 		'summary': 'Hello Ammar!',
# 		'description': 'This is just a test 2',
# 		'issuetype': {'name': 'Task'},
# 	}
# ]

# Create new issue ticket
# jira_test.create_new_issue(issues_list)
