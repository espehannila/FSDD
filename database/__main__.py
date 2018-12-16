import sys
import db

if __name__ == '__main__':

    # Connect to the database
    conn              = db.connect()


    ## Word testing

    # Create word record
    word            = { "text": "Testi", "docs": [] }
    
    # Add word to database
    db.addWord(word, conn)

    # Find word from database
    foundWord   = db.findWord(word, conn)
    
    # Verify word found
    if foundWord is None:
        print('Something went wrong, word', word['text'], 'does not exist as it should be')
        sys.exit(1)

    # Update word
    foundWord['docs'].append('test')

    # Replace word with updated one
    db.replaceWord(foundWord, conn)

    # Verify that word exists
    if db.wordExist({ 'text': 'Testi' }, conn):
        print('Word exists as it should be')
    else:
        print('Word does not exist')

    # Remove word from database
    db.removeWord(word['text'], conn)
    
    # Verify that word doesn't exist
    if db.wordExist({ 'text': 'Testi' }, conn):
        print('Word exists after remove')
    else:
        print('Word does not exist after remove')



    ## Document testing

    # Create document record
    doc         = {
        'text': 'Jotain sinne päin menevää dokumenttia'
    }

    # Store document to database
    db.addDocument(doc, conn)

    # Remove document from database
    db.removeDocument(doc, conn)