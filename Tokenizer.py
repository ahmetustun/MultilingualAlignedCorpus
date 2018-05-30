from nltk.tokenize import sent_tokenize
import nltk.data
import codecs

str = codecs.open("pt-br/orj_raw/DaveTroy_2014U.pt-br.txt", encoding='utf-8').read()

#tokenizer = nltk.data.load('ru/russian.pickle')
#sent_tokenize_list = tokenizer.tokenize(str)
sent_tokenize_list = sent_tokenize(str, language="spanish")

f = codecs.open('pt-br/sen_tkn/DaveTroy_2014U.pt-br.txt', 'w', encoding='utf-8')

for sent in sent_tokenize_list:
    print(sent)
    if not sent in ['\n', '\r\n', ' ']:
        f.write(sent+'\n')

f.close()