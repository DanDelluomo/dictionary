#!/bin/bash

# Retrieve giant word list from garden-variety Unix install
if [ -e /usr/share/dict/words ]
then
    DESTINATION="$( cd "$( dirname "$0" )" && cd .. && pwd )"
    if [ -e $DESTINATION/words.txt ]
    then    
        echo "words.txt already exists in $DESTINATION/"
    else
        :
    fi
else
    echo "/usr/share/dict/words not found"
fi





