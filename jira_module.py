from types import FunctionType
import dateutil.parser as dtime
from config.settings import CONFIG as config


class JiraTest():
  
  # We can inherit JIRA module into class
  # but for the purpose of simplicity I won't do it

  def __init__(self, auth_jira) -> None:
    self.auth_jira = auth_jira


  def get_issues(self) -> None:

    print("\nGetting tickets...\n")

    issues_size = 100
    issues_initial_index = 0

    while True:
        
      start= issues_initial_index * issues_size
      issues = self.auth_jira.search_issues(f'project={config["project_key"]}', start, issues_size)
      
      if len(issues) == 0:
        break
      
      issues_initial_index += 1
      
      for issue in issues:
        
        created_dtime = self.dtime_formater(issue.fields.created)

        content = f'Ticket number = {issue}\n'
        content += f'Creator = {issue.fields.creator}\n'
        content += f'IssueType = {issue.fields.issuetype.name}\n'
        content += f'Status = {issue.fields.status.name}\n'
        content += f'Summary = {issue.fields.summary}\n'
        content += f'Description = {issue.fields.description}\n'
        content += f'Votes = {issue.fields.votes.votes}\n'
        content += f'Created = {created_dtime.strftime("%d-%m-%Y %H:%M:%S")}\n'
        content += f'========================================\n'

        self.write_to_file(content)
        self.print_content(content)


  def dtime_formater(self, date) -> str:
    return dtime.parse(date)

  def print_content(self, content) -> None:
    print(content)

  
  def write_to_file(self, content) -> None:
    with open('jira_test.txt', 'a') as fi:
      fi.write(content)
      fi.close()

  def create_new_issue(self, data=None) -> FunctionType:
    if not data:
      print('Please, provide ticket data')
      return

    issues = self.auth_jira.create_issues(field_list=data)

    if issues:
      print("Ticket created successfully.")

    return self.get_issues()
