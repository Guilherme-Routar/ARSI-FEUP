def createEdges(pathToNodes, pathToEdges):

    edgesFile = open(pathToEdges, 'w')
    with open(pathToNodes) as usersFile:
        usersList = usersFile.readlines()

    # Checking, for each user, other users who contributed to the same project(s)
    iteration = 1
    for instance in usersList:
        user = instance.split(',')
        auxList = usersList[iteration:len(usersList)]

        # Iterating sublist of users
        for instance_aux in auxList:
            user2 = instance_aux.split(',')
            if user[0] != user2[0] and user[1] == user2[1]:
                edgesFile.write(user[0] + ',' + user2[0] + ',' + user[1])

        iteration += 1

    edgesFile.close() # Finished writing 


createEdges(
    '../data/users_by_followers_half.csv',
    '../data/edges_followers_half.csv'
)