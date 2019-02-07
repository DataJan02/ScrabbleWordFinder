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
find_all_words('able')
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
find_all_words('za',1)
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
For a set of characters, for example : "ywz", and 2 blanks, run the below command
```
find_all_words('yz',2)
```
#### Output
```
woozy
1 words found
```
For a set of characters, for example : "was", ending with y, run the below command
```
find_all_words('was',0,suffix="y")
```
#### Output
```
wy
way
say
sway
4 words found
```
For a set of characters, for example : "slwas", starting with "a"
, ending with "h" and having a minimum of 3 characters from your rack, run the below command
```
find_all_words("slwas", blanks=0, prefix="a", suffix="h", min_chars=3)
```
#### Output
```
awash
1 words found
```
### Issues : 
1. Deprecation warnings to be suppressed.
2. Repetitions in the result set.
