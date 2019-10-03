import argparse
import os.path as osp
from glob import glob
from collections import defaultdict

import nltk
from nltk import pos_tag
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

def process_text(raw_text):
    token_text = word_tokenize(raw_text)
    return token_text


def stanford_tagger(token_text):
    st = StanfordNERTagger(model_filename='/home/zal/Devel/OperaSpNLP/res/spanish.ancora.distsim.s512.crf.ser.gz',
                           path_to_jar='/home/zal/Devel/OperaSpNLP/res/stanford-ner.jar')
    ne_tagged = st.tag(token_text)
    return(ne_tagged)


def nltk_tagger(token_text):
    tagged_words = nltk.pos_tag(token_text)
    ne_tagged = nltk.ne_chunk(tagged_words)
    return(ne_tagged)


def count_and_tuple(input_list):
    count_dict = defaultdict(int)

    for item in input_list:
        count_dict[item] += 1
    return sorted([(key, count_dict[key])for key in count_dict.keys()], key=lambda x: x[1], reverse=True)


def print_count_tuple(count_tuple):
    for text, count in count_tuple:
        print(f'{text}: {count}')


def save_count_tuple(count_tuple, save_path):
    with open(save_path, 'w') as fout:
        fout.write('\n'.join([f'{text}: {count}' for text, count in count_tuple]))


def main():
    docs_dir = '/home/zal/Devel/OperaSpNLP/docs'#args.docs_dir
    output_dir = '/home/zal/Devel/OperaSpNLP/output/stanfordnlp/ner'
    file_ext = 'txt' #args.docs_ext

    entity_dict = defaultdict(list)

    for file_path in glob(osp.join(docs_dir, f'*.{file_ext}')):
        doc_text = open(file_path, 'r').read()

        tags = stanford_tagger(process_text(doc_text))

        for tag in tags:
            if tag[1] != 'O':
                entity_dict[tag[1]].append(tag[0])

    print(f'Total labels: {len(entity_dict.keys())}')
    print(f'{entity_dict.keys()}')

    for ner_label in entity_dict.keys():
        print(f'===================================={ner_label}: {len(entity_dict[ner_label])}')
        ner_label_count_tuple = count_and_tuple(entity_dict[ner_label])
        print_count_tuple(ner_label_count_tuple)
        save_path = osp.join(output_dir, f'{ner_label}.out')
        save_count_tuple(ner_label_count_tuple, save_path)



if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('docs_dir', type=str, help='Directory with the documents to be processed')
    # parser.add_argument('docs_ext', type=str, default='txt', help='File extension of documents to be processed')
    # args = parser.parse_args()

    main()