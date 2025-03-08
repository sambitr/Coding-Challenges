Coding Challenge link: https://codingchallenges.substack.com/p/coding-challenge-85-time-zone-converter

## Usage:

```
$ python timezone.py --help
usage: timezone.py [-h] --from-timezone FROM_TIMEZONE --to-timezone TO_TIMEZONE [TO_TIMEZONE ...]

    Convert time from one timezone to single/multiple target timezones.

    Example Usage:
      python timezone.py --from-timezone "UTC" --to-timezone "IST" "PST" "JST"

    Available Timezones:
      IST, PST, EST, CET, JST, GMT, UTC



options:
  -h, --help            show this help message and exit
  --from-timezone FROM_TIMEZONE
                        Source Timezone name from list ['GMT', 'IST', 'CET', 'PDT', 'EDT', 'MDT']
  --to-timezone TO_TIMEZONE [TO_TIMEZONE ...]
                        One or more target Timezone names from ['GMT', 'IST', 'CET', 'PDT', 'EDT', 'MDT']. For multiple time zones separated by space
```
Example: 1

```
$ python timezone.py --from-timezone IST  --to-timezone IST PST AST
Error: Invalid destination timezone 'AST'. Run with --help to see available options.
```

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

## Step 2
Added section to sort the timezone in result.

Before sortig

```
python timezone.py --from-timezone IST  --to-timezone IST PST JST
source timezone: IST
Source time in IST timezone is 2025-03-08 22:09:40.046779+05:30
Converted Time in IST timezone is: 2025-03-08 22:09:40.046779+05:30
Converted Time in JST timezone is: 2025-03-09 01:39:40.046779+09:00
Converted Time in PST timezone is: 2025-03-08 08:39:40.046779-08:00
```
After sorting

```
python timezone.py --from-timezone IST  --to-timezone IST PST JST
source timezone: IST
Source time in IST timezone is 2025-03-08 22:10:25.710264+05:30
Converted Time in IST timezone is: 2025-03-08 22:10:25.710264+05:30
Converted Time in PST timezone is: 2025-03-08 08:40:25.710264-08:00
Converted Time in JST timezone is: 2025-03-09 01:40:25.710264+09:00
```

## Step 3
24 hour time zone is already done. This came by defalt with pytz python module

## Step 4
As I am building it on a script basis and not a GUI basis, this section is not possible