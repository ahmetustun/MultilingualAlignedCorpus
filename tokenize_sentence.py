import codecs
import argparse
from sentence_splitter import SentenceSplitter

parser = argparse.ArgumentParser(description='Sentence Tokenizer')

parser.add_argument("--inputfile", type=str, default='', help="Input file")
parser.add_argument("--outputfile", type=str, default='', help="Output file")
parser.add_argument("--language", type=str, default='en', help='Language')

params, _ = parser.parse_known_args()

input = codecs.open(params.inputfile, mode='r', encoding='utf-8').read()
output = codecs.open(params.outputfile, mode='w', encoding='utf-8')
#
# Object interface
#
splitter = SentenceSplitter(language=params.language)

for sent in splitter.split(text=input):
    if not sent in ['\n', '\r\n', ' ', '']:
        # print(sent)
        output.write(sent+'\n')

output.close()
