"""
Class used to read a document.
Each document will be product by one instance of a DocumentReader

IF DATA IS MISSING, will be noted at ??? in the file 
"""

#Will be used when we find an exceptions
from userExceptions import *
#All documents contain multiple sentences
from sentence import *
#Will produce a document
from document import *
from userExceptions import * #Import exceptions
import os #Import os to parse folders/files
import datetime

class DocumentReader:
    """
    Used to read in a document
    """
    
    def __init__(self, fname = ""):
        """Pre: fname is one of the files in the train directory, is a string
           Post: self.__fname is set, self.__fileRef is set given fname
        """
        self.__fname = fname
        self.__fileRef = None #Will store the reference to file when open
    
    def getFName(self, fname):
        """Pre: fname is a file in the train directory
           Post: the full path of fname is returned
        """
        return self.__fname
    
    def __openFile(self):
        """
        Private function used to open the file and test if it exists
        """
        try:
            doc = open(self.__fname, "r")
            self.__fileRef = doc
        except OurInFileException:
            print("There was a problem when attempting to open the file.")
        return doc
        
    
    def readFile(self):
        """
        Will open (if not already open)/read the file
        Make a Document and return
        If any Error, throws error
        Format of file is MIME EMAIL
        """
        
        doc = self.__openFile() #Get opened file from __openFile()
        readDoc = doc.read() #Read document contents

        #Get body of doc excluding forwarded/original messages
        #Get start of message
        for i in range(len(readDoc)):
            if readDoc[i:i+13] == '\nX-FileName: ':
                index = i+13
                message1 = readDoc[index:]
        for j in range(len(message1)):
            if message1[j:j+2] == '\n\n':
                index = j+2
                message2 = message1[index:]
                break
        #Get message excluding forwarded or original message
        for k in range(len(message2)):
            if message2[k:k+4] == '----' or message2[k:k+3] == '\n\n\n\n':
                index = k
                mesFinal = message2[:k]
                break
            else:
                mesFinal = message2
                
        #Get sentences from Body of Message (mesFinal)
        #sentences holds info for self.__sentences
        sentences = []
        startIndex = 0
        #Loops through words in mesFinal to extract sentence
        for i in range(len(mesFinal)):
            if mesFinal[i] == '.' or mesFinal[i] == '!' or mesFinal[i] == '?':
                sentences += [Sentence(mesFinal[startIndex : i+1])]
                startIndex = i + 1

        #Get from email info
        #fromInfo holds info needed for __fromInfo
        fromInfo = os.path.basename(os.path.dirname(self.__fname))

        #Get to email info
        #toEmail holds info needed for __toInfo
        #Loops through email to find ToInfo
        for i in range(len(readDoc)):
            if readDoc[i:i+5] == '\nTo: ':
                index = i+5
                toInfo = ''
                for j in range(len(readDoc) - index):
                    if readDoc[index + j] == ',' or readDoc[index + j] == '\n'\
                       or readDoc[index + j] == '/':
                        break
                    else:
                        toInfo += readDoc[index + j]

        #Get date
        #day, month, year holds info needed for .__date attribute
        for i in range(len(readDoc)):
            if readDoc[i:i+6] == 'Date: ':
                
                dayIndex = i+6 + 5 #Account for the Mon, Tue, etc. in front of date
                day = '' #set up string to hold day
                month = '' #month
                year = '' #year
                
                #Find day
                for j in range(len(readDoc)):
                    if readDoc[dayIndex + j].isspace():
                        moIndex = dayIndex + j + 1
                        break
                    else:
                        day += readDoc[dayIndex + j]
                        
                #Find month
                for j in range(len(readDoc)):
                    if readDoc[moIndex + j].isspace():
                        yrIndex = moIndex + j + 1
                        break
                    else:
                        month += readDoc[moIndex + j]
                        
                #Find year
                for j in range(len(readDoc)):
                    if readDoc[yrIndex + j].isspace():
                        break
                    else:
                        year += readDoc[yrIndex + j]
                        
                #Convert to integers
                day = int(day)
                year = int(year)
                #Convert month (string) to integer
                monthWord = str.lower(month)
                posMonths = ['jan','feb','mar', 'apr','may','jun','jul','aug','sep','oct','nov','dec']
                month = 0
                for i in range(len(posMonths)):
                    if posMonths[i] == monthWord:
                        month = i+1

        #Create document, adding info found above
        docRead = Document(toInfo, fromInfo)
        docRead.setDate(year, month, day)
        for i in range(len(sentences)):
            docRead[i] = sentences[i]

        #return created document
        return docRead

    def checkFileFormat():
        """
        Will open the file (if not already open)
        Will test if it is a correctly formatted MIME EMAIL
        """
        if self.__fileRef == None:
            self.__openFile()
        if ("Mime-Version: 1.0" in self.__fileRef.read()) == False:
            raise OurInFileException
        else:
            return True



def testDocumentReader():
    """
    Used to test your DocumentReader class
    """
    file = '/Users/carolineedelman/Desktop/csci204project/csci204Project-master/train/phillip.allen@enron.com/3'
    d = DocumentReader(file).readFile()
    print('Body of Email:')
    for i in range(d.getSCount()):
        print(d[i])
    print('\n')
    print('Date of email (year, month, day): ', d.getDate())
    print('\n')
    print('Email recipient: ', d.getToInfo())
    print('\n')
    print('Email sender: ', d.getFromInfo())
    
if __name__ == "__main__":
    testDocumentReader()
