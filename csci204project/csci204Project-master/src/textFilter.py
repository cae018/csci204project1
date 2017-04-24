"""
This class will filter the information inside a Document
and return a filtered (SAME) Document.
"""


from document import *
from sentence import *


class TextFilter:
    """
    Applies a list of filter to a document and returns same filtered Document
    """

    def __init__(self, filterList=None, doc=None):
        self.__filterList = filterList
        self.__doc = doc

    def setFilterList(self, filterList):
        """
        Set a list of filters
        """
        self.__filterList = filterList

    def setDoc(self, doc):
        """
        Set document that you're applying filters to
        """
        self.__doc = doc

    def apply(self, doc=None):
        """
        doc is the Document we are applying each filter in the filterlist to
        """
        #for each filter in the list, apply the filter
        for x in range(len(self.__filterList)):
            currFilter = self.__filterList[x]
            if currFilter == "normalizeWhiteSpace":
                self.normalizeWhiteSpace()
            elif currFilter == "normalizeCase":
                self.normalizeCase()
            elif currFilter == "stripNull":
                self.stripNull()
            elif currFilter == "stripNumbers":
                self.stripNumbers()
            elif currFilter == "stripFiles":
                self.stripFiles()
            else:
                #Raise exception if non-existent filter is applied
                raise TextFilterException('You entered an invalid filter')
            
        #Return the filtered document
        return doc

    def normalizeWhiteSpace(self):
        """
        Post: removes extra (meaning more than one character) white space
        from a document
        """
        doc = self.__doc
        sCount = doc.getSCount()
        #For each sentence in the document
        for sentence in range(sCount):
            currSentence = doc[sentence]
            #Split sentence into strings of non-whitespace characters
            #Join with a single white-space
            filtSen = ' '.join(currSentence.split())
            doc[sentence] = Sentence(filtSen)
        

    def normalizeCase(self):
        """
        Post: normalizes the characters in a document to lowercase
        """
        doc = self.__doc
        sCount = doc.getSCount()
        #For each sentence in the document
        for sentence in range(sCount):
            currSentence = doc[sentence]
            #use .lower() function to make all characters lowercase
            lowerCase = currSentence.lower()
            doc[sentence] = Sentence(lowerCase)
    
    def stripNull(self):
        """
        Post: strips all characters that are not numbers or letters from a document
        """
        doc = self.__doc
        sCount = doc.getSCount()
        #For each sentence in the document
        for sentence in range(sCount):
            currSentence = doc[sentence]
            #For each word in the sentence
            for word in currSentence:
                #For each character in the word
                for ch in word:
                    #If the character is not a number or a letter, get rid and join surrounding characters
                    if not ch.isalnum() and ch != ' ':
                        currSentence = currSentence.replace(ch, "")
            doc[sentence] = Sentence(currSentence)
            

    def stripNumbers(self):
        """
        Post: strips all characters that are numbers from a document
        """
        doc = self.__doc
        sCount = doc.getSCount()
        #For each sentence in the document
        for sentence in range(sCount):
            currSentence = doc[sentence]
            #Get rid of any character that is a number
            stripSen = ''.join(i for i in currSentence if not i.isdigit())
            doc[sentence] = Sentence(stripSen)

    def stripFiles(self):
        """
        Post: strips all words found in a given file (for now we have
        created a mock file holding some words to strip)
        """
        doc = self.__doc
        stripWords = [line.rstrip('\n') for line in open('wordstrip.txt')] 
        #stripWords = ['fight', 'october', 'delta']
        sCount = doc.getSCount()
        #For each sentence in the document
        for sentence in range(sCount):
            currSentence = doc[sentence]
            #For each word in the document
            for word in currSentence.split():
                #If the word is found in the wordstrip file, get rid of it
                if word in stripWords:
                    currSentence = currSentence.replace(word, "")
            doc[sentence] = Sentence(currSentence)

def testTestFilter():
    """
    Put your test for the filter class here
    """
    #Set up a mock document
    d = Document()
    #Set document's sentences
    d[0] = Sentence('This   is8 the first  98 delta  sentence4 in  my email　@')
    print('Original: ', d[0])

    #set up a list of filters
    testFList = ['normalizeCase','stripNull','stripNumbers', 'stripFiles','normalizeWhiteSpace']
    #apply filters
    test = TextFilter(testFList, d)
    test.apply(d)
    print('Filtered: ', d[0])



if __name__ == "__main__":
    testTestFilter()





