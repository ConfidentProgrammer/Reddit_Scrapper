import praw
import json
from praw.models import MoreComments
reddit = praw.Reddit(
    client_id="GB_1L9TtC2j04awZCZOEYA",
    client_secret="It5GfDaaKYYgOHYDHMItVobuq3kNLw",
    password="Reddit@2618",
    user_agent="testscript by u/deepp2618",
    username="deepp2618",
)

class Scrape:
    def __init__(self, subReddit, keyWords):
        self.subReddit = subReddit
        self.keyWords = keyWords
    def start_Scraping(self):
        title = {}
        title['post'] = []
        #adding the name of subreddit to the api
        subreddit = reddit.subreddit(self.subReddit)
        # grabbing the posts for that subreddit limit is the 2000 posts for that keyword
        posts = subreddit.hot(limit = 2000)
        for post in posts:
            if isinstance(post, MoreComments):
                continue
            if self.keyWords in post.title:
               # print("->"+(post.title)+"\n")
               # print(subreddit)
                title['post'].append(post.title)
        return title
    def loadData(self):
        fileData = self.start_Scraping()
        with open('Data.json', 'w') as outputFile:
            json.dump(fileData, outputFile, indent=4)

                


secPlus = Scrape("Hacking_Tutorials+CompTIA+Cybersecurity+Hacking+HowToHack","Security+")
secPlus.loadData()




# subreddit = reddit.subreddit('hacking')
# print(reddit.user.me())


# posts = reddit.subreddit('Hacking_Tutorials+CompTIA').hot(limit = 1000)
# n=1
# keys = ["Hackers"]
# for post in posts:
#     if isinstance(post, MoreComments):
#         continue
#     if "Security+" in post.title:
#      print("->"+(post.title)+"\n")
#      n+=1
#      print(n)


# secPlus = Scrape("AccessCyber+apple+AskNetsec+BadApps+blackhat+blueteamsec+cissp+CompTIA+computerforensics+ComputerSecurity+Crypto+cyber+cyberlaws+cybersecurity+Cybersecurity101+CyberSecurityJobs+datarecovery+ethicalhacking+exploitdev+fulldisclosure+HackBloc+hackers+hackersec+hacking+Hacking_Tutorials+HowToHack+i2p+Information_Security+InfoSecNews+IOT+ISO27001+MacOS+macsysadmin+malware+msp+netsec+netsecstudents+NetworkSecurity+opendirectories+osx+privacy+pwned+redteamsec+regames+reverseengineering+SecurityCareerAdvice+securityCTF+TOR+websecurity+zeroday", "Security+")