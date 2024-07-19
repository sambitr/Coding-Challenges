### Set alias

$ alias ccsed="python ccsed.py"

### Step: 1
<br>########## ================== <br>
REPLACE QUOTES(") FROM ENTIRE FILE

$ ccsed s/\"//g test.txt
<br>########## ================== <br>
### Step: 2
mimic sed -n '2,4p' file name

$ ccsed -n '2,4p' unquoted.txt
<br>########## ================== <br>
### Step: 3
ccsed -n /pattern/p filename

$ ccsed -n /roads/p unquoted.txt
<br>########## ================== <br>

### Step: 4
to support double spacing a file

$ ccsed G unquoted.txt
<br>########## ================== <br>
### Step: 5
to support deletion

$ ccsed /^$/d unquoted.txt
<br>########## ================== <br>
