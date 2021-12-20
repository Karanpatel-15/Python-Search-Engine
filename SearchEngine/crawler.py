'''
Class: COMP 1405Z

Title: Course Project (crawler.py)
Name: Karan Patel
Student ID: 101218041
'''

import os
from webdev import *
import math
import matmult

#name of the directory where all data will be stored
dataDir = "data"

#queue that represents the pages that need to be crawled next
#queue will be multidimensional where queue[i][0] are urls and queue[i][1] is the urls mapping index
queue = []

#queue that stores the pages that already have been crawled
#same multidimensional concept as queue
completedQueue = []

#counter for the number of pages starting from the seed
totalPages = 0

#dictionary of all unique Words where key = word and values = word frequency
uniqueWords = {}
#dictionary of all unique Words where key = word and values = number of pages the word appears in
pagesWithUniqueWords = {}

#preset using instructions given
alpha = 0.1

#function responsible for crawling the web starting from the given seed
def crawl(seed):
    global queue, completedQueue, totalPages

    #reset all data if there is a pre-exsiting dataDir
    if os.path.isdir(dataDir):
        delDir(dataDir)

    #setup directories structure for dataDir
    setup()

    #The seed will always be the first page meaning it will have the mapping index of 0
    #the seed still needs to be crawled so it will be added to the queue
    queue.append([seed,'0'])

    #loop till all of the pages in queue have been crawled (i.e. queue is empty)
    while(len(queue) != 0):

        #split queue leader compenents into index and currentUrl
        currentUrl = queue[0][0]
        index = queue[0][1]

        #store index and currentUrl into the mapping file
        mapURL(index, currentUrl)

        #store HTML content into the currentHtmlContent string
        currentHtmlContent = read_url(currentUrl)

        #find the title of page between <title> and </title> tages and store it using saveTitle function
        title = currentHtmlContent[currentHtmlContent.find('<title>') + 7 : currentHtmlContent.find('</title>')].strip()
        saveTitle(title, index)

        #function to save all text from the page and to calculate/store the Tf values
        saveTextsAndTf(currentHtmlContent, index)

        #find all links in page using saveOutgoingAndIncomingLink function
        saveOutgoingAndIncomingLink(currentUrl, currentHtmlContent, index)

        #remove queueLeader from queue and add it to completedQueue
        completedQueue.append(queue.pop(0))

    #total pages will be offset by 1 becasue we added the seed to the queue from the start, so we need to add 1
    totalPages += 1

    #function to store/calculate Idf values and TfIdf values
    saveIdfAndTfIdf()

    #function to store/calculate pageRank
    pageRank()

    #store totalPages in totalPagesFile.txt file for search.py
    totalPagesFile = open(os.path.join(dataDir, "totalPages.txt"), "w")
    totalPagesFile.write(str(totalPages))
    totalPagesFile.close()

    return totalPages

#function is to recursively delete the given directory
def delDir(directory):
    #loop for all elements in given directory
    for element in os.listdir(directory):
        #update current path
        currentPath = os.path.join(directory, element)
        #if the currentPath links to a file delete the file
        if os.path.isfile(currentPath):
            os.remove(currentPath)
        #if the currentPath links to a directory recursively call the delDir function
        else:
            delDir(currentPath)
    #when the function reaches here the directory will be empty so it can be deleted
    os.rmdir(directory)

#function to create directory the structure
def setup():
    os.makedirs(dataDir)
    os.makedirs(os.path.join(dataDir, 'titles'))
    os.makedirs(os.path.join(dataDir, 'texts'))
    os.makedirs(os.path.join(dataDir, 'incoming_links'))
    os.makedirs(os.path.join(dataDir, 'outgoing_links'))
    os.makedirs(os.path.join(dataDir, 'tf'))
    os.makedirs(os.path.join(dataDir, 'idf'))
    os.makedirs(os.path.join(dataDir, 'tf_idf'))
    os.makedirs(os.path.join(dataDir, 'page_rank'))

#function to store mapping of all url and index in mapping.txt file
def mapURL(index, URL):
    #mapping will be stored in the mapping.txt file in the form "index,URL"
    mappingFile = open(os.path.join(dataDir, "mapping.txt"), "a")
    mappingFile.write(index + "," + URL + "\n")
    mappingFile.close()

#function to save title in titles directory using the form index.txt --content--> title
def saveTitle(title, index):
    titleFile = open(os.path.join(dataDir, "titles", str(index) + ".txt"), "w")
    titleFile.write(title)
    titleFile.close()

#function to save text in texts directory using the form index.txt --content--> text and call termFrequency function
def saveTextsAndTf(htmlContent, index):
    #split the htmlContent using paragraph starter tag ex. [...,<p>....,<p>.....,<p>.....]
    textList = htmlContent.split("<p>")
    #since the htmlContent using paragraph starter tag the first element will have no useful information
    textList.pop(0)
    combinedTexts = None

    #loop for all elements in textList
    for i in range(len(textList)):
        strText = textList[i]
        #find ending paragraph tag in textList[i] and remove anything past and including the tag, this will get rid of any information inbetween paragraph tags
        strText = strText[0 : strText.rfind('</p>')].strip()

        #this part is to combine the texts. combinedTexts will be used for the Tf calculation
        if combinedTexts == None:
            combinedTexts = strText
        else:
            combinedTexts = combinedTexts + "\n" + strText

    #call the termFrequency function and replace all spaces in combinedTexts with '\n'
    termFrequency(combinedTexts.replace(' ', '\n'), index)

#function to store all outgoing links and call the saveIncomingLink function
def saveOutgoingAndIncomingLink(currentUrl, htmlContent, index):
    global queue
    global totalPages
    #find absoulte path minus the relative link
    path = currentUrl[0:currentUrl.rfind('/')].strip()

    #stores all links in list by spliting text using tag <a href=".
    outgoingLinkList = htmlContent.split("<a href=\"")
    #first element of the list will consist of all text from begining to first <a href=". tag, therefore we dont need it
    outgoingLinkList.pop(0)
    outgoingLinkFile = open(os.path.join(dataDir, "outgoing_links", str(index) + ".txt"), "w")

    #loop for all elements in outgoingLinkList
    for i in range(len(outgoingLinkList)):
        strElement = outgoingLinkList[i]
        #if the href link starts with http:// then strip it from index 0 to '\">'
        if(strElement.startswith("http://")):
            absPath = strElement[0 : strElement.find('\">')].strip()
        else:
            #otherwise strip it from index 1 (to avoid '.' as it is a realtive path) to '\">'
            absPath = path + strElement[1 : strElement.find('\">')].strip()

        # check if URL is not in queue using existInQueue function then then add it
        if not existInQueue(queue,absPath) and not existInQueue(completedQueue,absPath):
            #this means the url is new so we need to add the totalPages by 1 and add url to queue
            totalPages += 1
            queue.append([absPath, str(totalPages)])

        #add absPath to outgoingLinkFile
        outgoingLinkFile.write(absPath + "," + str(findIndexInQueue(absPath)) + "\n")

        #Find index for URL
        index = findIndexInQueue(absPath)
        #Save incoming link
        saveIncomingLink(index, currentUrl)
    outgoingLinkFile.close()

#function to check if the given url is in the given queue
def existInQueue(queue, url):
    #loop for all element in queue
    for element in queue:
        #if the url matches the element return true
        if element[0] == url:
            return True
    return False

#function to store the incoming links
def saveIncomingLink(index, URL):
    incomingFile = open(os.path.join(dataDir, "incoming_links", str(index) + ".txt"), "a")
    incomingFile.write(URL + "\n")
    incomingFile.close()

#function to find the index of the given url in either queue
def findIndexInQueue(url):
    #if url is in the queue return index
    for element in queue:
        if element[0] == url:
            return element[1]
    #if url is in the completedQueue return index
    for element in completedQueue:
        if element[0] == url:
            return element[1]
    return None

#function to store Tf values, update uniqueWords and update pagesWithUniqueWords[word]
def termFrequency(text, index):
    #split all words by \n
    textList = text.split('\n')
    #textLenght is the total words in textList
    textLenght = len(textList)
    #differentWordCount is a local dictorory for all words in the given text where key = word and value = word frequency
    differentWordCount = {}
    #loop for every word in textList
    for word in textList:
        #if word is already in differentWordCount add one to the frequency and also add one to the uniqueWords dictionary
        if word in differentWordCount:
            differentWordCount[word] += 1
            uniqueWords[word] += 1
        else:
            #if not already in differentWordCount, initialize the word with frequency one
            differentWordCount[word] = 1
            #since this is the first occurrence of the word on this page there is a chance the word is not in uniqueWord we need to check
            if word not in uniqueWords:
                #sinces its a new word set the word in uniqueWords with the frequency one
                uniqueWords[word] = 1
                #sinces it is a new word set the word in uniqueWords with the frequency one
                pagesWithUniqueWords[word] = 1
            else:
                #if the word has already been initialized but is new to the page add one too uniqueWords and pagesWithUniqueWords
                uniqueWords[word] += 1
                pagesWithUniqueWords[word] += 1

    #for all words in differentWordCount create a file in the tf directory in the form "word_index.txt" --content--> termFrequency of word
    for word in differentWordCount:
        tfFile = open(os.path.join(dataDir, "tf", word + "_" + str(index) + ".txt"), "w")
        #termFrequency of word is calculted using frequency of words divided by total words
        tfFile.write(str(differentWordCount[word]/textLenght))
        tfFile.close()

#function to store/calculate Idf values and TfIdf values
def saveIdfAndTfIdf():
    #loop for all word in uniqueWords
    for word in uniqueWords:
        #Create a file in the idf directory in the form "word.txt" --content--> Idf value of the word
        idfFile = open(os.path.join(dataDir,"idf", word + ".txt"), "w")
        idf = str(math.log( ( totalPages / (1+pagesWithUniqueWords[word]) ) , (2) ))
        idfFile.write(idf)
        idfFile.close()
        #loop for all pages
        for i in range(totalPages):
            #find the path of the tf file for the index i and word in uniqueWords
            tfFileName = os.path.join(dataDir,"tf", word + "_" + str(i) + ".txt")
            #if there is such a file calculate and store the TfIdf values in the tf_idf directory
            if os.path.isfile(tfFileName):
                tfFile = open(tfFileName, "r")
                tfIdfFile = open(os.path.join(dataDir,"tf_idf", word + "_" + str(i) + ".txt"), "w")
                tfIdfFile.write(str(math.log(1+float(tfFile.readline().strip()), 2) * float(idf)))
                tfIdfFile.close()
                tfFile.close()

#function to calculate the page rank
def pageRank():
    #initialize the adjacencyMatrix with all 0's where rows and colunm numbers repersent the mapping index
    adjacencyMatrix = [[0.0]*(totalPages) for i in range(totalPages)]

    #loop for all files in outgoing_links directory
    for file in os.listdir(os.path.join(dataDir, 'outgoing_links')):
        outgoingLinkFile = open(os.path.join(dataDir, 'outgoing_links', file), "r")
        #set file name(mapping index) to row
        row = int(file[0:file.find('.')])
        #loop for all lines in outgoingLinkFile
        for line in outgoingLinkFile:
            #outgoingLinkFile lines are in the form "URL,index" therefore we can find the index and set it to column
            column = int(line[line.rfind(',')+1:line.rfind('\n')])
            #since we found the outgoing link set it to 1
            adjacencyMatrix[row][column] = 1

        outgoingLinkFile.close()

    #loop for all elements in the adjacencyMatrix
    for row in range(totalPages):
        #count all the number of ones in the row
        onesInRow = adjacencyMatrix[row].count(1)
        #loop for all coulums in the row
        for column in range(len(adjacencyMatrix[row])):
            #update adjacencyMatrix by deviding all the ones by number of ones in the row, then scale by 1-alpha then add alpha/totalPages
            adjacencyMatrix[row][column] = (adjacencyMatrix[row][column]/onesInRow)*(1-alpha)+(alpha/totalPages)

    #initialize previousIterations list with every element = 1/totalPages, this will make all elements of previousIterations added equal to 1
    previousIterations = [[]]
    for i in range(totalPages):
        previousIterations[0].append(1/totalPages)

    #multiply previousIterations by adjacencyMatrix matrix to get currentIterations
    currentIterations = matmult.mult_matrix(previousIterations, adjacencyMatrix)

    #loop till euclidean distance of previousIterations and currentIterations is >= 0.0001
    while matmult.euclidean_dist(previousIterations, currentIterations) >= 0.0001:
        previousIterations = currentIterations
        #multiply previousIterations by adjacencyMatrix matrix to get currentIterations
        currentIterations = matmult.mult_matrix(previousIterations, adjacencyMatrix)

    #PageRank values are stored in the page_rank directory in the form index.txt --content--> PageRank values
    for i in range(len(currentIterations[0])):
        pageRankFile = open(os.path.join(dataDir,"page_rank", str(i) + ".txt"), "w")
        pageRankFile.write(str(currentIterations[0][i]))
        pageRankFile.close()
