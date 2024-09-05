'''Helps in scheduling tasks or events based on dependencies.
Detects cycles in a directed graph.
Efficient for solving problems with precedence constraints.
Time complexcity is O(V+E)
'''

from collections import deque

def topological_E_DFS(sub:str, subgraph:dict, stack:list, visited:list):
    if sub not in visited:
        visited.append(sub)
        for linkSub in subgraph[sub]:
            if linkSub not in visited:
                topological_E_DFS(linkSub, subgraph, stack, visited)
        stack.append(sub)

def topological_E_DFS_U(sub):
    '''Go through the node and reach the root node. Since no more connection, then it is of no pre-requisite and add to the stack. The before node will now check for any pre-require if not then add this node to the stack'''
    stack = []
    visited = []
    for v in V:
        topological_E_DFS(v, sub, stack, visited)
    print(f"DFS - {stack}")

def topological_E_BFS(sub:dict):
    ''' Have a degree for each vertices so know if it has any pre-requisite. If no pre-requsite add to stack and then remove that node from the list'''
    vtxDeg = {}
    q = deque()
    stack = []

    for key, val in sub.items():
        vtxDeg[key] = len(val)
        if not vtxDeg[key]:
            q.append(key)

    while q:
        node = q.popleft()
        stack.append(node)

        for s, ls in sub.items():
            if node in ls:
                vtxDeg[s] -= 1
                if not vtxDeg[s]:
                    q.append(s)
    
    print(f"BFS - {stack}")

def edgeList(V, E):
    sub = {}
    for v in V:
        sub[v] = []

    for s1, s2 in E:
        sub[s2].append(s1)
    
    topological_E_DFS_U(sub)
    topological_E_BFS(sub)

if __name__ == "__main__":
    V = ['AdvPro', 'ProFun', 'Algo', 'ML', 'DeepLearn', 'BigData', 'Useablity', 'APD', 'Data mining', 'DB']
    E = [('ProFun','AdvPro'), ('ProFun','Algo'), ('DB', 'BigData'), ('ProFun', 'Data mining'), ('Algo', 'ML'), ('ML', 'DeepLearn'), ('DB', 'DeepLearn')]

    edgeList(V,E)
