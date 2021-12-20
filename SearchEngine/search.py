'''
Class: COMP 1405Z

Title: Course Project (search.py)
Name: Karan Patel
Student ID: 101218041
'''
import math
import searchdata
import os
import time
#name of the directory with all data
dataDir = "data"

#function to respond to search queries
def search(phrase, boost):
    #split the given phrase by spaces to get a list of words
    phraseList = phrase.split()
    phraseWords = len(phraseList)
    #uniquePhraseWordsVector will be a list of phrase words without duplicates
    uniquePhraseWordsVector = []
    uniqueWords = 0
    queryVector = []

    #loop for all words in phraseList
    for word in phraseList:
        #if the word is already in the uniquePhraseWordsVector there is a duplicate so we shouldn't add it to the queryVector
        if word in uniquePhraseWordsVector:
            continue
        #add new word to uniquePhraseWordsVector and increase counter by 1
        uniquePhraseWordsVector.append(word)
        uniqueWords += 1
        #use the formula given to calculate queryVector elements and add it to the queryVector
        queryVector.append(math.log( 1+( phraseList.count(word)/phraseWords), (2) ) * searchdata.get_idf(word) )

    #read the totalPages.txt to get the total pages
    totalPagesFile = open(os.path.join(dataDir, "totalPages.txt"), "r")
    totalPages = int(totalPagesFile.readline())
    totalPagesFile.close()

    pageVector = []

    #loop for all pages in totalPages
    for i in range(totalPages):
        #initialize the pageVector will 0
        pageVectorinitializer = []
        for w in range(uniqueWords):
            pageVectorinitializer.append(0)
        pageVector.append(pageVectorinitializer)

        #loop for all words in uniqueWords
        for j in range(uniqueWords):
            tfIdfPath = os.path.join(dataDir, "tf_idf", uniquePhraseWordsVector[j] + "_" + str(i) + ".txt")
            #if there is a TfIdf File for that path then set page vector to the tfIdf value
            if os.path.isfile(tfIdfPath):
                tfIdfFile = open(tfIdfPath, "r")
                pageVector[i][j] = float(tfIdfFile.readline())
                tfIdfFile.close()

    cosineSimilarity = []
    #loop for all pages
    for page in range(totalPages):
        #reset calculations
        numerator = 0
        leftDenom = 0
        rightDenom = 0
        #loop for all elements in queryVector
        for i in range(len(queryVector)):
            #calculate values and add to total
            numerator += queryVector[i]*pageVector[page][i]
            leftDenom += queryVector[i]**2
            rightDenom += pageVector[page][i]**2
        #if there is a 0 / 0 case set cosineSimilarity to 0
        if leftDenom*rightDenom == 0:
            cosineSimilarity.append(0)
        #is boost is true multiply by page rank value
        elif boost == True:
            cosineSimilarity.append((numerator/(math.sqrt(leftDenom)*math.sqrt(rightDenom)))*searchdata.get_page_rank_by_index(page))
        #otherwise just set the cosineSimilarity
        else:
            cosineSimilarity.append(numerator/(math.sqrt(leftDenom)*math.sqrt(rightDenom)))

    rankedList = []
    #loop 10 times as thats the number of results we wannt
    for i in range(0, 10):
        #find the index with the largest cosineSimilarity
        index = searchdata.largestValue(cosineSimilarity)
        #create a dictionary with required information
        rankedList.append({'url': searchdata.get_url(index), 'title': searchdata.get_title(index), 'score': cosineSimilarity[index]})
        #set the largest cosineSimilarity index to -1 so it cant appear again
        cosineSimilarity[index] = -1

    return rankedList
