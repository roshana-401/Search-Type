from Graph import Graph
import queue   

search=Graph(False)

#Add Node with Actions
search.Add_Node("Arad",["Zerind","Timisoara","Sibiu"])
search.Add_Node("Zerind",["Arad","Oradea"])
search.Add_Node("Oradea",["Zerind","Sibiu"])
search.Add_Node("Sibiu",["Oradea","Arad","Rimnicu","Fagaras"])
search.Add_Node("Timisoara",["Arad","Lugoj"])
search.Add_Node("Lugoj",["Timisoara","Mehadia"])
search.Add_Node("Mehadia",["Lugoj","Dobreta"])
search.Add_Node("Dobreta",["Mehadia","Craiova"])
search.Add_Node("Craiova",["Rimnicu","Pitasti","Dobreta"])
search.Add_Node("Pitasti",["Rimnicu","Craiova","Bucharest"])
search.Add_Node("Rimnicu",["Sibiu","Pitasti","Craiova"])
search.Add_Node("Fagaras",["Sibiu","Bucharest"])
search.Add_Node("Bucharest",["Giurgiu","Orziceni","Pitasti","Fagaras"])
search.Add_Node("Giurgiu",["Bucharest"])
search.Add_Node("Orziceni",["Bucharest","Hirsova","Vasfui"])
search.Add_Node("Hirsova",["Eforie","Orziceni"])
search.Add_Node("Eforie",["Hirsova"])
search.Add_Node("Vasfui",["Orziceni","fasi"])
search.Add_Node("fasi",["Vasfui","Neamt"])
search.Add_Node("Neamt",["fasi"])

#Add Node with Edge

search.Add_Edge("Arad","Sibiu",140)
search.Add_Edge("Arad","Zerind",75)
search.Add_Edge("Arad","Timisoara",118)
search.Add_Edge("Zerind","Oradea",71)
search.Add_Edge("Oradea","Sibiu",151)
search.Add_Edge("Timisoara","Lugoj",111)
search.Add_Edge("Lugoj","Mehadia",70)
search.Add_Edge("Mehadia","Dobreta",75)
search.Add_Edge("Dobreta","Craiova",120)
search.Add_Edge("Craiova","Rimnicu",146)
search.Add_Edge("Rimnicu","Sibiu",80)
search.Add_Edge("Sibiu","Fagaras",90)
search.Add_Edge("Rimnicu","Pitasti",97)
search.Add_Edge("Craiova","Pitasti",138)
search.Add_Edge("Pitasti","Bucharest",101)
search.Add_Edge("Fagaras","Bucharest",211)
search.Add_Edge("Bucharest","Orziceni",85)
search.Add_Edge("Giurgiu","Bucharest",90)
search.Add_Edge("Orziceni","Hirsova",98)
search.Add_Edge("Hirsova","Eforie",86)
search.Add_Edge("Orziceni","Vasfui",142)
search.Add_Edge("Vasfui","fasi",92)
search.Add_Edge("fasi","Neamt",87)


print('\nchoose your Node Star:')
print("Arad")
print("Sibiu")
print("Zerind")
print("Timisoara")
print("Oradea")
print("Lugoj")
print("Mehadia")
print("Dobreta")
print("Rimnicu")
print("Craiova")
print("Pitasti")
print("Fagaras")
print("Giurgiu")
print("Bucharest")
print("Hirsova")
print("Eforie")
print("Orziceni")
print("Vasfui")
print("fasi")
print("Neamt\n")

NodeStart=input()

print('\nchoose your Node End:')
print("Arad")
print("Sibiu")
print("Zerind")
print("Timisoara")
print("Oradea")
print("Lugoj")
print("Mehadia")
print("Dobreta")
print("Rimnicu")
print("Craiova")
print("Pitasti")
print("Fagaras")
print("Giurgiu")
print("Bucharest")
print("Hirsova")
print("Eforie")
print("Orziceni")
print("Vasfui")
print("fasi")
print("Neamt\n")

NodeEnd=input()
Node=search.graphNode[NodeStart]
NodeEnd=search.graphNode[NodeEnd]


print("\nChoose Algorithm:\n")
print("1.Breadh First Search")
print("2.Uniform Cost Search")
print("3.Depth First Search")
print("4.Depth Limited Search")
print("5. A* search")
print("6.Gready Search")

choose=int(input())

if choose==1:
    search.Breadh_First_Search(Node,NodeEnd)
elif choose==2:
    search.Uniform_Cost_Search(Node,NodeEnd)
elif choose==3:
    search.Depth_First_Search(Node,NodeEnd)
elif choose==4:
    search.Depth_Limited_Search(Node,NodeEnd)

# print('Welcome to the different search app to find the route:\n')
# print('This is our graph:\n')




