def question1(s, t):
    if s is None or t is None or not isinstance(s, str) \
      or not isinstance(t, str):
        return False

    tD = string_dict(t)
    sD = string_dict(s)

    sL = sD.keys()

    # make sure it's even worth going through all the substrings of s first
    for l, v in tD.items():
        if l not in sL or v > sD[l]:
            return False

    # go through substrings of s of length t and see if all characters match
    tLen = len(t)
    for i in range(len(s) - tLen):
        subStrD = string_dict(s[i:i + tLen])
        if subStrD == tD:
            return True

    return False


def string_dict(st):
    stringDict = {}
    for lett in st:
        stringDict.setdefault(lett, 0)
        stringDict[lett] += 1

    return stringDict

print('')
print('Q1')
print question1('uddacity', 'uddd')
# False
print question1('udacity', 'ud')
# True
print question1('udacity', 'du')
# True
print question1(None, 'ud')
# False
print question1(1, 'ud')
# False


def question2(s):
    import re
    import string

    if s is None or not isinstance(s, str):
        return TypeError('Not a string.')

    s = s.lower()
    s = re.sub('\s', '', s)
    s = s.translate(string.maketrans("", ""), string.punctuation)

    pal = s[0]
    for i in range(len(s)):
        for j in range(i):
            substr = s[j:i+1]
            if substr == substr[::-1]:
                if len(substr) > len(pal):
                    pal = substr

    return pal

print('')
print('Q2')
print question2('acbbcacdc')
# acbbca
print question2('qqaacbca')
# acbca
print question2('abcd')
# a
print question2(None)
# Not a string.
print question2(1)
# Not a string.


def question3(G):
    if not isinstance(G, Graph):
        return 'Input is not a graph.'

    return G.find_min_span()


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found is None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found is None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def find_min_span(self):
        srtEdges = sorted(self.edges, key=lambda x: x.value)
        eDict = {}
        visited = []
        while len(srtEdges) > 0:
            e = srtEdges.pop(0)
            if e.node_from.value not in visited or \
                e.node_to.value not in visited:
                    eDict.setdefault(e.node_from.value,
                                     []).append((e.node_to.value, e.value))
                    visited.append(e.node_from.value)
                    visited.append(e.node_to.value)

        for ed in eDict.keys():
            to_nodes = [i for i, j in eDict[ed]]
            for n in to_nodes:
                if n in eDict.keys():
                    to_nodes2 = [i for i, j in eDict[n]]
                    if ed not in to_nodes2:
                        for i, j in eDict[ed]:
                            if i == n:
                                val = j
                        eDict[n].append((ed, j))
                else:
                    for i, j in eDict[ed]:
                            if i == n:
                                val = j
                    eDict[n] = [(ed, val)]

            eDict[ed] = sorted(eDict[ed], key=lambda x: x[0])

        return eDict


g = Graph()
g.insert_edge(1, 'A', 'B')
g.insert_edge(2, 'B', 'C')
g.insert_edge(3, 'C', 'B')
g.insert_edge(4, 'C', 'A')

print('')
print('Q3')
print question3(g)
# {'A': [('B', 1)], 'B': [('A', 1), ('C', 2)], 'C': [('B', 2)]}
print question3(None)
# Input is not a graph.
print question3('teehee')
# Input is not a graph.


def question4(T, r, n1, n2):
    # T = tree (as matrix)
    # index of the list is equal to the integer stored in
    # that node and a 1 represents a child node.
    # r = root (integer)
    # n1, n2 = two Node objects
    if not isinstance(T, list):
        print 'Incorrect BST format.'
        return
    if not isinstance(r, int):
        print 'Root (r) should be an integer.'
        return
    if not isinstance(n1, int) or not isinstance(n2, int):
        return 'n1 and n2 must be integers'
        return

    nodes = [r]
    nodeD = {}
    n1D = None
    n2D = None
    while len(nodes) > 1 or not (n1D and n2D):
        startNode = nodes.pop(0)
        chil = 0
        for i in range(len(T[startNode])):
            entry = T[startNode][i]
            if entry == 1:
                nodes.append(i)
                temp = startNode
                nodeD.setdefault(i, []).append(temp)
                if startNode in nodeD.keys():
                    for j in nodeD[startNode]:
                        nodeD[i].append(j)

                chil += 1
            if entry == n1:
                n1D = nodeD[i]
            elif i == n2:
                n2D = nodeD[i]
            if chil == 2:
                break

    if n1D is None:
        return 'No common ancestor.'

    for i in n1D:
        if i in n2D:
            return i

    return 'No common ancestor.'

print('')
print('Q4')
print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 4)
# 3
print question4([[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]], 3, 1, 'a')
# n1 and n2 must be integers
print question4(None, None, None, None)
# Incorrect BST format.


def question5(ll, m):
    if not isinstance(ll, Node):
        print 'll must be a "Node" object'
        return
    if not isinstance(m, int) or m < 1:
        print 'm must be a positive integer'
        return

    cnt = 1  # counter for list length
    ans = ll
    while ll.next:
        ll = ll.next
        cnt += 1
        if cnt > m:
            ans = ans.next

    if cnt < m:
        print 'm is not longer than linked list length'
        return
    else:
        return ans.data


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

ll1 = Node('a')
ll2 = Node('m')
ll3 = Node('c')
ll4 = Node('e')
ll5 = Node('d')
ll6 = Node('.')
ll1.next = ll2
ll2.next = ll3
ll3.next = ll4
ll4.next = ll5
ll5.next = ll6

print('')
print('Q5')
print question5(ll1, 3)
# 'e'
print question5(ll1, 'a')
# m must be a positive integer
print question5(None, 3)
# ll must be a "Node" object
