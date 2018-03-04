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
usersFile = open('users.csv','w')
usersFile.write('user,repository') 

for page in range(0,50):

    # List of users
    users_raw = requests.get(mainPath + str(page), auth=(GITHUB_LOGIN, GITHUB_PASS))
    users = users_raw.json()

    # Contributions (repositories) per user
    for user in users['items']:
        data_raw = requests.get(userPath + user['login']  + '/repos', auth=(GITHUB_LOGIN, GITHUB_PASS))
        data = data_raw.json()
        
        # Writing each contribution per user to the file
        for repos in range(0,len(data)):
            usersFile.write('\n' + user['login'] + ',' + data[repos]['name'])

usersFile.close()