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
import email

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
        message = email.message_from_string(readDoc) #Get message object from string

        #Get the body of the message
        mBody = message.get_payload()
        mBody = mBody.split()
        #Split the message into a list of each word
        sentences = []
        curSent = ""
        fwd = 0
        #This loop checks each word in the list that was
        #created and pieces together a single sentence object
        for word in mBody:
            if "." in word or "?" in word or "!" in word:
                curSent = curSent + word
                sentences.append(Sentence(curSent)) #Make sentence object
                curSent = ""
            elif "Forwarded" in word or "Original" in word:
                fwd = 1
                break
            else:
                curSent = curSent + word + " "

        #Get from email info
        #fromInfo holds info needed for __fromInfo
        fromInfo = os.path.basename(os.path.dirname(self.__fname))

        #Get toInfo holds info needed for __toInfo
        toInfo = ''
        emails = message['To']
        #If for some reason message['To'] is none, resort to parsing email
        #by way of indices
        if message['To'] == None:
            for i in range(len(readDoc)):
                if readDoc[i:i+6] == 'X-To: ':
                    index = i+6
                    toInfo = ''
                    for j in range(len(readDoc) - index):
                        if readDoc[index + j] == ',' or readDoc[index + j] == '\n'\
                           or readDoc[index + j] == '/':
                            break
                        else:
                            toInfo += readDoc[index + j]
        #Else get the To info normally
        else:
            for char in emails:
                if char == ",":
                    break
                toInfo += char

        #Get date
        fullDate = message['Date']
        #Because this is the full date, it must be changed into only day, month, year
        fullDate = fullDate.split()
        #Since we only want three values, and the format
        #Is always the same with MIME, the values
        #can be obtained by taking values 1-4
        #and joining them
        fullDate = fullDate[1:4]
        #Reverse the list because it is not in the format that is needed for the document
        fullDate = fullDate[::-1]
        fullDate = "".join(fullDate)
        
        #From fullDate, get integers for day, month, year in order to use date object
        #Get year
        year = int(fullDate[0:4])
        month = fullDate[4:7]
        #Convert month to an integer
        monthWord = str.lower(month)
        posMonths = ['jan','feb','mar', 'apr','may','jun','jul','aug','sep','oct','nov','dec']
        month = 0
        for i in range(len(posMonths)):
            if posMonths[i] == monthWord:
                month = i+1
        #Get day
        day = int(fullDate[7:])

        #Get the subject and check if Re: in subject
        subject = message['Subject']
        if "Re:" in subject:
            reply = 1
        else:
            reply = 0


        numSentences = len(sentences)
        #Create document, adding info found above
        docRead = Document(toInfo, fromInfo)
        docRead.setDate(year, month, day)

        docRead.setFwd(fwd)
        docRead.setReply(reply)
        
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
    file = '/Users/carolineedelman/Desktop/csci204Project-master/train/phillip.allen@enron.com/411'
    
    d = DocumentReader(file).readFile()
    print(doc.mapParameters())
    print('Original Body of Email:')
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
