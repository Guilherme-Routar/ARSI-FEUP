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
usersFile = open('../data/users.csv','w')
usersFile.write('user,repository,stars,forks,issues,size,language') 

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
        for repos_id in range(0, len(data)):
            
            # user name
            login = user['login']
            string = login + ','

            # Ignoring useless common repositories
            repos = data[repos_id]['name']
            if repos in ignore_repos:
                break
            string = string + repos + ','
            
            # repository stars
            stars = str(data[repos_id]['stargazers_count'])
            string = string + stars + ','

            # repository forks
            forks = str(data[repos_id]['forks_count'])
            string = string + forks + ','

            # open issues
            open_issues = str(data[repos_id]['open_issues_count'])
            string = string + open_issues + ','

            # repository size
            size = str(data[repos_id]['size'])
            string = string + size + ','

            # repository (main) language
            language = data[repos_id]['language']
            if language is None:
                language = 'null'
            string = string + language

            # Writing to file
            usersFile.write('\n' + string)
 
# Closing file
usersFile.close()