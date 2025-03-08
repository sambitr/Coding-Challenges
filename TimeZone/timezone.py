from datetime import datetime
from pytz import timezone
import argparse

timezones = ["GMT", "IST", "CET", "PDT", "EDT", "MDT"]

def main(source_tz, dest_tz_list):

    format = "%Y-%m-%d %H:%M:%S"
    timezone_map = {
        "IST": "Asia/Kolkata",
        "PST": "America/Los_Angeles",
        "EST": "America/New_York",
        "CET": "Europe/Berlin",
        "JST": "Asia/Tokyo",
        "GMT": "GMT",  
        "UTC": "UTC"       
    }

    print(f"source timezone: {source_tz}")
    source_tz_new = timezone_map.get(source_tz, source_tz)
    source_time = datetime.now(timezone(source_tz_new))   
    print(f"Source time in {source_tz} timezone is {source_time}")    
    
    for dest_tz in dest_tz_list:
        dest_tz_new = timezone_map.get(dest_tz, dest_tz)

        converted_time = source_time.astimezone(timezone(dest_tz_new))
        print(f"Converted Time in {dest_tz} timezone is: {converted_time}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"This app is to Convert timezone. Timezones are: {timezones}")
    parser.add_argument("--from-timezone", required=True, help="Source Timezone name.")
    parser.add_argument("--to-timezone", nargs="+", required=True, help="One or more target Timezone names.")
    args = parser.parse_args()
    main(args.from_timezone, args.to_timezone)