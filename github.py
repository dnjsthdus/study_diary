import requests
import json


def get_issues():
    url = 'https://api.github.com/repos/dnjsthdus/study_diary/issues'
    response = requests.get(url)

    return json.loads(response.text)
