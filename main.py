import github

issues = github.get_issues()

print('title: {title}'.format(title=issues[0]['title']))
print('body: {body}'.format(body=issues[0]['body']))
