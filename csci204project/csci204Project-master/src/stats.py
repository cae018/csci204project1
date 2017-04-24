"""
This class will perform simple stats calcuations on our data
Most of these will be static methods
"""
from sort import *
from heap import *
from collections import *


class Stats:


    def __init__(self):
        pass

    @staticmethod
    def findFreqDic(aList):
        """
        Takes in a list of words, returns a dictionary of words/freq
        """
        #Code From CSCI 203 Project that made a freq Dict
        freqDict = {}
        
        #This goes through the word list and adds the key to the dict with
        #Value of 1 if it was not in freqDict, else it adds one to the value
        #of key.
        for x in range(len(aList)):
            word = aList[x]
            if word in freqDict:
                freqDict[word] += 1
            else:
                freqDict[word] = 1
        
        return freqDict
        

    @staticmethod
    def topNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the highest freq
        """
        #Using the collections libarary, sort the list based on the value
        #Since collections does not inheirintly create a dictionary,
        #return dict(TopNSortDic )
        topNSortDic = (sorted(aDic.items(), key = lambda t: t[1], reverse = True))
        topNSortDic = topNSortDic[:n]
        
        
        
        return dict(topNSortDic)
            
                

    @staticmethod
    def bottomNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the lowest freq
        """
        #Same idea as topNSortm however with reversed it will instead
        bottomNSortDic = (sorted(aDic.items(), key = lambda t: t[1]))
        bottomNSortDic = bottomNSortDic[:n]
        
        return dict(bottomNSortDic)


    @staticmethod
    def topNHeap(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the highest freq
        """
        pass

    
    @staticmethod
    def bottomNHeap(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the lowest freq
        """
        pass



def testStats():
    """
    Can be used to test methods in the Stats Class
    """
    test = Stats()
    unsortedDic = {'cat': 4, 'dog': 1, 'fox': 7, "quick": 5, 'the': 10}
    c = test.topNSort(unsortedDic, 3)
    #Should print {'the':10, 'fox': 7, 'quick': 5}
    print(c)
    d = test.bottomNSort(unsortedDic, 2)
    #Should print {'dog': 1, 'cat': 4}
    print(d)    
    
if __name__ == "__main__":
    testStats()
