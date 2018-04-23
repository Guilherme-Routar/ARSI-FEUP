import requests, json
from setAuth import export

# Setting credentials for a higher API request limit
credentials = export()
GITHUB_LOGIN = credentials[0]
GITHUB_PASS = credentials[1]

# API paths
mainPath = 'https://api.github.com/repos/'
subPath = '/contributors?page='
repositories = ['twbs/bootstrap', 
                'tensorflow/tensorflow', 
                'facebook/react', 
                'vuejs/vue', 
                'airbnb/javascript', 
                'angular/angular.js',
                'jquery/jquery',
                'nodejs/node']

userPath = 'https://api.github.com/users/'

# Initializing users file
usersFile = open('../data_v2/users_by_repos_v2.csv','w')
usersFile.write('user,repository')

usersFile_reps = open('../data_v2/users_by_repos_v2_dups.csv','w')
usersFile_reps.write('user')

for repos in repositories:

    for page in range(1,5): # 3 * 30 = 90 users per repository
        url = mainPath + repos + subPath + str(page)
        print(url)
        users_raw = requests.get(url, auth=(GITHUB_LOGIN, GITHUB_PASS))
        users = users_raw.json()

        # Contributions (repositories) per user
        for user in users:
            reposArray = repos.split("/")
            usersFile.write('\n' + user['login'] + ',' + reposArray[1])
            usersFile_reps.write('\n' + user['login'])

            data_raw = requests.get(userPath + user['login']  + '/repos', auth=(GITHUB_LOGIN, GITHUB_PASS))
            data = data_raw.json()
            if len(data) > 1:
                if data[0]['name'] != reposArray[1]:
                    usersFile.write('\n' + user['login'] + ',' + data[0]['name'])
                else:
                    usersFile.write('\n' + user['login'] + ',' + data[1]['name'])

usersFile.close()