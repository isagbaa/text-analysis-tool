from random_username.generate import generate_username
from nltk.tokenize import sent_tokenize, word_tokenize
import re
#welcome message
def welcomeuser():
    print("\n welcome to my Okj text analysis tool.")
def getusername():
    maxattempts=3
    attempts=0

    while attempts < maxattempts:

        inputprompt = ""
        if attempts==0 :
           inputprompt = ("\n Enter your username:\n ")
        else :
           inputprompt = ("\n try again:\n ")
        usernamefrominput = input(inputprompt)
        
        #validate username
        if  len(usernamefrominput) < 5  or not usernamefrominput.isidentifier():  #if username is less than 5 characters or not a valid identifier
         print("Your Username must be at least 5 characters long,alphanumeric only, (A-Z/a-z/0-9) and have no space and cannot start with a number.")
        else :
            return usernamefrominput  #return valid username
        attempts += 1  #increment attempts
   
    
    print("\nExhuasted"+ str(maxattempts) +" attempts,Assigned username instead...." ) #display assigned username
    
    return generate_username()[0] #return generated username

    
      
    
    
def greeting(name):
    print("hello " + name + ", let's get started!")
\
#code starts here
 #displays welcome message check the function above
#print("Please enter your username:") #print message
#username input
# saves the resullt of getusername function to username variable
#personalized greeting


#get text from file
def getArticleText():
    f = open("files/article.txt", "r") #open the file in read mode
    rawtext =f.read() #print the content of the file
    f.close() #close the file
    return rawtext.replace("\n", " " ). replace("\r", " " ) #return the text with newlines replaced by spaces

#extract sentences from the text body 
def tokenizesentences(rawtext):     
    return sent_tokenize(rawtext) #tokenize the text into sentences using sent_tokenize function from nltk
   
   # extract words from list of sentences 
def tokenizewords(sentences):
   words = []
   for sentence in sentences:
       words.extend(word_tokenize(sentence)) #tokenize each sentence into words and add to the words list
   return words #return the list of words



def extractkeysentences(sentences , searchpattern):
    matchedsentences = []
    for sentence in sentences:
         #if matches desired pattern add to matchedsentences list
        

         if  re.search(searchpattern, sentence.lower()): #search for the pattern in the sentence using re.search function
             matchedsentences.append(sentence)
    return matchedsentences

#get user details and welcome them
welcomeuser()
username = getusername()
greeting(username)

#extract and tokenize article text
articleTextraw = getArticleText() #get article text from function
articlesentences = tokenizesentences(articleTextraw) #tokenize the article text into sentences
articlewords = tokenizewords(articlesentences)

stocksearchpattern = "[0-9] | [%$€£] |thousand|million|billion|trillion|profit|loss"
keysentences = extractkeysentences(articlesentences , stocksearchpattern)

#print for testing purposes
print("GOT: ")
print (keysentences)

