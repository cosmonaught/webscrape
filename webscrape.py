#simple webscraper program TOTALLY NOT COMPLETE OR ANYTHING JUST THE CURRENT CODE I HAVE WRITTEN I NEEDED TO GET PUT UP
from BeautifulSoup import BeautifulSoup, SoupStrainer
import webbrowser
import requests
import re
import urllib2

#establishing the while loop
while True:
    print('Please name the website you wish to scrape for information, or q to quit')
    webName = input()
    if webName == 'q' #break function for the program
        break
    else: 
        print('please input the key term that you wish to search for, or q to quit')
        keyTerm = input()
        if keyTerm == 'q'
            break #break function again 
        else: #found core code on stackoverflow, editing to use the way I need it to work. 
            doc = urllib2.urlopen(str(webName)).read()
            links = SoupStrainer('a', href=re.compile(keyTerm))
            soup = [str(elm) for elm in BeautifulSoup(doc, parseOnlyThese=links)]
            for elm in soup:
                print elm
            #not sure if I want to print it out in the console or if I want to print into the console 
