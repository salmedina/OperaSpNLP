import argparse
import os.path as osp
from glob import glob
from collections import defaultdict

import spacy
import neuralcoref


def main():
    docs_dir = '/home/zal/Devel/OperaSpNLP/docs'#args.docs_dir
    output_dir = '/home/zal/Devel/OperaSpNLP/output/spacy/pos'
    file_ext = 'txt' #args.docs_ext

    nlp = spacy.load('es_core_news_md')
    neuralcoref.add_to_pipe(nlp)

    pos_dict = defaultdict(list)

    for file_path in glob(osp.join(docs_dir, f'*.{file_ext}')):
        doc_text = open(file_path, 'r').read()
        doc = nlp(doc_text)
        for token in doc:
            pos_dict[token.pos_].append(token.text)

    for pos_tag in pos_dict.keys():
        print(f'{pos_tag}: {len(pos_dict[pos_tag])}')
        save_path = osp.join(output_dir, f'{pos_tag}.out')
        with open(save_path, 'w') as fout:
            fout.write('\n'.join([word for word in pos_dict[pos_tag]]))



if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('docs_dir', type=str, help='Directory with the documents to be processed')
    # parser.add_argument('docs_ext', type=str, default='txt', help='File extension of documents to be processed')
    # args = parser.parse_args()

    main()