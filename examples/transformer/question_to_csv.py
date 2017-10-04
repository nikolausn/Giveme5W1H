import os
import csv
from extractor.tools.file.handler import Handler

# example, how to convert the extracted answers to csv file for further evaluation
# set the question here
question = 'how'
# number of included candidates
candidates = 3
# input files, usually the output directory of giveme5w
inputPath = os.path.dirname(__file__) + 'extracting/output'


# extracting
def get_parts_as_text(parts):
    answer_text = ''
    for part in parts:
        answer_text = answer_text + ' ' + part.get('text')
    return answer_text
output = []
documents = Handler(inputPath).preload_and_cache_documents().process().get_documents()

for document in documents:
    raw = document.get_rawData()
    answers = raw['fiveWoneH'][question]['extracted']
    if answers:
        counter = 0
        for candidate in answers:
            output.append([str(document.get_document_id()), raw.get('topics','noTopic'),str(candidate['score']), get_parts_as_text(candidate.get('parts'))])
            counter = counter + 1
            if counter == candidates:
                break

with open(os.path.dirname(__file__) + '/test.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for line in output:
        print(line)
        writer.writerow(line)


