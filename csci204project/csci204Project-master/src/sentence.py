"""
A primary data-structure.
Document will keep a list of these.
A Sentence is NOT a line.
"""

class Sentence:

    def __init__(self, sString = ""):
        self.__sString = sString
        self.__wCount = -1
        self.__endP = "" #Ending puncuation
        
    def getWCount(self):
        """
        Pre: A Sentence() is being acted upon
        Post: The word count of the given sentence is returned
        """
        sentence = self.__sString
        self.__wCount = 0
        for i in range(len(sentence)):
            #If the current index is a letter and the next index is not
            #add one to the word count
            if str.isalpha(sentence[i-1]) is True and str.isalpha(sentence[i]) is False:
                self.__wCount += 1
        return self.__wCount

    def getSString(self):
        """Return the sentence that is being held
        """
        return self.__sString


    def setSString(self, value):
        """Pre: value is a string, a sentence
           Post: The Sentence() data is set as the given value
        """
        self.__sString = value

    def getEndP(self):
        """Pre: A Sentence() is being acted upon
           Post: The ending puctuation of the sentence ('.', '?', '!') is returned
        """
        #Dont know if this getter is needed but may be helpful
        sentence = self.getSString()
        for i in range(len(sentence)):
            if sentence[i] == '.' or sentence[i] == '!' or sentence[i] == '?':
                self.__endP = sentence[i]
            else:
                self.__endP == ""
        return self.__endP

def testSentence():
    """
    Used to test your Sentence class
    """
    s = Sentence('')
    s.setSString('This is a sentence!')
    print('Test sentence getter: ' , s.getSString())
    print('Test getWCount(): ', s.getWCount())
    print('Test getEndP(): ', s.getEndP())


if __name__ == "__main__":
    testSentence()

    
