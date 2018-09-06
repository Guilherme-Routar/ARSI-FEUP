class Edge:
    
    # Initializing edge
    def __init__(self, source, target, repository, stars, forks, issues, size, language):
        # source and target nodes
        self.source = source
        self.target = target
        # repositories
        self.repositories = []
        self.repositories.append(repository)
        # stars (weight)
        self.weight = int(stars)
        # other parameteres
        self.forks = int(forks)
        self.issues = int(issues)
        self.size = int(size)
        # languages
        self.languages = []
        self.languages.append(language)
    

    # Updating edge's repositories and weight
    def update_edge(self, repository, stars, forks, issues, size, language):
        self.repositories.append(repository)
        self.weight += int(stars)
        self.forks += int(forks)
        self.issues += int(issues)
        self.size += int(size)
        if language not in self.languages:
            self.languages.append(language)


# Function to create network edges
def launch_edges(pathToNodes, pathToEdges):

    # Initializing edges file
    edgesFile = open(pathToEdges, 'w')
    edgesFile.write('source,target,repository,weight,forks,issues,size,languages') 

    # Reading users file
    with open(pathToNodes) as usersFile:
        usersList = usersFile.readlines()

    # Lists to store edges id and edge objects
    edges_ids = []
    edges = []

    # Checking, for each user, other users who contributed to the same project(s)
    iteration = 1
    for instance in usersList:

        # source node
        source = instance.split(',')
        # target nodes list
        auxList = usersList[iteration:len(usersList)]
        
        # Iterating sublist of users (targets)
        for instance_aux in auxList:
            
            # target node
            target = instance_aux.split(',')
            # source node settings
            source_username = source[0]
            source_repository = source[1]
            # target node settings
            target_username = target[0]
            target_repository = target[1]
            # common repository stars
            repository_stars = source[2]
            # Edge weight can't be 0
            if repository_stars == '0':
                repository_stars = '1'
            # repository forks
            repository_forks = source[3]
            # repository issues
            repository_issues = source[4]
            # repository size 
            repository_size = source[5]
            # repository language
            repository_language = source[6].strip('\n')

            # Making sure source and target aren't the same user
            if source_username != target_username and source_repository == target_repository:
                # Creating edge id
                edge_id = source[0] + target[0]
                # Checking if edge exits already
                if edge_id not in edges_ids:
                    # Add it to the edges_ids list
                    edges_ids.append(source_username + target_username)
                    # If not, create new edge (source, target, repository, stars)
                    edge = Edge(source_username, target_username, source_repository, repository_stars, repository_forks, repository_issues, repository_size, repository_language)
                    # Add it to the edges list (so we can write it to the file later)
                    edges.append(edge)
                # Edge has already been created, we need to update it
                else:
                    for edge in edges:
                        # Finding edge in the list
                        if edge.source == source_username and edge.target == target_username:
                            # Updating edge repositories and weight
                            edge.update_edge(source_repository, repository_stars, repository_forks, repository_issues, repository_size, repository_language)

        iteration += 1
    
    # Writing edges to file
    i = 1
    for edge in edges:
        repos_list_aux = ','.join(edge.repositories)
        repos_list = repos_list_aux
        langs_list_aux = ','.join(edge.languages)
        langs_list = langs_list_aux
        edgesFile.write('\n' + edge.source + "," + edge.target + "," + '"' + repos_list + '"' + "," + str(edge.weight) + ',' + str(edge.forks) + ',' + str(edge.issues) + ',' + str(edge.size) + ',' + '"' + langs_list+ '"')

    # Finished writing 
    edgesFile.close()

launch_edges(
    '../data/users.csv',
    '../data/edges.csv'
)