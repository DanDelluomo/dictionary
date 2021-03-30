#!/bin/bash

# Retrieve giant word list from garden-variety Unix install
if [ -e /usr/share/dict/words ]
then
    cat /usr/share/dict/words > ../words.txt
    echo "Success! words.txt created in root of project"
else
    echo "/usr/share/dict/words not found"
fi

