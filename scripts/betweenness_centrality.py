import matplotlib.pyplot as plt
import operator

def plot_centrality(pathToNodes):
    
    with open(pathToNodes) as nodesFile:
        nodesList = nodesFile.readlines()
    
    #top_betweenness_central_users = ['kevinsawicki', 'amitshekhariitbhu', 'sahat', 'qiwsir', 'zpao', 'alvarotrigo', 'hehonghui', 'yyx990803', 'gavinkwoe', 'robdodson']
    #top_closeness_central_users = ['kevinsawicki', 'zpao', 'alvarotrigo', 'yyx990803', 'gavinkwoe', 'krasimir', 'ljharb', 'robdodson', 'paulcbetts', 'benjamn']
    top_eigenvector_central_users = ['nelsonic', 'mikeal', 'yulingtianxia', 'HenriqJoreteg', 'xinyu198736', 'mschwarzmueller', 'xtaci', 'onevcat', 'phuslu', 'muan']

    langs_dict = {}

    for top_user in top_eigenvector_central_users:

        for instance in nodesList:
        
            node_params = instance.split(',')
            if node_params[0] == top_user:
        
                language = node_params[6].strip('\n')
                if language != 'null':
                    key = langs_dict.get(language)
                    if key is None:
                        langs_dict[language] = 1
                    else:
                        langs_dict[language] += 1

    sorted_langs_dict = sorted(langs_dict.items(), key=operator.itemgetter(1))
    print(sorted_langs_dict)

    plt.bar(range(len(langs_dict)), list(langs_dict.values()), align='center')
    plt.xticks(range(len(langs_dict)), list(langs_dict.keys()))
    plt.show()

plot_centrality('../data/users.csv')