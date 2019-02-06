# ScrabbleWordFinder
Enter characters (as a string) and number of blanks to find all eligible words

### Prerequisites

You'll need nltk corpus for the required dictionary

```
>>> pip install nltk
>>> nltk.download()
```

Select wordnet and download from the GUI

### Example

For a set of characters, for example : "able", and no blanks, run the below command
```
wordFinder('able')
```
#### Output
```
able
abel
bale
blae
4 words found
```
For a set of characters, for example : "za", and 1 blank, run the below command
```
wordFinder('za',1)
```
#### Output
```
azs
adz
zea
zap
zag
azt
azo
7 words found
```
```
For a set of characters, for example : "ywz", and 2 blanks, run the below command
```
wordFinder('yz',2)
```
#### Output
```
woozy
1 words found
```
Issues : 
1. Deprecation warnings to be suppressed.
2. Repetitions in the result set.
