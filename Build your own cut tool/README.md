### Set alias

$ alias ccsed="python cut.py"

### Step: 1

```
$ cut -f2 sample.tsv
f1
1
6
11
16
21
```

### Step: 2

```
$ cut -f1 -d, fourchords.csv|head -n5 
Song title
"10000 Reasons (Bless the Lord)"
"20 Good Reasons"
"Adore You"
"Africa"
```

### Step: 3

```
$ cut -f"1 2 3" sample.tsv
f0      f1      f2
0       1       2
5       6       7
10      11      12
15      16      17
20      21      22
```

$ cut -f1,2 sample.tsv

```
f0      f1
0       1
5       6
10      11
15      16
20      21
```

