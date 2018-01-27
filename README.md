
# Syllable Encoder for Text

AKA Byte Pair Encoding.  Learns a vocab and byte pair encoding for provided white-space separated text.

This syllable encoder currently supports Turkish only.

## Usage

```bash
$ pip install git+https://github.com/ftkurt/python-syllable.git@master
```

```python
from syllable import Encoder


encoder = Encoder(lang="tr",vocab=3000)  # params chosen for demonstration purposes

example = "İki kürkü yırtık kel kör kirpi dadanmış."
print(encoder.tokenize(example))
# [['İ', 'ki'], ['kür', 'kü'], ['yır', 'tık'], ['kel'], ['kör'], ['kir', 'pi'], ['da', 'dan', 'mış', '.']]
print(next(encoder.transform([example])))
# [26, 108, 79, 104, 72, 24, 26, 117, 24, 9, 11, 8, 12, 10, 26, 90, 24, 26, 154, 56, 37, 149, 80, 169, 84, 24, 26, 156, 24]
print(next(encoder.inverse_transform(encoder.transform([example]))))
# İki kürkü yırtık kel kör kirpi dadanmış.
```
