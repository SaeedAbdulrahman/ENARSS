import feedparser
import bcolors
import time
import os

os.system('clear')
updated = ''

def LoadRSS():
    global NewsFeed
    NewsFeed = feedparser.parse("https://wam.ae/en/rss/emirates")

while True:
    LoadRSS()
    if updated == NewsFeed['feed']['updated']:
        print(bcolors.ERR + "No updates" + bcolors.ENDC)
    else:
        print(bcolors.OK + "Updated Feed" + bcolors.ENDC)
    entries = len(NewsFeed['entries'])
    updated = NewsFeed['feed']['updated']
    print(updated)
    for entry in range(0, entries):
        print(bcolors.HEADER + NewsFeed['entries'][entry]['title'] + bcolors.ENDC)
        print(bcolors.WARN + NewsFeed['entries'][entry]['summary'] + bcolors.ENDC)
        print(bcolors.UNDERLINE + NewsFeed['entries'][entry]['link'] + bcolors.ENDC)
        print("\n")
        time.sleep(3)
