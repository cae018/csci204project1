"""
Main Interface 
Requirements:  matplotlib, numpy, scipy, sci-kit
Recommended to use with anaconda (will have all packages)
"""

from util import *
from documentReader import *
from stats import *
#from plot import *
import os


def main():
    """
    Will call main loop of interface
    """
    user_interface()

def user_interface():
    """
    Will be used to interact with user
    """

    info = UserInput() #my main structure that holds my execution information

    print("----Welcome to Enron Data Analysis----")
    print("Goals: (1) Who wrote an email (2) Communication Network -- Who talked to who")
    
    ###User Enters full file path without quotes
    
    tpath = input("Please enter the filepath for the training data: ")
    info.tpath = tpath
    
    #If inputted tpath is invalid, ask again
    if os.path.basename(tpath) != 'phillip.allen@enron.com' and \
                       os.path.basename(tpath) != 'tana.jones@enron.com'and \
                       os.path.basename(tpath) != 'james.derrick@enron.com'and\
                       os.path.basename(tpath) != 'jeff.skilling@enron.com'and\
                       os.path.basename(tpath) != 'john.arnold@enron.com'and\
                       os.path.basename(tpath) != 'kenneth.lay@enron.com'and\
                       os.path.basename(tpath) != 'mark.taylor@enron.com'and\
                       os.path.basename(tpath) != 'richard.sanders@enron.com'and\
                       os.path.basename(tpath) != 'sally.beck@enron.com'and\
                       os.path.basename(tpath) != 'susan.scott@enron.com':
         print('Enter valid train path')
         tpath = input("Please enter the filepath for the training data: ")
         info.tpath = tpath
    
    print("Loading Training Documents")
    
    #FILL ME WITH CODE TO DO THIS, WRITE OUT IF SUCCESSFUL
    
    #Create empty list that will contain document objects
    docList1 = []
    #Find emails within directory
    for directory in os.listdir(tpath):
        joinPath = os.path.join(tpath, directory)
        #Find email files
        if os.path.isfile(joinPath): #is file not is dir
            #Get document object from file
            docObj = DocumentReader(joinPath)
            doc = docObj.readFile()
            #Add document to list
            docList1 += [doc]
            
    #info.tpath is set to the list of documents
    info.tpath = docList1
    
    #FILL ME WITH CODE TO DO THIS, WRITE OUT IF SUCCESSFUL
    
    ##Currently there is nothing, so skip this for now
    epath = input("Please enter the filepath for the unknown data: " )
    info.epath = epath
    print("Loading Eval Documents")


    #Find emails within directory
    #Create empty list that will contain document object
    
    docList2 = []
    for directory in os.listdir(epath):
        joinPath = os.path.join(epath, directory)
        #Find email files
        if os.path.isfile(joinPath): #is file not is dir
            #Get document object from file
            docObj = DocumentReader(joinPath)
            doc = docObj.readFile()
            #Add document to list
            docList2 += [doc]
    
            
    #info.epath is set to the list of documents
    info.epath = docList2
    
    #FILL ME... if everything is ok call the topMenu
    topMenu(info)
      

def topMenu(info):
    
    print("Enter Selection")
    print("1. Add Text Filter")
    print("2. Apply Text Filter")
    print("3. Topic Analyis of Train")
    print("4. Topic Analyis of Eval")
    print("5. Find UnKnown From")
    print("6. Find UnKnown To")
    print("7. Build Social Network Graph")
    t = int(input("?"))
    
    #FILL ME, test if t is ok, if not do something smart
    if t == 3:
        print(topicAnalysisTrain(info.tpath))
    elif t == 4:
        print(topicAnalysisEval(info.epath))
        
    #Checkpoint 2, only option 3 is available from menu
    else:
        print('\n')
        print('Try again. Currently only option 3 and 4 are available.')
        print('\n')
        topMenu(info)

def addTextFilter(info):
    """
    Add information about which text filters to use, see TextFilter class for details
    """
    print("Student to add")
    return None

def applyTextFilter(info):
    """
    Apply the text filter to both the training and eval Document Lists
    """
    print("Student to add")
    return None

def topicAnalysisTrain(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    Pre: info is a Document object made of Sentence objects
    Post: Checkpoint 2: most common and least common words are returned
    """
    exclude = set(('!', '.', '?'))
    freq = Stats()
    fullText = []
    #Parse emails
    for x in range(len(info)):
        for sentence in range(info[x].getSCount()):
            #Simplify emails into string of words separated by single space
            sString = info[x][sentence].lower()
            sString = ''.join(char for char in sString if char not in exclude)
            sString = sString.split()
            fullText = fullText + sString

    #Call findFreqDic() to find frequencies of words
    freqDict = freq.findFreqDic(fullText)

    #Ask user for number of words they want to analyze
    numTopic = int(input("Please enter number of words you want to analyze: "))
    
    #Find most and least common calling topNSort and bottomNSort
    mostCommon = freq.topNSort(freqDict, numTopic)
    leastCommon = freq.bottomNSort(freqDict, numTopic)
    
    #Code for graph
    
    return mostCommon, leastCommon


def topicAnalysisEval(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    Pre: info is a Document object made of Sentence objects
    Post: Checkpoint 2: most common and least common words are returned
    """
    print("Student to add")

    exclude = set(('!', '.', '?'))
    freq = Stats()
    fullText = []
    for x in range(len(info)):
        for sentence in range(info[x].getSCount()):
            #Simplify emails into string of words separated by single space
            sString = info[x][sentence].lower()
            sString = ''.join(char for char in sString if char not in exclude)
            sString = sString.split()
            fullText = fullText + sString

    #Call findFreqDic() to find frequencies of words
    freqDict = freq.findFreqDic(fullText)
    
    #Ask user for number of words they want to analyze
    numTopic = int(input("Please enter number of words: "))
    
    #Find most and least common calling topNSort and bottomNSort
    mostCommon = freq.topNSort(freqDict, numTopic)
    leastCommon = freq.bottomNSort(freqDict, numTopic)
    
    #Code for graphs
            
    return mostCommon, leastCommon

def findUnKnownFrom(info):
    """
    To be added (decision tree, pca, seq)
    """
    print("To be added")
    return None

def findUnKnownTo(info):
    """
    To be added (decision tree, pca, seq)
    """
    print("To be added")
    return None


def buildNetwork(info):
    """
    To be added (may or maynot get)
    """
    print("To be added")
    return None


if __name__ == "__main__":
    main()
