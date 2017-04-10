"""
Will be used to make a decision tree using sklearn
More details will be added to this later
"""

import math
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
#from sklearn.tree import predict


class SKTree:
    
    def __init__(self):
        """
        More information will be given about this later
        """
        self.tree = None


    def train(self, xData, yData, maxDepth):
        """
        Pre: xData is a 2D list containing mapped parameters from given documents
             yData is the 1D list containing the mapped from info
        Post: makes decision tree and .dot document that contains tree 
              graphic information
        """
        #Make tree        
        tree = DecisionTreeClassifier(criterion="entropy", max_depth=maxDepth, random_state=0)
        #Fit to parameters
        tree = tree.fit(xData, yData)
        
        dot_data = export_graphviz(tree, out_file='traintree.dot', \
                                   feature_names=['Date', 'toInfo', 'Forward', 'Reply','Top10','Bott10'])
    
        self.tree = tree
    
    def eval(self, xData):
        """
        Pre: xData is the known data from the eval folder, a 2D list of mapped parameters
        Post: Returns a list containing the predicted sender of the email for 
              each doument in the eval folder
        """
        
        pred = self.tree.predict(xData)
        
        return pred


def testSKTree():
    """
    Used to test my SKTree
    Predicts some random list of parameters
    """
    warn = input('WARNING: If you are testing this comment out the dot_data line 34. \nY to continue N to cancel: ')
    if warn == 'Y':
        s = SKTree()
    
        knownX = [[1,0,7],[1,4,2],[7,2,4],[8,1,0]]
        knownY = [3,6,2,6]
    
        unknownX = [[0,4,7],[1,5,2],[8,4,1],[4,2,1]]
    
        s.train(knownX, knownY, 4)
        prediction = s.eval(unknownX)
    
        print(prediction)
    else:
        pass

if __name__ == "__main__":
    testSKTree()
