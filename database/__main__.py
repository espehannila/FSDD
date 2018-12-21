# -*- coding: utf-8 -*-
import sys
import db
from word import Word
from document import Document


def main():

    # Connect to the database
    conn              = db.connect()

    

    # Create document record
    document            = Document('Tämä dokumentti on manuaalisesti kirjoitettu tänne, joten se saattaa sisältää paljon virheitä', year='2018', conn=conn)
    document.save()


    # List all documents in database
    docs                = Document.find(conn=conn)
    print('\nList of docs in database')
    print('-----------------------------------------')
    for doc in docs:
        print(doc._id, doc.year, doc.text)
    print('-----------------------------------------')


    # Load one document from the database
    doc                 = Document.findOne({ 'text': 'Tämä' }, conn=conn)
    


    if doc is None:
        print('No document found')
    else:
        print('Found document "%s"' % doc.text)








    # Create word record
    word            = Word('Testi', conn=conn)

    word.save()



    # List all words in database
    words           = Word.find(conn=conn)
    print('\nList of words in database')
    print('-----------------------------------------')
    for word in words:
        print(word._id, word.text, word.docs)
    print('-----------------------------------------')



    # Load one word from the database
    testWord        = Word.findOne({ 'text': 'Testi' }, conn=conn)
    
    testWord.inDocument(doc)

    testWord.save()

    if testWord is None:
        print('No word found')
    else:
        print('Found word "%s"' % testWord.text, testWord.docs)


    # Remove word from database
    res             = Word.removeOne({ 'text': 'Testi' }, conn=conn)
    if res['n'] == 0:
        print('No word removed')
    else:
        print('Removed %d word(s)' % res['n'])







    # Remove document from database
    res             = Document.removeOne({ 'text': 'Tämä' }, conn=conn)
    if res['n'] == 0:
        print('No document removed')
    else:
        print('Removed %d document(s)' % res['n'])


if __name__ == '__main__':
    main()