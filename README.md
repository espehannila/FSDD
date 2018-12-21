# Project 26: Finnish slang. Dynamic distribution

## External tools required

- [MongoDB](https://www.mongodb.com/)
- [Natural Language Toolkit](http://www.nltk.org/)
- [gensim](https://radimrehurek.com/gensim/)

## Data sources

- [Korp.csc](https://korp.csc.fi/)

## Text processing chain

1. Filter
2. Stopword removal
3. Tokenization
4. Lemmatization
5. Building dictionary

## Target

- Parsing
- Information retrieval (building model, scoring function)
- Sentiment Analysis
- Summarization
- Comparison, discussions with alternatives
- GUI interface

## Tag document
```shell
cat tokenized_input | python3 finnpos-ratna-feats.py ../share/finnpos/ftb_omorfi_model/freq_words | ./finnpos-label ../share/finnpos/ftb_omorfi_model/ftb.omorfi.model > tagged_input


bash -c "cat tokenized_input | python3 finnpos-ratna-feats.py ../share/finnpos/ftb_omorfi_model/freq_words | ./finnpos-label ../share/finnpos/ftb_omorfi_model/ftb.omorfi.model | python3 postag.py > tagged_input"

bash -c "echo 'Sanomassa' | python3 finnpos-ratna-feats.py ../share/finnpos/ftb_omorfi_model/freq_words | ./finnpos-label ../share/finnpos/ftb_omorfi_model/ftb.omorfi.model | python3 ./postag.py"
```


## Authors

*Esa Hannila, Oona Kivelä, Tuomas Koivuaho, Santeri Matero, Mauri Miettinen, Tuomas Tuokkola*


## Course

*Natural Language Processing and Text Mining, 521158S*

