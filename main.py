import github
from datetime import datetime

issues = github.get_issues()


def get_subject(issue: object):
    labels = issue['labels']
    for label in labels:
        if label['name'].startswith('과목-'):
            return label['name'][3:]

    return None


def get_study_time(issue: object):
    comments = github.get_comments(issue['number'])
    for comment in comments:
        if comment['body'].startswith('공부시간-'):
            return int(comment['body'][5:])

    return 0


def is_study_completed(issue: object):
    labels = issue['labels']
    for label in labels:
        if label['name'] == '완료':
            return True

    return False


total_study_time: int = 0

for issue in issues:
    study_time = get_study_time(issue)
    total_study_time = total_study_time + study_time

    print('---------------------')
    print('제목: {title}'.format(title=issue['title']))
    print('내용: {body}'.format(body=issue['body']))
    print('공부 과목: {subject}'.format(subject=get_subject(issue)))
    print('공부 시간: {time}'.format(time=study_time))
    print('공부 완료: {state}'.format(state=is_study_completed(issue)))
    print('---------------------')
    print()

print('[공부 요약]')
print('날짜: {date}'.format(date=datetime.today().strftime('%Y년 %m월 %d일')))
print('총 공부 시간: {time}'.format(time=total_study_time))
