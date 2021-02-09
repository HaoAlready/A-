# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
import sys
all_data = []
dict = dict()
start = {}
node_visited = []
node_reach = []
open_set = []
close_set = []

class node:
    def __init__(self,numb,parent,cost,realcost):
        self.numb = numb
        self.parent = parent
        self.cost = cost
        self.realcost = realcost

    def cost(self):
        return self.cost

    def parent(self):
        return self.parent

    def numb(self):
        return self.numb

    def real(self):
        return self.realcost

    def p(self):
        print(self.numb,self.parent,self.cost,self.realcost)

def read_data():
    fr = open("data.txt", "r") # 设置文件对象
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split(',')
        newline = [0, 0, 0]
        newline[0] = (int(listFromLine[0]))
        newline[1] = (int(listFromLine[1]))
        newline[2] = (float(listFromLine[2]))
        all_data.append(newline)
    fr.close()

def dijkstra():
    while (bool(dict)):
        min_dis = min(zip(dict.values(), dict.keys()))
        node = min_dis[1]
        if node not in node_visited: #Node not visited
                for d in all_data:
                    if d[0] == node:     #Find this node
                        if d[1] in dict.keys():
                            res1 = float(dict[node])
                            res2 = float(d[2])
                            #if d[1] ==99:
                            #print(node,min_dis[0],res1 + res2)
                            if float(dict[d[1]]) > res1 + res2:   #New distance smaller
                                dict[d[1]] = res1 + res2
                            else:
                                continue

        del dict[node]
        start[node]= min_dis[0]
        node_visited.append(node)

def A_star(target):
    n = open_set[0]
    s = n
    index = 0
    while len(open_set):
        if n.numb == target.numb:
            count_distance(s,n)
            sys.exit()
        if not n.numb == target.numb:   #不是想要的点
            #print('fir'+ str(n.numb))
            #print('sed'+ str(target.numb))
            for temp in all_data: #找点加点
                if temp[0] == n.numb:  #找点
                    realcost = temp[2] + float(n.real())
                    cost = 10 + realcost
                    nodetemp = node(temp[1],n,cost,realcost)
                    if nodetemp not in close_set:
                        open_set.append(node(temp[1],n,cost,realcost))
                    else:
                        continue
            index = open_set.index(n)
            del open_set[index]
            close_set.append(n)
            n = open_set[0]

        for item in open_set:
            if item.cost < n.cost:
                n = item



def count_distance(s,d):
    start = d
    way = []
    way.append(start)
    while not start==s:
        start = d.parent
        way.append(start)
    #way.reverse()
    allnode = []
    while way:
        n = way.pop()
        allnode.append(n.numb)
    print('The way is '+str(allnode))
    print('The distance is '+ str(n.realcost))


def main():
    read_data()
    a = input("input source: ")
    b = input("input dest: ")
    n0 = node(int(a),None,0,0)
    open_set.append(n0)
    target = node(int(b),None,None,None)
    A_star(target)

if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
