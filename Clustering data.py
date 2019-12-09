#there are foolowing steps for implementing kmeans clustering algorithm:
#step#1: Select no of cluster to be identified i.e value of k it can be determined using Elbow algorithm
#step#2:Randomly select k distinct data point
#step#3:Measure the distance between first point(Which is randomly selected) and the  K clusters
#step#4: Assign first point to the nearest cluster 
#step#5:  determine to which cluster point 2 belongs to how
import sys                                              
from random import shuffle,uniform
import math
from colorama import Fore,Back,Style
import tkinter as tk
from tkinter import*
import random
import time
#Read data from dataset to be cluster#
def ReadData(fileName):                     #Function to read data from file
    f = open(fileName,'r')                  #open the file to be read
    lines = f.read().splitlines()           #This function will store line by line to lines variable split paragraph at line endl
    f.close()                               #close file afte reading data
    #print(lines)
    items = []                              #initializing list in which data is to be copied for clustering as single item

    for i in range(1,len(lines)):
        line = lines[i].split(',')          #for dividind item's attributes as features upon which it can be clustered 
        itemFeatures = []                   #intialization of list for storing attribiutes upon whih cluster is based
       #print(line)
        for j in range(len(line)-1):
            v = float(line[j]);             #convert features values in the float value so that it can be clustered eaisly.
            itemFeatures.append(v);          #Add features to the list 

        items.append(itemFeatures)          #Add list of feature in list of items having feature

    shuffle(items)                           # Shuffling items

    return items                             #returning shuffled items.
#Step No 1:
#def GetclusterValue():
    #We have to install Anaconda for repesnting elbow point using inertial  and by distortion
                                           #Additional function for seprating item's feature in max and minima 
def FindMinMax(items):
    n = len(items[0])
    minima = [sys.maxsize    for i in range(n)]  #for  initializing all the value minima list to positive infinity
    maxima = [-sys.maxsize-1 for i in range(n)]  # for intializing all value of maxima to zero to negative infinity
    
    for item in items:                            #For sepreting items attribute as maxima and as minima list less values in minima list and are
        for f in range(len(item)):                #storing features   minimum values into minima list and maximum values into maxima list 
            if(item[f] < minima[f]):              #by comparing same index of feature with minima
                minima[f] = item[f]               # Assigning small value to minma list
            if(item[f] > maxima[f]):              # Comparing maxima value to the item index 
                maxima[f] = item[f]               #storing the maximum value to the maxima list

    return minima,maxima                          # returning maxima and minima  list values

#step#02:
def InitializeMeans(items,k,cMin,cMax):             #Function for defining means which are basically clusters which are centriod to be formed 

    f = len(items[0]);                               #number of features
    means = [[0 for i in range(f)] for j in range(k)]  #comprehension list for intializing list for k cluster intializing means between them
    #print(means)
    for mean in means:
        for i in range(len(mean)):                      #as means is list of list so loop through the list for assigning random no to means 
            
            mean[i] = uniform(cMin[i]+1,cMax[i]-1)       #Uniform function for getting random mean as a centroid

    return means 
#step#03:                                         #returning means with some intialize values  
def EuclideanDistance(x,y):                               #Euclideanfunction for clculating distance between two points which decide clusters of points
    S = 0; 
    for i in range(len(x)):
        S += math.pow(x[i]-y[i],2)             
                               # Formula for getting distance between two points p(x1,y1) and q(x2,y2) is given as D=((x2-x1)^2+(y2-y1)^2)^1/2
    return math.sqrt(S);  
#step#4:          #for eliminating square root
def UpdateMean(n,mean,item):         
    for i in range(len(mean)):      #after  getting distance or deciding which cluster should selected 
        m = mean[i]                 #We have to calculate mean including new point which would be different from the previous one which is already
        m = (m*(n-1)+item[i])/float(n) #hence we need to update it according to the given formula 
        mean[i] = round(m,3)          # By rounding off the mean upto the three decimal 
    return mean                       #return mean value which is updated recently  
#Step#05
def FindClusters(means,items):         #Now we have to decide which cluster should be selected for the the point  
    clusters = [[] for i in range(len(means))];  #Intializing clusters as list and then filling them with values  
    #print(clusters)
    for item in items:                     #iterate attributes from items
        #Classify item into a cluster
        index = Classify(means,item)       #Calling classify function  which return the index of cluster which offer minimum distance of data point                                  #from the clusters 
        clusters[index].append(item)        #Adding item into the suitable index index representing cluster one ,two and three.
    #print(clusters)                      
    return clusters                          #this function will return the list of clusters having further clusters in it 

def Classify(means,item):                     #This classify function will get means and item in this function parameter means represnting cluster 
                                               #Classify item to the mean/cluster with minimum distance
    minimum = sys.maxsize                      #intializing the minimum variable to positive infinity for finding the minimum value
    index = -1                                 #intializing index to minus value due to the avoid from confusion
    #print(means)
    for i in range(len(means)):
        #Find distance from item to mean
        dis = EuclideanDistance(item,means[i])   #Check by passing different values of cluster means and checking them with a particular point and 
                                      #which cluster is closest to the given point and deciding the cluster or mean for particular point
        if(dis < minimum):            #check for minimum point
            minimum = dis
            index = i
    
    return index                       #returning suitable index upon which item should append 

def CalculateMeans(k,items,maxIterations=100):
                                                 #Find the minima and maxima for columns
    cMin, cMax = FindMinMax(items)
    
                                                  #Initialize means at random points
    means = InitializeMeans(items,k,cMin,cMax)
                                               #Initialize clusters, the array to hold
                                               #the number of items in a class
    clusterSizes = [0 for i in range(len(means))] 
   #print(clusterSizes)                          #getting size of a single cluster
                                                 #An array to hold the cluster an item is in
    belongsTo = [0 for i in range(len(items))]   #A list to  hold the cluster 
    #Calculate means
    for i in range(maxIterations):                #its prediction of iteration for which we achieve the equal variation for all the cluster
                                                 #If no change of cluster occurs, halt
        noChange = True
        for i in range(len(items)):                #iterate through the items/attributes 
            item = items[i]                         
                                                #Classify item into a cluster and update the
                                                 #corresponding means.
            index = Classify(means,item)

            clusterSizes[index] += 1              #for placing next item increment to index of clusters
            means[index] = UpdateMean(clusterSizes[index],means[index],item) #it will store the updated mean to the suitable index

                                                 #Item changed cluster
            if(index != belongsTo[i]):             #Check wether the data point is stop changing thier cluster 
                noChange = False

            belongsTo[i] = index           #Assign index to related items

                                           #Nothing changed, return
        if(noChange):
            break                             #when we achieve our desired state there is less variation

    return means

def main():
    items = ReadData("E:/Web designing/data.txt")
    k = 3
    root=Tk()
    def readdata():
        w = tk.Label(root, bg="powder blue",fg="black",text="Data imported suceesfully!!!!!")
        w.pack()
    def KValue():
        k = 3
        w = tk.Label(root, bg="powder blue",fg="black",text="Value of K Is")
        w.pack()
    def process():
         means = CalculateMeans(k,items)
         clusters = FindClusters(means,items)
         print(means)
         #print(Fore.RED + 'some red text')
         #print(Back.GREEN + 'and with a green background')
         #print(Style.DIM + 'and in dim text')
         print(Fore.GREEN + "clusters")
         print(clusters)
   
    
    root.geometry("1600x800+0+0")
    root.title("Clustering People using Scrap Data")
    Tops=Frame(root,width=1600,height=50,bg="powder blue", relief=SUNKEN)
    Tops.pack(side=TOP)
    #=================================Time==========================
    localtime=time.asctime(time.localtime(time.time()))
    #=================================Info==========================
    lblInfo=Label(Tops,font=('arial',50,'bold'),text="Clustering People using Scrap Data",fg="Steel Blue",bd=10)
    lblInfo.grid(row=0,column=0)
    lblInfo=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
    lblInfo.grid(row=1,column=0)
#===============================Buttons===========================
    start_button = Button(root, text="IMPORT FILE",padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,bg="powder blue")

    cancel_button = Button(root,text="CLUSTER VALUE",padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,bg="powder blue")

    center_button = Button(root,text="PROCESS ALGO",padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,bg="powder blue")
    start_button.bind("<Button-1>",readata)
    start_button.pack(side=TOP)
    cancel_button.bind("<Button-1>",KValue)
    cancel_button.pack(side=TOP)
    center_button.bind("<Button-1>",process)
    center_button.pack(side=TOP)
    root.mainloop()
    #print Classify(means,newItem);

if __name__ == "__main__":
    main()

