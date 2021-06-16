#!/bin/bash

# Retrieve giant word list from garden-variety Unix install
if [ -e /usr/share/dict/words ]
then
    DESTINATION="$( cd "$( dirname "$0" )" && cd .. && pwd )"
    if [ ! -e $DESTINATION/words.txt ]
    then
        cat /usr/share/dict/words > $DESTINATION/words.txt
    else
        echo "words.txt already exists in $DESTINATION"
    fi
else
    echo "/usr/share/dict/words not found"
fi
