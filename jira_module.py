import requests
import dateutil.parser as dtime


class JiraTest():

  def __init__(self, domain, search_url, config) -> None:
    self.domain = domain
    self.search_url = search_url
    self.config = config


  def get_issues(self) -> dict:
    # Ечли запрос отправить через прокси 
    # то нужно указать параметры proxy в конфигурации
    response = requests.get(
      self.search_url,
      headers=self.config['headers'],
      params=self.config['query'] ,
      auth=self.config['auth_params'],
      proxies=self.config['proxy']
    )
    data = response.json()
    return data


  def start(self) -> None:

    print("\nВытащим информацию для Вас!!...\n")

    issues_data = self.get_issues()
    issues = issues_data["issues"]

    for idx, issue in enumerate(issues):
      issue_key = issue["key"]
      issue_url =  f"{self.domain}/rest/api/3/issue/{issue_key}"
      response = requests.get(
        issue_url,
        headers=self.config['headers'],
        auth=self.config['auth_params']
      )
      data = response.json()

      print(
        f'ID Проблема ({issue_key}) со статусом ({data["fields"]["status"]["name"]})\n'
      )

      content = f'Ссылка проблемы: {issues[idx]["self"]}\n'
      content += f'Ключ проблемы: {issues[idx]["key"]}\n'
      content += f'Ссылка тип проблемы: {issues[idx]["fields"]["issuetype"]["self"]}\n'
      content += f'Название тип проблемы: {issues[idx]["fields"]["issuetype"]["name"]}\n'
      content += f'Описаие проблемы: {issues[idx]["fields"]["issuetype"]["description"]}\n'
      content += f'Иконка: {issues[idx]["fields"]["issuetype"]["iconUrl"]}\n'
      content += f'Ссылка на проект: {issues[idx]["fields"]["project"]["self"]}\n'
      content += f'Название проекта: {issues[idx]["fields"]["project"]["name"]}\n'
      content += f'Аватарка проекта: {issues[idx]["fields"]["project"]["avatarUrls"]["48x48"]}\n'
      content += f'Резюме проекта: {issues[idx]["fields"]["summary"]}\n'
      content += f'Создатель: {issues[idx]["fields"]["creator"]["displayName"]}\n'
      content += f'Создатель email: {issues[idx]["fields"]["creator"]["emailAddress"]}\n'
      content += f'Создатель аватарка: {issues[idx]["fields"]["creator"]["avatarUrls"]["48x48"]}\n'
      content += f'Ссылка создателя: {issues[idx]["fields"]["creator"]["self"]}\n'
      content += f'Голосов: {issues[idx]["fields"]["votes"]["votes"]}\n'

      created_dtime = issues[idx]["fields"]["created"]
      last_view_dtime = issues[idx]["fields"]["lastViewed"]

      created_dtime_format = self.dtime_formater(created_dtime)
      last_view_dtime_format = self.dtime_formater(last_view_dtime)

      content += f'Создано: {created_dtime_format.strftime("%d-%m-%Y %H:%M:%S")}\n'
      content += f'Последний ревью: {last_view_dtime_format.strftime("%d-%m-%Y %H:%M:%S")}\n'
      content += f'===================================\n\n\n'

      self.write_to_file(content)
      self.print_content(content)


  def dtime_formater(self, date) -> str:
    return dtime.parse(date)

  
  def write_to_file(self, content) -> None:
    with open('jira_test.txt', 'a') as fi:
      fi.write(content)
      fi.close()


  def print_content(self, content) -> None:
    print(content)
