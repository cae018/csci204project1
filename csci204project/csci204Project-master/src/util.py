"""
This file will contain utility classes and functions
"""


class UserInput:
    """
    Class that will keep a record of user inputs
    """
    def __init__(self):
        self.tPath = ""
        self.ePath = ""
        self.__tDocument = [] #A List of training documents
        self.__eDocument = [] #A List of evaluation documents
        self.__textFilter = [] #A List of text filters

    def setTDocument(self, docList):
        """
        Set a list of training documents
        """
        self.__eDocument = docList

    def addTDocument(self, doc):
        """
        Add a training document
        """
        self.__tDocument += [doc]

    def getTDocument(self):
        """
        Returns the training document list
        """
        return self.__tDocument

    def setEDocument(self, docList):
        """
        Set a list of eval documents
        """
        self.__eDocument = docList


    def addEDocument(self, doc):
        """
        Add an eval document
        """
        self.__eDocument += [doc]
        
    def getEDocument(self):
        """
        Returns the eval document list
        """
        return self.__eDocument

    def setTextFilter(self, filter):
        self.__textFilter += [filter]
    
    def getTextFilter(self):
        return self.__textFilter
        


class TimerStats:
    """
    This class may be used to keep information on performance of your code
    """
    
    def __init__(self):
        pass
