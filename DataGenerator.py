import random
from Util import *

FIRST_NAMES = readFile('data/first-names.txt')
LAST_NAMES = readFile('data/last-names.txt')
UNIVERSITY_DOMAINS = readFile('data/university-domains.txt')
TOPICS = readFile('data/topics.txt')
EXTENSIONS = readFile('data/extensions.txt')

NUM_AUTHORS = 100
NUM_PAPERS = 100

# Generate author information
class Author:
    def __init__(self, emailID, firstName, lastName):
        self.emailID = emailID
        self.firstName = firstName
        self.lastName = lastName
        self.paperIDs = []

    def csvStr(self):
        return '%s,%s,%s' % (self.emailID, self.firstName, self.lastName)

    def jsonStr(self):
        return json.dumps(self.__dict__)

authors = []

for i in range(NUM_AUTHORS):
    firstName = random.choice(FIRST_NAMES)
    lastName = random.choice(LAST_NAMES)
    emailID = '%s%s%d@%s' % (firstName.lower(), lastName.lower(), i,
                           random.choice(UNIVERSITY_DOMAINS).lower())
    authors.append(Author(emailID, firstName, lastName))
    
# Generate paper information
class Paper:
    def __init__(self, ID, topic, fileName):
        self.ID = ID
        self.topic = topic
        self.fileName = fileName
        self.authorIDs = []

    def csvStr(self):
        return '%s,%s,%s' % (self.ID, self.fileName, self.topic)

    def jsonStr(self):
        return json.dumps(self.__dict__)


IDs = list(range(1, NUM_PAPERS + 1))
random.shuffle(IDs)
papers = []
for ID in IDs:
    topic = random.choice(TOPICS)
    fileName = '%s%s.%s' % (topic.replace(' ', ''), ID, random.choice(EXTENSIONS))
    papers.append(Paper(ID, topic, fileName))

# Generate paper authorship information
authorships = []
for paper in papers:
    for author in randChoice(authors, 2):
        paper.authorIDs.append(author.emailID)
        author.paperIDs.append(paper.ID)
        authorships.append((author.emailID, paper.ID))

for author in authors:
    for paper in randChoice(papers, 2):
        if not paper.ID in author.paperIDs:  # This author has not written this paper
            author.paperIDs.append(paper.ID)
            paper.authorIDs.append(author.emailID)
            authorships.append((author.emailID, paper.ID))

# Output to file
writeFile([author.csvStr() for author in authors], 'genfiles/authors.csv')
writeFile([author.jsonStr() for author in authors], 'genfiles/authors.json')
writeFile([paper.csvStr() for paper in papers], 'genfiles/papers.csv')
writeFile([paper.jsonStr() for paper in papers], 'genfiles/papers.json')
writeFile(['%s,%s' % authorship for authorship in authorships], 'genfiles/authorships.csv')
