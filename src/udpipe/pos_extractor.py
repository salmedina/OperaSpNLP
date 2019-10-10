import os.path as osp
from glob import glob
from collections import defaultdict
from unidecode import unidecode

import spacy_udpipe
import neuralcoref


def main():
    docs_dir = '/home/zal/Devel/OperaSpNLP/docs'
    output_dir = '/home/zal/Devel/OperaSpNLP/output/udpipe/pos'
    file_ext = 'txt'

    nlp = spacy_udpipe.load('es-ancora')
    neuralcoref.add_to_pipe(nlp)

    pos_dict = defaultdict(list)

    for file_path in glob(osp.join(docs_dir, f'*.{file_ext}')):
        doc_text = unidecode(open(file_path, 'r').read())
        doc = nlp(doc_text)
        for token in doc:
            pos_dict[token.pos_].append(token.text)

    for pos_tag in pos_dict.keys():
        print(f'{pos_tag}: {len(pos_dict[pos_tag])}')
        save_path = osp.join(output_dir, f'{pos_tag}.out')
        with open(save_path, 'w') as fout:
            fout.write('\n'.join([word for word in pos_dict[pos_tag]]))



if __name__ == '__main__':

    main()