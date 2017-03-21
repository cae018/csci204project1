"""
This file contains objects related to our plotting
"""


import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class MyPlot:
    """
    This class will be used for all plotting.
    In most cases, the functions will just be static
    However, this allows for on nice interface
    """

    def __init__(self):
        """
        constructor
        """
        pass


    @staticmethod
    def twoDScatter(xList, yList, xLabels=None, yLabels=None):
        #Get x and y values
        y = yList
        x = xList
        width = 25
        plt.scatter(x, y, width, color="blue")
        
        fig = plt.gcf()
        #Make axis labels
        plt.xlabel(xLabels)
        plt.ylabel(yLabels)
    
        #Produce graph
        plt.tight_layout()
        plt.show()


    @staticmethod
    def twoDBar(xList, yList, xLabels=None, yLabels=None):
        #Get x and y values
        y = yList
        x = xList
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        
        
        fig = plt.gcf()
        #Make axis labels
        plt.xlabel(xLabels)
        plt.ylabel(yLabels)
    
        #Produce grap
        plt.tight_layout()
        plt.show()





def testMyPlot():
    """
    Used to test MyPlot class
    """
    d = MyPlot
    d.twoDBar([5,3,4,9],[10,4,5,8],"X-axis","Y-Axis")
    d.twoDScatter([5,3,4,9],[10,4,5,8],"X-axis","Y-Axis")


if __name__ == "__main__":
    testMyPlot()


