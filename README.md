
# Syllable Encoder

Decodes syllables inside a word. Applies vocabulary limit to low-frequency syllables. Can learn sylable frequencies from scratch.

This syllable encoder currently supports Turkish only.

## Usage

```bash
$ pip install git+https://github.com/ftkurt/python-syllable.git@master
```

```python
from syllable import Encoder


encoder = Encoder(lang="tr", limitby="vocabulary", limit=3000)  # params chosen for demonstration purposes

example = "İki kürkü yırtık kel kör kirpi dadanmış."
print(encoder.tokenize(example))
# i ki kür kü yır tık kel kör kir pi da dan mış
print(next(encoder.transform([example])))
# [10, 11, 713, 161, 859, 347, 349, 1081, 639, 384, 4, 49, 156]
print(next(encoder.inverse_transform(encoder.transform([example]))))
# i ki kür kü yır tık kel kör kir pi da dan mış
```
