#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the file that contains your dicision tree
"""
import math

class DTreeNode:
    """
    Your Node Class for your dicision tree
    """
    
    def __init__(self, key, data=None):
        """
        I am allowing these to be public to manipulate them easy
        """
        self.key = key      
        self.data = data
        self.clas = None #self.class gave an error
        self.edges = None #A dictionary storing the reference to children
          

class MyDecisionTree:
    """
    Will contain your deicision tree algorithm
    """
    
    def __init__(self):
        self.__myRoot = None
        self.__maxHeight = -1
        self.__minHeight = -1


    def train(self, xData, yData, maxDepth):
        """
        External interface for building the tree
        """
        #make tree
        tree = self._recursiveBuild(None, xData, None, yData, 0, maxDepth)
        #Set root
        self.__myRoot = tree

    def eval(self, xData):
        """
        External interface for evaluating the tree (Predicting)
        """
        #Get root from train
        root = self.__myRoot
        #_walk tree to predict
        return self._walk(root, xData)

    def _entropy(self, xData, xMap, col):
        """
        Will be used to calculate the entropy of column (col-relative to xData)
        xData is a 2D Python list
        xMap is a dictionary that maps the current column number to the original
        returns a list of unique elements in the col of xData and entropy of column
        """
        #Raise error if col is greater that number of columns in xData
        assert(col >= 0 and col <= len(xData[0]))
               
        elements = []
        for row in range(len(xData)):
            #get all elements in the column
            elements += [xData[row][col]]
        
        unique = list(set(elements)) #Unique elements in the column, will be returned
        numUni = len(unique) #Number of unique elements
        numElem = len(elements) #Number of all elements
        uniDict = {}
        for i in range(numUni):
            #Create a dictionary with each unique item and it's count
            uniDict.update({str(unique[i]):0})
        for j in range(numElem):
            #Update the number of a given item in the column
            uniDict[str(elements[j])] += 1
        
        #set entropy to 0
        entropy = 0
        for u in unique:
            num = uniDict[str(u)]
            #Calculate entropy given equation outlined in checkpoint4
            entropy -= num/numElem * math.log(num/numElem,2)
            
        return unique, entropy
            
    def _stripRowCol(self, xData, yData, colIn):
        """
        Will strip the column and rows related to the unique elements in col.
        returns a list of 2DLists.  One for each unique element.
        """
        #Get unique elements in stripped column
        uElementL = []
        numRows = len(xData)
        for element in range(numRows):
            if xData[element][colIn] not in uElementL:
                uElementL.append(xData[element][colIn])
        numNewLists = len(uElementL)
        
        #Create new lists for the unstripped rows/cols
        newXData = [[] for x in range(numNewLists)]
        newYData = [[] for j in range(numNewLists)]

        #If only 1 y element, simply keep that as newYData
        if len(yData) == 1:
            newYData[0] = yData
        
        #Else strip the given column
        else: 
            for col in range(numRows):
                if len(yData) == 1:
                    newYData[0] = yData
                else:
                    uniqueEl = xData[col][colIn]
                    listAssign = uElementL.index(uniqueEl)
                    newYData[listAssign].append(yData[col])

        #Strip xData
        for col in range(numRows):
            uniqueEl = xData[col][colIn]
            del xData[col][colIn]
            listAssign = uElementL.index(uniqueEl)
            newXData[listAssign].append(list((xData[col])))

        return newXData, newYData
    
    def _recursiveBuild(self, root, xData, xMap,  yData, currentDepth, maxDepth):
        """
        Where you really will build the tree
        root - of the current subtree (may not be used)
        xData - 2D Python List of attributes
        xMap - Dictionary mapping current rows to those in the original 
        yData - Output
        currentDepth - How many times we have already recursed
        maxDepth - how many level the tree will have at most
        """
        currentDepth += 1
        
        ##Base cases
        if len(xData[0]) == 1:
            key = 0 #Not sure about this
            node = DTreeNode(key)
            node.edges = None
            
            #Find frequency of each element in xData
            uniDict = {}
            for i in range(len(xData)):
                if str(xData[i][0]) not in uniDict:
                    uniDict.update({str(xData[i][0]):0}) 
                else:
                    uniDict[str(xData[i][0])] += 1
                            
            #Find element with max frequency
            maxUni = str(xData[0][0]) #unique element that occurs the most
            for k in range(len(uniDict)):
                if uniDict[str(xData[k][0])] > uniDict[maxUni]:
                    maxUni = str(xData[k][0])
            for l in range(len(xData)):
                #print(xData[l])
                if int(maxUni) in xData[l]:
                    predictedY = yData[l]
                    break
            #Predict yData as element with max frequency
            node.clas = predictedY
            
            return node
             
        if currentDepth == maxDepth:
            node = DTreeNode(None)
            node.clas = root.clas
            node.edges = None
            return node
            
        ##Calculate the entropy of our attributes
        xEntropy = [None]*len(xData[0])
        for col in range(len(xData[0])):
            entropy = self._entropy(xData, xMap, col)[1]
            xEntropy[col] = entropy
                    
        ##Calculate the estimate change in entropy for our attribute         
        minCol = 0
        for i in range(len(xEntropy)):
            if xEntropy[i] < xEntropy[minCol]:
                minCol = i
        unique = self._entropy(xData, xMap, minCol)[0]
        
        ##Make new node based on minCol Entropy
        key = minCol #Not sure about this
        tNode = DTreeNode(key)
        
        #build a dictionary with unique values and their frequency
        #Unique value with highest frequency is predicted y value
        uniDict = {}
        for i in range(len(unique)):
            uniDict.update({str(unique[i]):0})
       
        for j in range(len(xData)):
            uniDict[str(xData[j][minCol])] += 1
                
        maxUni = str(xData[0][minCol]) #unique element that occurs the most

        for k in range(len(unique)):
            if uniDict[str(xData[k][minCol])] > uniDict[maxUni]:
                maxUni = str(xData[k][minCol])
                
        #Find predicted yData element that is most likely
        for l in range(len(xData)):
            if int(maxUni) in xData[l]:
                predictedY = yData[l]
                break
        tNode.clas = predictedY

        ##Split xData and yData based on minCol
        newXData, newYData = self._stripRowCol(xData, yData, minCol)
        
        ##Loop over all lists and store in edges
        tNode.edges = {}
        for j in range(len(newXData)):
            if len(yData) == 1:
                returnRef = self._recursiveBuild(tNode, newXData[j], None, newYData[0], currentDepth, maxDepth)
            else:
                returnRef = self._recursiveBuild(tNode, newXData[j], None, newYData[j], currentDepth, maxDepth)
            for i in range(len(unique)):
                tNode.edges.update({str(unique[i]):returnRef})
        return tNode

    def _walk(self, root, xData):
        """
        Walks the tree 
        returns the most likely ydata classifier
        """
        #If we get to a leaf node, return the prediction
        if root.edges == None:
            return root.clas
        
        #Create a dummy yData list to use in _stripRowCol later
        yData = [None]*len(xData)
        for i in range(len(xData)):
            yData[i] = 0
                 
        #Find the column that the split is occuring
        split = root.key
        
        #Find element in split column that occurs the most
        uniDict = {}
        for j in range(len(xData)):
            if xData[j][split] not in uniDict:
                uniDict.update({xData[j][split]:1})
            else:
                uniDict[xData[j][split]] += 1
                       
        #Split unknown xData
        predXData, predYData = self._stripRowCol(xData, yData, split)
        
        #Follow child that corresponds to most frequent element in split, if it exists
        maxKey = list(uniDict.keys())[0]
        for key in uniDict:
            if uniDict[key] > uniDict[maxKey]:
                maxKey = key          
        if str(maxKey) in root.edges:
            nextChild = root.edges[str(maxKey)]
        else:
            nextChild = list(root.edges.values())[0]
            
        #Walk rest of the tree
        pred = []
        for i in range(len(predXData)):
            pred += [self._walk(nextChild, predXData[i])]
        
        #Return predictions
        return pred
        
        
def testMyDecisionTree():
    """
    Used for your testing
    """
    t1 = MyDecisionTree()
    xData1 = [[0,1,4],[1,1,3],[0,0,4],[0,1,7],[1,0,3],[1,1,4]]
    col = 2
    print('Test entropy on xData \n')
    print('Unique values in col 2: ', t1._entropy(xData1,None,col)[0], '\n')
    print('Entropy of col 2: ', t1._entropy(xData1,None,col)[1], '\n')
    
    t2 = MyDecisionTree()
    xData2 = [[0,1,2],[0,2,2],[1,0,0],[0,1,2]]
    yData2 = [2,0,1,0]
    
    print('Test split on x and y data  \n')
    newX, newY = t2._stripRowCol(xData2, yData2, 1)
    print('x split on col 1: ', newX, '\n')
    print('y split on col 1: ', newY, '\n')
    
    uX = [[1,2,1],[0,0,2]]
    t3 = MyDecisionTree()
    print('Test recursive build and walk \n')
    t3.train(xData2, yData2, 16)
    print('Predictions: ', t3.eval(uX))
    


if __name__ == "__main__":
    testMyDecisionTree()