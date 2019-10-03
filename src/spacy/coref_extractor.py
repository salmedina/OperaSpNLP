import argparse
import os.path as osp
from glob import glob
from collections import defaultdict

import spacy
import neuralcoref


def main():
    docs_dir = '/home/zal/Devel/OperaSpNLP/docs'#args.docs_dir
    output_dir = '/home/zal/Devel/OperaSpNLP/output/spacy/coref'
    file_ext = 'txt' #args.docs_ext

    nlp = spacy.load('es_core_news_md')
    neuralcoref.add_to_pipe(nlp)

    entity_dict = defaultdict(list)

    for file_path in glob(osp.join(docs_dir, f'*.{file_ext}')):
        doc_text = open(file_path, 'r').read()
        doc = nlp(doc_text)
        print(f'{file_path}======================================================')
        print(doc._.coref_clusters)
        print(f'=================================================================')


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('docs_dir', type=str, help='Directory with the documents to be processed')
    # parser.add_argument('docs_ext', type=str, default='txt', help='File extension of documents to be processed')
    # args = parser.parse_args()

    main()