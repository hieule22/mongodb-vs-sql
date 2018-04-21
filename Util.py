# List of helpful procedures for the project.

import json
import random

def readFile(path):
    lines = []
    with open(path) as f:
        for line in f:
            lines.append(line.strip())
    return lines

def writeFile(entities, path):
    with open(path, 'w') as f:
        for entity in entities:
            f.write(str(entity) + '\n')

def parseDomains(inFile, outFile):
    domains = []

    with open(inFile, 'r', encoding='utf-8') as f:
        jsonData = json.loads(f.read())
        for school in jsonData:
            for domain in school['domains']:
                domains.append(domain)
    
    with open(outFile, 'w') as f:
        for domain in domains:
            f.write(domain + '\n')

def randChoice(seq, n):
    """Randomly select n distinct elements from a sequence"""
    choices = set()
    while len(choices) < n:
        choices.add(random.randint(0, len(seq) - 1))
    return [seq[i] for i in choices]
