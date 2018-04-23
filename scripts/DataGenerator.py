import os
import random
import sys

from Util import *

if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    sys.stderr.write('Usage: python %s <number of rows>\n' % sys.argv[0])
    sys.exit()

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
        self._id = emailID
        self.firstName = firstName
        self.lastName = lastName
        self.paperIDs = []

    def csvStr(self):
        return '%s,%s,%s' % (self._id, self.firstName, self.lastName)

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
    def __init__(self, ID, topic, fileName, contactAuthorEmailID):
        self._id = ID
        self.topic = topic
        self.fileName = fileName
        self.authorEmailIDs = []
        self.contactAuthorEmailID = contactAuthorEmailID

    def csvStr(self):
        return '%s,%s,%s,%s' % (self._id, self.fileName, self.topic,
                                self.contactAuthorEmailID)

    def jsonStr(self):
        return json.dumps(self.__dict__)


IDs = list(range(1, NROWS + 1))
random.shuffle(IDs)
papers = []
for ID in IDs:
    topic = random.choice(TOPICS)
    fileName = '%s%s.%s' % (removeWhitespaces(topic), ID,
                            random.choice(EXTENSIONS))
    papers.append(Paper(ID, topic, fileName, None))

# Generate paper authorship information

authorships = []
for paper in papers:
    # Each paper requires 1 contact author
    contactAuthor = random.choice(authors)
    paper.contactAuthorEmailID = contactAuthor._id
    paper.authorEmailIDs.append(contactAuthor._id)
    contactAuthor.paperIDs.append(paper._id)
    authorships.append((contactAuthor._id, paper._id))

AUTHORSHIP_THRESHOLD = min(len(papers), 2)  # Minimum number of papers per author

for author in authors:
    while len(author.paperIDs) < AUTHORSHIP_THRESHOLD:
        paper = random.choice(papers)
        if not paper._id in author.paperIDs:
            # This author has not written this paper
            author.paperIDs.append(paper._id)
            paper.authorEmailIDs.append(author._id)
            authorships.append((author._id, paper._id))

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
