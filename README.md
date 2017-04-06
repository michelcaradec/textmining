# textmining

Tiny text mining package for Python.

## Setup

```bash
pip install textmining
```

## Usage

### Tokenization

```python
import tm

text = u"Les chaussettes de l'archiduchesse sont-elles sèches, archi-sèches ?"
for token in tm.tokenize(text):
    print token
```

Output:

	Les
	chaussettes
	de
	l
	archiduchesse
	sont
	elles
	sèches
	archi
	sèches

```python
import tm

text = u"Les chaussettes de l'archiduchesse sont-elles sèches, archi-sèches ?"
for token in tm.tokenize(text, split_on_dash=False):
    print token
```
	
Output:

	Les
	chaussettes
	de
	l
	archiduchesse
	sont-elles
	sèches
	archi-sèches

### Applying successive transformations

```python
import tm

print tm.transform(u"Archi-sèches", [tm.to_lower, tm.substitute_accents])
```

Output:

	archi-seches

### Tokenization and transformation

```python
import tm

transformations = [tm.clean, \
    tm.min_len(1), \
    tm.to_lower, \
    tm.remove_stopwords, \
    tm.substitute_accents]

text = u"Les chaussettes de l'archiduchesse sont-elles sèches, archi-sèches ?"
tokens = tm.tokenize_transform(text, transformations)

print " ".join(tokens)
```

Output:

	chaussettes archiduchesse seches archi seches

### First name detection

```python
import tm

for firstname in [u"Mathilde", u"Gaëlle", u"Grégory", u"Rennes", u"Yann"]:
    print "%s is %sa first name." % (firstname, "" if tm.is_firstname(firstname) else "not ")
```

Output:

	Mathilde is a first name.
	Gaëlle is a first name.
	Grégory is a first name.
	Rennes is not a first name.
	Yann is a first name.

### Gender detection

```python
from firsname import FirstName

for firstname in [u"Mathilde", u"Gaëlle", u"Grégory", u"Yann"]:
	FirstName.get_singleton().get_gender(firstname)
```

Output:

	Mathilde: 3
	Gaëlle: 2
	Grégory: 1
	Yann: 3
