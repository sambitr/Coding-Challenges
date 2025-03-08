## Step 0
Tech Stack: Python
Execution method: script way. ./timezone.py

## Step 1
Added option for the source time zone to destination time zone convertion. Th option is enabled for 1 source time zone to 1 or more destination time zone convertion.

By default the pytz module helps in 24 hour time zone

usage: 

```
python timezone.py --from-timezone <source time zone> --to-timezone <destination time zone(s)>
python timezone.py --from-timezone GMT  --to-timezone IST PST
```