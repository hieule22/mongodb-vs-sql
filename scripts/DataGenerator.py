import os
import random
import sys

from Util import *

# The repository directory is the parent directory of the directory containing
# this script.
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(REPO_DIR, 'data')
GENFILES_DIR = os.path.join(REPO_DIR, 'genfiles')

FIRST_NAMES = readFile(os.path.join(DATA_DIR, 'first-names.txt'))
LAST_NAMES = readFile(os.path.join(DATA_DIR, 'last-names.txt'))
UNIVERSITY_DOMAINS = readFile(os.path.join(DATA_DIR, 'university-domains.txt'))
TOPICS = readFile(os.path.join(DATA_DIR, 'topics.txt'))
EXTENSIONS = readFile(os.path.join(DATA_DIR, 'extensions.txt'))

NROWS = int(sys.argv[1])

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

for i in range(NROWS):
    firstName = random.choice(FIRST_NAMES)
    lastName = random.choice(LAST_NAMES)
    # Email has the form <first name><last name><index>@<university domain>
    # where index is used to uniquely identify the email.
    emailID = '%s%s%d@%s' % (firstName.lower(), lastName.lower(), i,
                           random.choice(UNIVERSITY_DOMAINS).lower())
    authors.append(Author(emailID, firstName, lastName))

random.shuffle(authors)  # Shuffle to avoid ascending index values
    
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


IDs = list(range(1, NROWS + 1))
random.shuffle(IDs)
papers = []
for ID in IDs:
    topic = random.choice(TOPICS)
    fileName = '%s%s.%s' % (removeWhitespaces(topic), ID,
                            random.choice(EXTENSIONS))
    papers.append(Paper(ID, topic, fileName))

# Generate paper authorship information

AUTHORSHIP_RATIO = 2  # Minimum number of authors per paper and vice versa

authorships = []
for paper in papers:
    for author in randChoice(authors, min(AUTHORSHIP_RATIO, len(authors))):
        paper.authorIDs.append(author.emailID)
        author.paperIDs.append(paper.ID)
        authorships.append((author.emailID, paper.ID))

for author in authors:
    for paper in randChoice(papers, min(AUTHORSHIP_RATIO, len(papers))):
        if not paper.ID in author.paperIDs:
            # This author has not written this paper
            author.paperIDs.append(paper.ID)
            paper.authorIDs.append(author.emailID)
            authorships.append((author.emailID, paper.ID))

# Output to file
writeFile([author.csvStr() for author in authors],
          os.path.join(GENFILES_DIR, 'authors.csv'))
writeFile([author.jsonStr() for author in authors],
          os.path.join(GENFILES_DIR, 'authors.json'))
writeFile([paper.csvStr() for paper in papers],
          os.path.join(GENFILES_DIR, 'papers.csv'))
writeFile([paper.jsonStr() for paper in papers],
          os.path.join(GENFILES_DIR, 'papers.json'))
writeFile(['%s,%s' % authorship for authorship in authorships],
          os.path.join(GENFILES_DIR, 'authorships.csv'))
