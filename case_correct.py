import re
import sys
from corenlp_pywrap import pywrap
cn = pywrap.CoreNLP(url='http://localhost:9000', annotator_list=['truecase'])

def print_clean(line):
    line = line.lower()
    out = cn.basic(line, out_format='json')
    normalized_sent = [token['truecaseText'] for token in out.json()['sentences'][0]['tokens']]
    pretty_string = re.sub(" (?=[\.,'!?:;])", "", ' '.join(normalized_sent))
    print(pretty_string)

f = open(sys.argv[1],"r")
contents = f.readlines()
[print_clean(x) for x in contents]
f.close()
