class Graph:
    def __init__(self,direct):
        self.graphNode={}
        self.graphEdge=[]
        self.graph=[]
        self.direct=direct
        self.exploredSet=[]
        self.frontierSet=[]
        self.frontierSetWithPathCost=[]
        self.frontierSetWithDepth=[]
        
    def Add_Node(self,Node,action):

        self.graphNode[Node]={"State":Node,"Action":action}
         
    def Add_Edge(self,Node1,Node2,cost):#Node1:Node Start Node2:Node End

        if not self.direct:
            self.graphEdge.append({"from":Node1,"To":Node2,"cost":cost})
            self.graphEdge.append({"from":Node2,"To":Node1,"cost":cost})
        else:
            self.graphEdge.append({"from":Node1,"To":Node2,"cost":cost})
            
    def Add_Child(self,Node,cost,parent,pathCost,action):
        
        self.graph.append({"node":Node,"cost":cost,"parent":parent,"path_cost":pathCost,"Action":action})
        
        return self.graph[-1]
        
    def CostOfEdge(self,Parent,Node):
        for item in self.graphEdge:
            if (item["To"]==Node and item["from"]==Parent) or (item["from"]==Node and item["To"]==Parent and self.direct==False):
                return item["cost"]
    
    def CostOfParent(self,Parent,Node):
        for item in self.graph:
            if item["node"]==Parent and Node in item["Action"]:
                return item["path_cost"]
    
    def show_Graph(self):
        for value in self.graph:
            print(f'Node:{value} -> {self.graph[value]}\n')
            
    def Breadh_First_Search(self,Node,NodeEnd):
        
        node=self.Add_Child(Node['State'],0,Node['State'],0,Node['Action'])

        if Node['State']==NodeEnd['State']:
            return self.Search_Answer(node,Node)
        
        self.frontierSet.insert(0,Node['State'])

        while True:         
            if self.frontierSet==[] :
                return print('failure')
                
            node=self.frontierSet.pop()
            self.exploredSet.append(node)
            for child in self.graphNode[node]['Action']:
                
                costChild=self.CostOfEdge(node,child)
                childNode=self.Add_Child(child,costChild,node,self.CostOfParent(node,child)+costChild,self.graphNode[child]['Action'])
                if childNode['node'] not in self.exploredSet and childNode['node'] not in self.frontierSet:
                    
                    if childNode['node']==NodeEnd['State']:
                        return self.Search_Answer(childNode,Node)
                    self.frontierSet.insert(0,child)
                    
                    
    def Uniform_Cost_Search(self,Node,NodeEnd):
        
        node=self.Add_Child(Node['State'],0,Node['State'],0,Node['Action'])

        if Node['State']==NodeEnd['State']:
            return self.Search_Answer(node,Node)
        
        self.frontierSetWithPathCost.insert(0,{"node":Node['State'],"path_cost":node["path_cost"],"parent":node["parent"]})

        while True:         
            if self.frontierSetWithPathCost==[] :
                return print('failure')
                
            node=self.frontierSetWithPathCost.pop(0)

            if node['node']==NodeEnd['State']:
                return self.Search_Answer(node,Node)
            
            self.exploredSet.append(node["node"])
            for child in self.graphNode[node["node"]]['Action']:
                
                costChild=self.CostOfEdge(node["node"],child)
                childNode=self.Add_Child(child,costChild,node["node"],self.CostOfParent(node["node"],child)+costChild,self.graphNode[child]['Action'])
               
                if childNode['node'] not in self.exploredSet:
                    nodeInfrontierSet=self.CheckInfrontierSet(self.frontierSetWithPathCost,childNode["node"])
                    
                    if nodeInfrontierSet[0]==True:
                        
                        self.frontierSetWithPathCost.insert(0,{"node":childNode['node'],"path_cost":childNode["path_cost"],"parent":node["node"]})
                        self.frontierSetWithPathCost = sorted(self.frontierSetWithPathCost, key=lambda x: x["path_cost"])
                    else:
                       
                        if self.frontierSetWithPathCost[nodeInfrontierSet[1]]["path_cost"] > childNode["path_cost"]:
                            self.frontierSetWithPathCost.pop(nodeInfrontierSet[1])
                            self.frontierSetWithPathCost.insert(nodeInfrontierSet[1],{"node":childNode["node"],"path_cost":childNode["path_cost"],"parent":node["node"]})
                            self.frontierSetWithPathCost = sorted(self.frontierSetWithPathCost, key=lambda x: x["path_cost"])
                        
            
    def Depth_First_Search(self,Node,NodeEnd):
        node=self.Add_Child(Node['State'],0,Node['State'],0,Node['Action'])

        if Node['State']==NodeEnd['State']:
            return self.Search_Answer(node,Node)
        
        self.frontierSet.insert(0,Node['State'])

        while True:         
            if self.frontierSet==[] :
                return print('failure')
                
            node=self.frontierSet.pop(0)
            self.exploredSet.append(node)
            Actions=self.graphNode[node]['Action']
            for child in list(reversed(Actions)):
                
                costChild=self.CostOfEdge(node,child)
                childNode=self.Add_Child(child,costChild,node,self.CostOfParent(node,child)+costChild,self.graphNode[child]['Action'])
                if childNode['node'] not in self.exploredSet and childNode['node'] not in self.frontierSet:
                    
                    if childNode['node']==NodeEnd['State']:
                        return self.Search_Answer(childNode,Node)
                    self.frontierSet.insert(0,child)
                    
               
    def Depth_Limited_Search(self,Node,NodeEnd):
        Limited=5
        replaceArray=[]
        Depth=0
        node=self.Add_Child(Node['State'],0,Node['State'],0,Node['Action'])

        if Node['State']==NodeEnd['State']:
            return self.Search_Answer(node,Node)
        
        self.frontierSetWithDepth.insert(0,{"node":Node['State'],"Depth":0})

        while True:         
            if self.frontierSetWithDepth==[] :
                return print('failure')
            node=self.frontierSetWithDepth.pop(0)
            Depth=node["Depth"]
            if(Depth<Limited):
                self.exploredSet.append(node["node"])
            else:
                for items in self.frontierSetWithDepth:
                    if items["Depth"]<Limited:
                        replaceArray.append(items)
                self.frontierSetWithDepth=replaceArray
                node=self.frontierSetWithDepth.pop(0)
                self.exploredSet.append(node["node"])
                if self.frontierSetWithDepth==[] :
                    return print('failure')

            Actions=self.graphNode[node["node"]]['Action']

            for child in list(reversed(Actions)):
                
                costChild=self.CostOfEdge(node["node"],child)
                childNode=self.Add_Child(child,costChild,node["node"],self.CostOfParent(node["node"],child)+costChild,self.graphNode[child]['Action'])
                if childNode['node'] not in self.exploredSet :
                    
                    nodeInfrontierSet=self.CheckInfrontierSet(self.frontierSetWithDepth,childNode["node"])
                    
                    if nodeInfrontierSet[0]==True:
                        
                        if childNode['node']==NodeEnd['State']:
                            return self.Search_Answer(childNode,Node)
                        self.frontierSetWithDepth.insert(0,{"node":child,"Depth":Depth+1})

               
               
               
               
                
    def CheckInfrontierSet(self,frontierSet,NodeName):
        for index,item in enumerate(frontierSet):
            if item["node"]==NodeName:
                return [False,index]
        return [True,0]
    
    def Search_Answer(self,Node,StartNode):
        print(f"\nAll Cost:{Node["path_cost"]}")

        parent=Node["parent"]
        MyNode=Node["node"]
        AnswerNode=[]
        AnswerNode.append(MyNode)
        if Node["parent"]==MyNode:
            return self.Print_Answer([MyNode])
        while True:
            found = False  

            for item in self.graph:
                if item["node"] == parent and MyNode in item["Action"]:
                    AnswerNode.insert(0, parent)
                    parent = item["parent"]
                    MyNode=item["node"]
                    
                    if parent == StartNode["State"]:
                        AnswerNode.insert(0, parent)
                        return self.Print_Answer(AnswerNode)
                    
                    found = True 
                    break  

            if not found: 
                print("Parent not found in the graph.")
                break  

            if parent is None:  
                print("Reached a None parent.")
                break
                
    def Print_Answer(self,array):
        
        for index, item in enumerate(array):
            if index == len(array) - 1:
                print(f"{item}")
            else:
                print(f"{item} -> ", end="")
        
     