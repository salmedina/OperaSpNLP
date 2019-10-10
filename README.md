# OperaSpNLP

### SpaCy

- Install 2.1.0 to enable `neuralcoref` module

```
pip install -U spacy==2.1.0
pip install -U spacy-lookups-data
python -m spacy download es_core_news_md
```


### Stanford Core NLP


## UDPipe
Installed UDPipe using the SpaCy framework on top through `spacy_udpipe` and using the `es-ancora` model to compare under the same baseline against SpaCy and SCNLP.

```
pip install spacy-udpipe
python3 "import spacy_udpipe; spacy_udpipe.download('es-ancora')"
```
