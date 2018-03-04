# Reading users file and writing to edges file
usersFile = open('users.csv','r')
edgesFile = open('edges.csv','w')

with open('users.csv') as usersFile:
    usersList = usersFile.readlines() # Closes automatically

iteration = 1
for instance in usersList:
    user = instance.split(',')
    auxList = usersList[iteration:len(usersList)]
    for instance_aux in auxList:
        aux = instance_aux.split(',')
        if user[0] != aux[0] and user[1] == aux[1]:
            edgesFile.write(user[0] + ',' + aux[0] + ',' + user[1])
    iteration += 1

edgesFile.close() # Finished writing 