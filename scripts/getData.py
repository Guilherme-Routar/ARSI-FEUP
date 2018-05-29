import requests, json
from setAuth import export

# API paths
mainPath = 'https://api.github.com/search/users?q=followers:>100&page='
userPath = 'https://api.github.com/users/'

# Setting credentials for a higher API request limit
credentials = export()
GITHUB_LOGIN = credentials[0]
GITHUB_PASS = credentials[1]

# Initializing users file
usersFile = open('../data/users_proj.csv','w')
usersFile.write('user,repository,stars,size,language') 

for page in range(1,40):

    # List of users
    print(mainPath + str(page))
    users_raw = requests.get(mainPath + str(page), auth=(GITHUB_LOGIN, GITHUB_PASS))
    users = users_raw.json()

    # Contributions (repositories) per user
    for user in users['items']:

        # Getting request json
        data_raw = requests.get(userPath + user['login']  + '/repos', auth=(GITHUB_LOGIN, GITHUB_PASS))
        data = data_raw.json()

        # Repositories to be ignored
        ignore_repos = {'docs', 'ama', 'dotfiles', 'blog', 'amas'}
        
        # Writing each contribution per user to the file
        for repos in range(0, len(data)):
            # Ignoring useless common repositories
            repos = data[repos]['name']
            if repos in ignore_repos
                break
            # user name
            login = user['login']
            # repository stars
            stars = str(data[repos]['stargazers_count'])
            # repository size
            size = str(data[repos]['size'])
            # repository (main) language
            language = data[repos]['language']
            if language is None:
                language = 'null'
            # open issues
            open_issues = data[repos]['open_issues_count']
            # Writing to file
            usersFile.write('\n' + login + ',' + repos + ',' + stars + ',' + size + ',' + language)

# Closing file
usersFile.close()