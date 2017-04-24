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
        
        #Create a graphviz visualization of tree
        dot_data = export_graphviz(tree, out_file='traintree.dot', \
                                   feature_names=['Date', 'toInfo', 'Forward', 'Reply','Top10','Bott10'])
    
        #Set the tree attribute to the created tree
        self.tree = tree
    
    def eval(self, xData):
        """
        Pre: xData is the known data from the eval folder, a 2D list of mapped parameters
        Post: Returns a list containing the predicted sender of the email for 
              each doument in the eval folder
        """
        #Use skTree's predict function to make a prediction based on trained tree
        pred = self.tree.predict(xData)
        
        #Return the prediction
        return pred


def testSKTree():
    """
    Used to test my SKTree
    Predicts some random list of parameters
    """
    s = SKTree()

    knownX = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
    knownY = [1,2,3,4]

    unknownX = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

    s.train(knownX, knownY, 5)
    prediction = s.eval(unknownX)

    print(prediction)

if __name__ == "__main__":
    testSKTree()
