'''
Class: COMP 1405Z

Title: Course Project (searchdata.py)
Name: Karan Patel
Student ID: 101218041
'''
import os
import math

#name of the directory with all data
dataDir = "data"

#function to get the mapping index given the url
def get_mapping_index(URL):
    index = None
    mappingFile = open(os.path.join(dataDir, "mapping.txt"), "r")
    #loop for all lines in mappingFile
    for line in mappingFile:
        #mappingFile lines are in the form "index,URL" so we can split the line and compare it to the given URL
        if URL == line[line.find(',') + 1 : line.find('\n')]:
            #if there is a match save the mapping index and break
            index =  line[0 : line.find(',')]
            break

    mappingFile.close()
    return index

#function to get url given the mapping index
def get_url(index):
    url = None
    mappingFile = open(os.path.join(dataDir, "mapping.txt"), "r")
    #loop for all lines in mappingFile
    for line in mappingFile:
        #mappingFile lines are in the form "index,URL" so we can split the line and compare it to the given index
        if str(index) == line[0 : line.find(',')]:
            #if there is a match save the url and break
            url = line[line.find(',') + 1 : line.find('\n')]
            break

    mappingFile.close()
    return url

#function to get the title of the url given the mapping index
def get_title(index):
    #titles are stored in the titles directory in the form index.txt --content--> title
    titleFile = open(os.path.join(dataDir, "titles", str(index) + ".txt"), "r")
    #read the first line and return it
    title = titleFile.readline()
    titleFile.close()
    return title

#function to get the outgoing links of the url given the url
def get_outgoing_links(URL):
    #use the get_mapping_index to convert given URL to mapping index
    index = get_mapping_index(URL)
    #if the mapping index returns None there is no such URL in the crawled data
    if index == None:
        return None

    #outgoing Links are stored in the outgoing_links directory in the form index.txt --content--> multiple "outgoingLinks,index" seperated by "/n"
    outgoingLinkFile = open(os.path.join(dataDir, "outgoing_links", str(index) + ".txt"), "r")
    outgoingLinkList = []
    #loop for all lines in outgoingLinkFile
    for line in outgoingLinkFile:
        #return the links from each line by spliting the line
        outgoingLinkList.append(line[0 : line.rfind(',')])
    outgoingLinkFile.close()
    #return the list of outgoingLinks
    return outgoingLinkList

#function to get the incoming links of the url given the url
def get_incoming_links(URL):
    #use the get_mapping_index to convert given URL to mapping index
    index = get_mapping_index(URL)
    #if the mapping index returns None there is no such URL in the crawled data
    if index == None:
        return None

    #incoming Links are stored in the incoming_links directory in the form index.txt --content--> multiple "incominglink" seperated by "/n"
    incomingLinkFile = open(os.path.join(dataDir, "incoming_links", str(index) + ".txt"), "r")
    #we can split the file by the \n to create a list of incoming links
    incomingLinkList = incomingLinkFile.read().split('\n')
    #the last element in the list will always be a empty space so we can pop it
    incomingLinkList.pop()
    incomingLinkFile.close()
    #return list of incoming links
    return incomingLinkList

#function to get the pageRank of a URL given the url
def get_page_rank(URL):
    #use the get_mapping_index to convert given URL to mapping index
    index = get_mapping_index(URL)
    #if the mapping index returns -1 there is no such URL in the crawled data
    if index == None:
        return -1

    #PageRank values are stored in the page_rank directory in the form index.txt --content--> PageRank values
    pageRankFilePath = os.path.join(dataDir,"page_rank", str(index) + ".txt")

    #if file exists return the value
    if os.path.isfile(pageRankFilePath):
        pageRankFile = open(pageRankFilePath, "r")
        return float(pageRankFile.readline().strip())
    #else return -1 Note this will never happen because all indexs have a value
    return -1

#function to get the pageRank of a URL given the mapping index
def get_page_rank_by_index(index):
    #PageRank values are stored in the page_rank directory in the form index.txt --content--> PageRank values
    pageRankFilePath = os.path.join(dataDir,"page_rank", str(index) + ".txt")

    #if file exists return the value
    if os.path.isfile(pageRankFilePath):
        pageRankFile = open(pageRankFilePath, "r")
        return float(pageRankFile.readline().strip())
    #else return -1 Note this will never happen because all indexs have a value
    return -1

#function to get the idf value of a word given the word
def get_idf(word):
    #idf Values are stored in the idf directory in the form index.txt --content--> idf Value
    idfFilesPath = os.path.join(dataDir, "idf", word + ".txt")
    #if the word has a idf value return it otherwise return 0
    if os.path.isfile(idfFilesPath):
        wordFile = open(idfFilesPath, "r")
        wordIdf = wordFile.readline()
        wordFile.close()
        return float(wordIdf)
    return 0

#function to get the tf value of a word and url given the word and url
def get_tf(URL, word):
    #use the get_mapping_index to convert given URL to mapping index
    index = get_mapping_index(URL)
    #tf Values are stored in the tf directory in the form word_index.txt --content--> tf Value
    tfFilesPath = os.path.join(dataDir, "tf", word + "_" + str(index) + ".txt")
    #if the URL and word has a tf value return it otherwise return 0
    if os.path.isfile(tfFilesPath):
        wordFile = open(tfFilesPath, "r")
        wordTf = wordFile.readline()
        wordFile.close()
        return float(wordTf)
    return 0

#function to get the tfidf value of a word and url given the word and url
def get_tf_idf(URL, word):
    #use the get_mapping_index to convert given URL to mapping index
    index = get_mapping_index(URL)
    #tfIdf Values are stored in the tf directory in the form word_index.txt --content--> tfIdf Value
    tfIdfFilesPath = os.path.join(dataDir, "tf_idf", word + "_" + str(index) + ".txt")
    #if the URL and word has a tfIdf value return it otherwise return 0
    if os.path.isfile(tfIdfFilesPath):
        wordFile = open(os.path.join(tfIdfFilesPath), "r")
        wordTfIdf = wordFile.readline()
        wordFile.close()
        return float(wordTfIdf)
    return 0

#function to get the largest element in the list given the list
def largestValue(list):
    maxValueIndex = 0
    for i in range(len(list)-1):
        if list[i+1] > list[maxValueIndex]:
            maxValueIndex = i+1
    return maxValueIndex
