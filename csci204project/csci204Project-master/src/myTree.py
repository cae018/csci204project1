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
        pass


    def eval(self, xData):
        """
        External interface for evaluating the tree (Predicting)
        """
        pass


    def _entropy(self, xData, xMap, col):
        """
        Will be used to calculate the entropy of column (col-relative to xData)
        xData is a 2D Python list
        xMap is a dictionary that maps the current column number to the original
        returns a list of unique elements in the col of xData and entropy of column
        """
        #Only have 6 columns so raise error if col > 5
        assert(col >= 0 and col <= 5)
        #There are 6 columns of xData from the train folder
        #[date, to, forward, reply, top10, bott10]
        #xMap = {0: 'date', 1: 'to', 2: 'forward', 3: 'reply', 4: 'top10', 5: 'bott10'}
               
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
        print(uniDict)
        
        #set entropy to 0
        entropy = 0
        for u in unique:
            num = uniDict[str(u)]
            #Calculate entropy given equation outlined in checkpoint4
            entropy -= num/numElem * math.log(num/numElem,2)
            
        return unique, entropy
            
    def _stripRowCol(self, xData, yData, col):
        """
        Will strip the column and rows related to the unique elements in col.
        returns a list of 2DLists.  One for each unique element.
        """
        pass
    
    def __recursiveBuild(self, root, xData, xMap,  yData, currentDepth, maxDepth):
        """
        Where you really will build the tree
        root - of the current subtree (may not be used)
        xData - 2D Python List of attributes
        xMap - Dictionary mapping current rows to those in the original 
        yData - Output
        currentDepth - How many times we have already recursed
        maxDepth - how many level the tree will have at most
        """
        pass

    def _walk(self, root, xData, xMap):
        """
        Walks the tree 
        returns the most likely ydata classifier
        """
        pass

def testMyDecisionTree():
    """
    Used for your testing
    """
    t = MyDecisionTree()
    xData = [[0,1,4],[1,1,3],[0,0,4],[0,1,7],[1,0,3],[1,1,4]]
    xMap = {0: 'date', 1: 'to', 2: 'forward', 3: 'reply', 4: 'top10', 5: 'bott10'}
    col = 2
    #Test entropy
    print(t._entropy(xData,xMap,col))


if __name__ == "__main__":
    testMyDecisionTree()