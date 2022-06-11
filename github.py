import requests
import json


def get_issues():
    url = 'https://api.github.com/repos/dnjsthdus/study_diary/issues'
    response = requests.get(url)

    return json.loads(response.text)


def get_comments(issue_number: str):
    url = 'https://api.github.com/repos/dnjsthdus/study_diary/issues/{number}/comments'.format(number=issue_number)
    response = requests.get(url)

    return json.loads(response.text)
