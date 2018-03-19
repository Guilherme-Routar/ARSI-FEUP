import requests, json
from setAuth import export

# Setting credentials for a higher API request limit
credentials = export()
GITHUB_LOGIN = credentials[0]
GITHUB_PASS = credentials[1]

# API paths
mainPath = 'https://api.github.com/search/users?q=followers:>100&page='
userPath = 'https://api.github.com/users/'

# Initializing users file
usersFile = open('../data/users_by_followers_v2.csv','w')
usersFile.write('user,repository') 

for page in range(0,50):

    # List of users
    users_raw = requests.get(mainPath + str(page), auth=(GITHUB_LOGIN, GITHUB_PASS))
    users = users_raw.json()

    # Contributions (repositories) per user
    for user in users['items']:
        data_raw = requests.get(userPath + user['login']  + '/repos', auth=(GITHUB_LOGIN, GITHUB_PASS))
        data = data_raw.json()
        
        # Storing repository name and stars count in a hashmap 
        repos_hash = []
        for repos in range(0,len(data)):
            repos_hash.append([
                data[repos]['stargazers_count'],
                data[repos]['name']
            ])

        # Get the 10 (or max) most popular repositories per user        
        repos_hash.sort()
        if len(repos_hash) >= 10:
            max = -11
        else:
            max = -len(repos_hash)
        for index in range(-1,max,-1):
            usersFile.write('\n' + user['login'] + ',' + data[index]['name'])


usersFile.close()