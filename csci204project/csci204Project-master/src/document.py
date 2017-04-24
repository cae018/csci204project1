"""
Class that will contain a document (Basic unit -- "Primary Data-Structure)
"""

from util import *
from sentence import *
import datetime
from userExceptions import * #Import exceptions
from stats import *
import os


class Document:
    
    def __init__(self, toInfo = None, fromInfo = None, date=None):
        self.__sentences = []
        self.__sCount = -1 #Number of sentences
        self.__toInfo = toInfo #Who was the document to
        self.__fromInfo = fromInfo #Who was the document from
        self.__date = date
        self.__fwd = False
        self.__reply = False


    def __getitem__(self, index):
        """Pre: Index is an integer
           Post: returns the sentence containted in the document at the given index
        """
        return self.__sentences[index].getSString()

    def __setitem__(self, index, value):
        """Pre: Index is an integer, Value is a Sentence object
           Post: self[index] is set to be the inputted value
        """
        try:
            self.__sentences[index] == None
            self.__sentences[index] = value
        except:
            if isinstance(value, Sentence) is True:
                self.__sentences = self.__sentences + [None]
                self.__sentences[index] = value
            else:
                 raise OurInFileException('Inputted value is not a sentence object')

    def getSCount(self):
        """Pre: A nonempty Document() is being acted upon
           Post: The number of sentences in the document is returned
        """
        #fill me (we should not have to ever set sCount)
        return len(self.__sentences)

    def setToInfo(self, value):
        """Pre: Value is a name or email, a string
           Post: self.__toInfo is set to given value
        """
        #fill me
        self.__toInfo = value

    def getToInfo(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the receiver is returned
        """
        #fill me
        return self.__toInfo

    def setFromInfo(self, value):
        """Pre: Value is a name or email, a string
           Post: self.__fromInfo is set to given value
        """
        #fill me
        self.__fromInfo = value

    def getFromInfo(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the sender is returned
        """
        #fill me
        return self.__fromInfo
    
    
    def setDate(self, year, month, day):
        """Pre: Year, month, day are all integers
           Post: self.__date is set utilizing datetime package
        """
        #should use date object in python datetime package
        mydate = datetime.date(year, month, day)
        #fill me
        self.__date = mydate

    def getDate(self):
        """Pre: A Document() is being acted upon
           Post: the date of the document is returned (Year, Month, Day)
        """
        #returns year,month,day
        return self.__date.year, self.__date.month, self.__date.day


    def setFwd(self, value):
        """Pre: Value is a name or email, a string
           Post: self.__fwd is set to given value
        """
        #fill me 
        self.__fwd = value

    def getFwd(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the forwarder is returned
        """
        #fill me
        return self.__fwd

    def setReply(self,value):
        """Pre: Value is a name or email, a string
           Post: self.__reply is set to given value
        """
        #fill me
        self.__reply = value
    
    def getReply(self):
        """Pre: A Document() is being acted upon
           Post: the information (name or email) of the replier is returned
        """
        #fill me 
        return self.__reply

    def checkDate(self):
        """
        Pre: document with date attribute
        Post: convert date to integer in mmddyyyy
        Utilized to map data to integers for decision tree
        """
        day = str(self.getDate()[2])
        if day < '10':
            day = '0' + day
        month = str(self.getDate()[1])
        if month < '10':
            month = '0' + month
        date = month + day + str(self.getDate()[0])
        
        return date

    def toMap(self):
        '''Pre: Email document
           Post: returns the numerical mapping of the to information
                 obtains to info from a txt file. If the to info exists
                 already, that numerical value is returned, if not the to info
                 is added to the file and is assigned a numerical value
        '''
        #Get the to information from the email
        toInfo = self.getToInfo()
        
        #Get path name from whatever system we are on
        #MapTo.txt is organized so one line has the actual email and the
        #following line has the mapping
        mapFileBase = 'MapTo.txt'
        mapFile = os.getcwd()
        mapFile = os.path.dirname(mapFile)
        mapFile = os.path.join(mapFile, mapFileBase)
        
        openMap = open(mapFile, 'r')
        #Read the information in the map file
        readMap = openMap.read().split('\n')
        openMap.close() #close file

        lastNum = int(readMap[-1]) + 1

        toNum = None

        for i in range(len(readMap)):
            #If our to info exists, get the corresponding integer
            if toInfo == readMap[i]:
                toNum = readMap[i+1] #Get the map
                return int(toNum)
                
        #If the to info does not yet exists in the map, add it
        if toNum is None:
            openMap = open(mapFile, 'a+')
            openMap.write('\n' + toInfo + '\n' + str(lastNum))
            openMap.close()
            return lastNum

    def fromMap(self):
        '''Pre: email document from train file
           Post: returns a numerical value that is arbtrarily assigned to the
                 from information
        '''
        fromIn = self.__fromInfo
        if fromIn == 'james.derrick@enron.com':
            return 1
        elif fromIn == 'jeff.skilling@enron.com':
            return 2
        elif fromIn == 'john.arnold@enron.com':
            return 3
        elif fromIn == 'kenneth.lay@enron.com':
            return 4
        elif fromIn == 'mark.taylor@enron.com':
            return 5
        elif fromIn == 'phillip.allen@enron.com':
            return 6
        elif fromIn == 'richard.sanders@enron.com':
            return 7
        elif fromIn == 'sally.beck@enron.com':
            return 8
        elif fromIn == 'susan.scott@enron.com':
            return 9
        elif fromIn == 'tana.jones@enron.com':
            return 10

    def commonWords(self):
        """
        We will analyze topics based on words in the email
        We will prompt the user for how many topics "words" they are looking for
        After we will find this information and plot it using our Plot class
        Pre: info is a Document object made of Sentence objects
        Post: Checkpoint 2: most common and least common words are returned
        """
        #utilize similar code used in stats.py
        exclude = set(('!', '.', '?'))
        freq = Stats()
        fullText = []
        #Parse email
        for x in range(self.getSCount()):
            #Simplify email into string of words separated by single space
            sString = self[x].lower()
            sString = ''.join(char for char in sString if char not in exclude)
            sString = sString.split()
            fullText = fullText + sString

        #Call findFreqDic() to find frequencies of words
        freqDict = freq.findFreqDic(fullText)

        #Analyze 10 words
        numTopic = 10
        
        #Find most and least common calling topNSort and bottomNSort
        mostCommon = freq.topNSort(freqDict, numTopic)
        leastCommon = freq.bottomNSort(freqDict, numTopic)
        
        most = list(mostCommon.keys())
        least = list(leastCommon.keys())
        
        return most, least
        
    def mapParameters(self):
        """
        Pre: A Document being acted upon
        Post: A numerical list of parameters required for making decision tree
        """
        #The order for input of the list will be
        #[date, to, forward, reply, top10, bott10]
        parameterL = []
        
        #Map the date parameter
        date = self.checkDate()
        parameterL.append(int(date))
        
        #Map the to info parameter
        to = self.toMap()
        parameterL.append(to)

        #Check to see if a reply occured - 0 if not, 1 if so
        reply = self.getReply()
        parameterL.append(reply)

        #Check to see if a forward occured - 0 if not, 1 if so
        fwd = self.getFwd()
        parameterL.append(fwd)

        top10, bott10 = self.commonWords()
        #If top10 or bot10 words exist, map to 1. If not, map to 0
        if len(top10) == 10:
            parameterL.append(1)
        else:
            parameterL.append(0)

        if len(bott10) == 10:
            parameterL.append(1)
        else:
            parameterL.append(0)
        return parameterL
        
def testDocument():
    """
    Used to test your Document Class
    """
    #Set up a mock document
    d = Document()
    #Set document's sentences
    d[0] = Sentence('This is the first sentence in my email.')
    d[1] = Sentence('This is the second sentence in my email!')
    d[2] = Sentence('Sincerely, last sentence')
    
    #Get document's setences
    print(d[0])
    print(d[1])
    print(d[2])
    #Test getSCount()
    print('self.__sCount should be 3: ', d.getSCount())
    #Set toInfo
    d.setToInfo('friend@gmail.com')
    #Get toInfo
    print('To Info: ', d.getToInfo())
    #Set fromInfo
    d.setFromInfo('me@work.org')
    #Get fromInfo
    print('From Info: ', d.getFromInfo())
    #Set Date
    d.setDate(2017, 3, 6)
    #Get Date
    print('(Year, Month, Day): ', d.getDate())
    #Get Fwd
    d.setFwd('forward@gmail.com')
    #Set Fwd
    print('Forward Info: ', d.getFwd())
    #Set Reply
    d.setReply('reply@gmail.com')
    #Get Reply
    print('Reply Info: ', d.getReply())

    
if __name__ == "__main__":
    testDocument()





    
