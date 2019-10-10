import os.path as osp
import spacy_udpipe
from glob import glob
from collections import defaultdict
from unidecode import unidecode

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
    docs_dir = '/home/zal/Devel/OperaSpNLP/docs'
    output_dir = '/home/zal/Devel/OperaSpNLP/output/udpipe/ner'
    file_ext = 'txt'

    nlp = spacy_udpipe.load('es-ancora')

    entity_dict = defaultdict(list)

    for file_path in glob(osp.join(docs_dir, f'*.{file_ext}')):
        doc_text = unidecode(open(file_path, 'r').read())
        doc = nlp(doc_text)
        for ent in doc.ents:
            entity_dict[ent.label_].append(ent.text)

    print(f'Total labels: {len(entity_dict.keys())}')
    print(f'{entity_dict.keys()}')

    for ner_label in entity_dict.keys():
        print(f'===================================={ner_label}: {len(entity_dict[ner_label])}')
        ner_label_count_tuple = count_and_tuple(entity_dict[ner_label])
        print_count_tuple(ner_label_count_tuple)
        save_path = osp.join(output_dir, f'{ner_label}.out')
        save_count_tuple(ner_label_count_tuple, save_path)



if __name__ == '__main__':

    main()