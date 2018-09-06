import matplotlib.pyplot as plt
import operator

def group_users_by_module(pathToNodes, pathToMods):
    
    with open(pathToMods) as modsFile:
        modsList = modsFile.readlines()

    users_module_1 = [] #36
    users_module_2 = [] #9
    users_module_3 = [] #26
    users_module_4 = [] #19
    users_module_5 = [] #42
    users_module_6 = [] #14
    users_module_7 = [] #23
    
    for instance in modsList:
        node_params = instance.split(',')
        module = node_params[4]
        user = node_params[0]

        if module == '36':
            users_module_1.append(user)
        elif module == '9':
            users_module_2.append(user)
        elif module == '26':
            users_module_3.append(user)
        elif module == '19':
            users_module_4.append(user)
        elif module == '42':
            users_module_5.append(user)
        elif module == '14':
            users_module_6.append(user)
        elif module == '23':
            users_module_7.append(user)
    
    modules_dict_1 = {} #36
    modules_dict_2 = {} #9
    modules_dict_3 = {} #26
    modules_dict_4 = {} #19
    modules_dict_5 = {} #42
    modules_dict_6 = {} #14
    modules_dict_7 = {} #23

    with open(pathToNodes) as nodesFile:
        nodesList = nodesFile.readlines()
    
    for mod1 in users_module_1:
        for instance in nodesList:
            node_params = instance.split(',')

            if node_params[0] == mod1:
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = modules_dict_1.get(language)
                    if key is None:
                        modules_dict_1[language] = 1
                    else:
                        modules_dict_1[language] += 1
    
    for mod2 in users_module_2:
        for instance in nodesList:
            node_params = instance.split(',')

            if node_params[0] == mod2:
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = modules_dict_2.get(language)
                    if key is None:
                        modules_dict_2[language] = 1
                    else:
                        modules_dict_2[language] += 1
    
    for mod3 in users_module_3:
        for instance in nodesList:
            node_params = instance.split(',')

            if node_params[0] == mod3:
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = modules_dict_3.get(language)
                    if key is None:
                        modules_dict_3[language] = 1
                    else:
                        modules_dict_3[language] += 1
    
    for mod4 in users_module_4:
        for instance in nodesList:
            node_params = instance.split(',')

            if node_params[0] == mod4:
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = modules_dict_4.get(language)
                    if key is None:
                        modules_dict_4[language] = 1
                    else:
                        modules_dict_4[language] += 1
    
    for mod5 in users_module_5:
        for instance in nodesList:
            node_params = instance.split(',')

            if node_params[0] == mod5:
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = modules_dict_5.get(language)
                    if key is None:
                        modules_dict_5[language] = 1
                    else:
                        modules_dict_5[language] += 1
    
    for mod6 in users_module_6:
        for instance in nodesList:
            node_params = instance.split(',')

            if node_params[0] == mod6:
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = modules_dict_6.get(language)
                    if key is None:
                        modules_dict_6[language] = 1
                    else:
                        modules_dict_6[language] += 1

    for mod7 in users_module_7:
        for instance in nodesList:
            node_params = instance.split(',')

            if node_params[0] == mod7:
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = modules_dict_7.get(language)
                    if key is None:
                        modules_dict_7[language] = 1
                    else:
                        modules_dict_7[language] += 1




    sorted_modules_dict_1 = sorted(modules_dict_1.items(), key=operator.itemgetter(1))
    print(sorted_modules_dict_1[-15:])
    print('\n')
    sorted_modules_dict_2 = sorted(modules_dict_2.items(), key=operator.itemgetter(1))
    print(sorted_modules_dict_2[-15:])
    print('\n')
    sorted_modules_dict_3 = sorted(modules_dict_3.items(), key=operator.itemgetter(1))
    print(sorted_modules_dict_3[-15:])
    print('\n')
    sorted_modules_dict_4 = sorted(modules_dict_4.items(), key=operator.itemgetter(1))
    print(sorted_modules_dict_4[-15:])
    print('\n')
    sorted_modules_dict_5 = sorted(modules_dict_5.items(), key=operator.itemgetter(1))
    print(sorted_modules_dict_5[-15:])
    print('\n')
    sorted_modules_dict_6 = sorted(modules_dict_6.items(), key=operator.itemgetter(1))
    print(sorted_modules_dict_6[-15:])
    print('\n')
    sorted_modules_dict_7 = sorted(modules_dict_7.items(), key=operator.itemgetter(1))
    print(sorted_modules_dict_7[-15:])


group_users_by_module('../data/users.csv', '../data/users_modularity.csv')