"""
Main Interface 
Requirements:  matplotlib, numpy, scipy, sci-kit
Recommended to use with anaconda (will have all packages)
"""

from util import UserInput
from documentReader import DocumentReader
from stats import *
#from plot import *
import os
from skTree import SKTree
from textFilter import TextFilter


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
    
    #tpath = input("Please enter the filepath for the training data: ")
    tpath = '/Users/carolineedelman/Desktop/csci204Project-master/train'
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
                       os.path.basename(tpath) != 'susan.scott@enron.com' and\
                       os.path.basename(tpath) != 'train':
         print('Enter valid train path')
         tpath = input("Please enter the filepath for the training data: ")
         info.tpath = tpath

    print("Loading Training Documents")
    
    #Find emails within train directory
    for email in os.listdir(tpath):
        if email != '.DS_Store':
            joinEmail = os.path.join(tpath,email)
            for directory in os.listdir(joinEmail):
                joinPath = os.path.join(joinEmail, directory)
                #Find email files
                if os.path.isfile(joinPath): #is file not is dir
                    #Get document object from file
                    docObj = DocumentReader(joinPath)
                    doc = docObj.readFile()
                    #Add document to list
                    info.addTDocument(doc)
            
    #Now info.__tDocuments is set to the list of documents
    
    #epath = input("Please enter the filepath for the unknown data: " )
    epath = '/Users/carolineedelman/Desktop/csci204Project-master/eval/UnKnown'
    
    info.epath = epath
    
    if os.path.basename(epath) != 'UnKnown':
        print('Enter valid eval path')
        epath = input("Please enter the filepath for the unknown data: ")
        info.epath = epath
        
    print("Loading Eval Documents")
    
    #Find email docs within eval directory
    for directory in os.listdir(epath):
        joinPath = os.path.join(epath, directory)
        #Find email files
        if os.path.isfile(joinPath): #is file not is dir
            #Get document object from file
            docObj = DocumentReader(joinPath)
            doc = docObj.readFile()
            #Add document to list
            info.addEDocument(doc)
            
    #Now info.__eDocuments is set to the list of documents
    
    #FILL ME... if everything is ok call the topMenu
    topMenu(info)
      

def topMenu(info):
    #Get train and eval documents for use
    trainDocs = info.getTDocument()
    evalDocs = info.getEDocument()
    
    print("Enter Selection")
    print("1. Add Text Filter")
    print("2. Apply Text Filter")
    print("3. Topic Analyis of Train")
    print("4. Topic Analyis of Eval")
    print("5. Find UnKnown From")
    print("6. Find UnKnown To")
    print("7. Build Social Network Graph")
    print("8. Predict SKTree")
    print("9. Exit")
    t = int(input("?"))
    
    #FILL ME, test if t is ok, if not do something smart
    if t == 1:
        #Call addTextFilter
        addTextFilter(info)
    elif t == 2:
        #Apply the filters that have been added
        applyTextFilter(info)
    elif t == 3:
        print(topicAnalysisTrain(trainDocs))
    elif t == 4:
        print(topicAnalysisEval(evalDocs))
    elif t == 8:
        predictSKTree(info)
    elif t == 9:
        return
        
    #Checkpoint 3, only option 1, 2, 3, 4, 8, 9 are available from menu
    else:
        print('\n')
        print('Try again. Options 5, 6, and 7 are currently unavailable.')
        print('\n')
        topMenu(info)

def addTextFilter(info):
    """
    Add information about which text filters to use, see TextFilter class for details
    """
    #Ask user for filter, must be of the form of the functions in textFilter.py
    addFilter = input('What filter would you like to add? ')
    #Add the given filter to the list of filters
    info.setTextFilter(str(addFilter))
    #Return to menu, can add more filters if you want or can apply filters
    topMenu(info)

def applyTextFilter(info):
    """
    Apply the text filter to both the training and eval Document Lists
    """
    #Set which filters have been added from addTextFilter()
    textFilter = TextFilter(info.getTextFilter())
    #Get tpath documents
    trainDocs = info.getTDocument()
    #Get epath documents
    evalDocs = info.getEDocument()
    
    #For each document in train, apply the filters
    for i in range(len(trainDocs)):
        doc = trainDocs[i]
        #Set current document
        textFilter.setDoc(doc)
        #Apply filter
        textFilter.apply()
        
    #Test a random document
    #for i in range(trainDocs[1].getSCount()):
        #print(trainDocs[1][i])
        
    #For each document in eval, apply the filters
    for j in range(len(evalDocs)):
        doc = evalDocs[j]
        #Set current document
        textFilter.setDoc(doc)
        #Apply filter
        textFilter.apply()
        

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

def predictSKTree(info):
    """
    Pre: info object contains is the documents read from the train and
         eval folder
    Post: information from the train emails will be used
          to predict who sent emails in the eval folder
    """
    #Separate the training and eval documents
    trainDocs = info.getTDocument()
    evalDocs = info.getEDocument()
    
    #Create 1D and 2D lists to hold numeric info
    #2DL[0] contains the info for which cell contains what data
    train2DL = []
    eval2DL = []
    
    #1D list containing from map info. Filled with 0 for eval
    train1DL = []
    eval1DL = []
    
    maxDepth = 0
    #Get numeric info for train docs, compile 2D lists
    for doc in range(len(trainDocs)):
        train2DL += [trainDocs[doc].mapParameters()]
        train1DL += [trainDocs[doc].fromMap()]
        maxDepth += 1
    
    #Get numeric info for eval docs
    for doc in range(len(evalDocs)):
        eval2DL += [evalDocs[doc].mapParameters()]
        eval1DL += [0]
        
    #Create an skTree class
    skTree = SKTree()
    #Train the data, create a tree
    skTree.train(train2DL, train1DL, maxDepth)
    #Predict the data
    predict = skTree.eval(eval2DL)
    
    #map of from emails
    fromEmails = ['james.derrick@enron.com','jeff.skilling@enron.com','john.arnold@enron.com',\
                  'kenneth.lay@enron.com','mark.taylor@enron.com','phillip.allen@enron.com',\
                  'richard.sanders@enron.com','sally.beck@enron.com','susan.scott@enron.com',\
                  'tana.jones@enron.com']
    
    #Convert numerical representation of prediction to email names
    #Print the predicted sender of the eval emails
    count = 0
    for directory in os.listdir(info.epath):
        print('Email ', directory , ' in eval folder is from ', fromEmails[predict[count]-1])
        count += 1

    #Return the predicted list of fromInfo for the eval folder
    return predict

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
