# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:49:10 2021

@author: Cihang
"""

class SentimentLexicon:    
    def __init__(self):
        self.dictionary = {}    #an instance variable initialised in the constructor that is a dictionary
        
    def makerecord(self):
        pathNega = input("please input the file path of negative word:")    #import negative-words.txt
        with open(pathNega, "r") as fileNega:
            readNega = fileNega.read()   #read the file of negative words
            Nega =  readNega.split('\n')    #split the file and each word in a line would be a string item in the list"Nega"
            for key in Nega[31:]:    #skip the fisrt 30 line of notes
                self.dictionary[key] = -1     #for each negative word as a key, its value is -1
        
        pathPosi = input("please input the file path of posiive word:")     #import positive-words.txt
        with open(pathPosi, "r") as filePosi:   #read the file of positive words
           readPosi = filePosi.read()   #same as negative
           Posi =  readPosi.split('\n')
           for key in Posi[30:]:
               self.dictionary[key] = 1     
            
    
class Classifier:
    def __init__(self, sl):     #The instance variable for Classifier is an instantiated SentimentLexicon object
        self.sl = sl
        
    def classify(self, text):
        self.text = text    #for this classify method, there should be a text for it to process
        lexicon = self.sl.dictionary    #self.sl is the SentimentLexicon object, the dictionary is its attribute which was defined in class SentimentLexicon
        words = text.split()    #split the text to a list of single words 
        score = 0
        for word in words:      #use for loop to look up every word's value in the text
            if word in lexicon:
                score = score + lexicon[word]   #lexicon[word] will return the value of the key in the dictionary
        if score > 0:
            finalscore = 1      ##If overall the score is positive, a value of 1 should be returned
        elif score < 0:
            finalscore = -1     #If overall the score is negative, a value of -1 should be returned
        else:
            finalscore = 0
        return(finalscore)      #after running this function, the final score would be returned

print("input main() to start")
def main():
    sl = SentimentLexicon()     #creates a SentimentLexicon object
    sl.makerecord()    #call the makerecord method to create the dictionary inside the SentimentLexicon object
    clf = Classifier(sl)    #creates a Classifier object, and the SentimentLexicon object is its instance variable
    text = ["I love Python.", "Python is the language I love!","The iPhone is clearly not the most terrible and worst phone ever. It is the best."]
    for t in text:
        result = {"text": t, "sentiment": clf.classify(t)}      
        #clf.classify(t) means call the classify method in the clf object, to process the strings in the list of text
        print(result)
 

    
