# AUTHOR: Written by Junhyeok Jeong (jeongju@oregonstate.edu)
# ID: 933196042
# CLASS: CS325 - 400 (2019 Fall)
# ASSIGNMENT: Homework 5

import sys
import string
import numpy
import math
import collections

#set up class Vertex for storing each wrestler information
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.state = 'unvisited'
        self.team = 'none'
        self.distance = 9999

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)

#set up class Graph for applying BFS algorithm with queue
class Graph:
    def __init__(self):
	    self.vertices = {}
	    self.possible = True
	    self.root = None
	    self.counter = 0

#graph needs to be added vertex with a function
    def add_vertex(self, wrestler):
        try:
            self.vertices[wrestler.name] = wrestler
            if self.counter == 0:
                self.root = wrestler
                self.counter += 1
        except:
            return -1

#adding edge based on the input text file values. use hashtable method(key and value) for this  
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

#implementation part of devised bfs
    def bfs(self, vertex):
        queue = []
        vertex.distance = 0
        vertex.team = 'Babyfaces'
        vertex.state = 'visited'

    #if a vertex has neighbors, then add distance to seperate
        for i in vertex.neighbors:
            self.vertices[i].distance = vertex.distance + 1
            self.vertices[i].team = 'Heels'
            queue.append(i)

    #change state attribute as the vertex is visited
        while len(queue) > 0:
            node = queue.pop(0)
            node_u = self.vertices[node]
            node_u.state = 'visited'

            for i in node_u.neighbors:
                node_v = self.vertices[i]
                if node_v.state == 'unvisited':
                    queue.append(i)

                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1

    #if distance is even, then node's team set to Babyfaces
                    if node_v.distance % 2 == 0:
                        node_v.team = 'Babyfaces'
    #if distance is odd, then node's team set to Heels
                    elif node_v.distance % 2 != 0:
                        node_v.team = 'Heels'

    #if both key node and value node team values are the same, then BFS is impossible 
                    if node_u.team == node_v.team:
                        self.possible = False
    
    #function for checking unvisited vertex
    def unvisited_check(self):
        for i in self.vertices:
            if self.vertices[i].state == 'unvisited':
                self.vertices[i].state = 'visited'
                if self.vertices[i].team == 'none':
                    self.vertices[i].team = 'Babyfaces'
                
                for j in self.vertices[i].neighbors:
                    if self.vertices[j].state == 'unvisited':
                        self.vertices[j].team = 'Heels'


            
            




#main part
mylines = []

#store all lines from a text file in an array
while True:
	try:
		with open(input(), "r") as f:
			for i,line in enumerate(f):
				mylines.append(line.strip())

		f.close()
		break

	except:
		print("error: the input file name is not valid! please type again!")


line_index = 0
g = Graph()


name_num = int(mylines[line_index])
line_index += 1


#add vertices with for loop of text file lines
for i in range(name_num):
	g.add_vertex(Vertex(mylines[line_index]))
	line_index += 1

edge_num = int(mylines[line_index])
line_index += 1

#add edges with for loop of text file lines
for i in range(edge_num):
	edge_info = list( mylines[line_index].split())
	g.add_edge(edge_info[0],edge_info[1])
	line_index += 1

g.bfs(g.root)
g.unvisited_check()

#if BFS is possible, then print the result on the terminal
if g.possible == True:
    babyfaces = []
    heels = []
    print("Yes Possible")

    for i in g.vertices:
        if g.vertices[i].team == 'Babyfaces':
            babyfaces.append(g.vertices[i].name)
        if g.vertices[i].team == 'Heels':
            heels.append(g.vertices[i].name)
    print("Babyfaces: {0}".format(" ".join(map(str, babyfaces))))
    print("Heels: {0}".format(" ".join(map(str, heels))))


else:
    print("No Impossible")
