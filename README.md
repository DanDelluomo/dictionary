In-memory Python dictionary of the English language for easy access in NLP applications. 

To my knowledge, this does not exist. Current dictionary packages rely on API calls under the hood, which are extremely slow compared to key lookup.

## Install
```
pip install english_dictionary
```

## Usage

```
from english_dictionary.scripts.read_pickle import get_dict
english_dict = get_dict()

english_dict["xylophone"]  # english_dict is a Python dictionary of English
```
