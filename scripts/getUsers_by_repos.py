import requests, json
from setAuth import export

# Setting credentials for a higher API request limit
credentials = export()
GITHUB_LOGIN = credentials[0]
GITHUB_PASS = credentials[1]

# API paths
mainPath = 'https://api.github.com/repos/'
subPath = '/contributors?page='
repositories = ['twbs/bootstrap', 'tensorflow/tensorflow', 'facebook/react', 'vuejs/vue', 'airbnb/javascript', 'angular/angular.js']

userPath = 'https://api.github.com/users/'

# Initializing users file
usersFile = open('../data/users_by_repos.csv','w')
usersFile.write('user,repository')

for repos in repositories:

    for page in range(1,7): # 7 * 30 = 210 users per repository
        url = mainPath + repos + subPath + str(page)
        print(url)
        users_raw = requests.get(url, auth=(GITHUB_LOGIN, GITHUB_PASS))
        users = users_raw.json()

        # Contributions (repositories) per user
        for user in users:
            data_raw = requests.get(userPath + user['login']  + '/repos', auth=(GITHUB_LOGIN, GITHUB_PASS))
            data = data_raw.json()
        
            # Writing each contribution per user to the file
            for repos2 in range(0,len(data)):
                usersFile.write('\n' + user['login'] + ',' + data[repos2]['name'])

usersFile.close()