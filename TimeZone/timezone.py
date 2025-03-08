from datetime import datetime
import pytz
import sys
import argparse

timezones = ["GMT", "IST", "CET", "PDT", "EDT", "MDT"]

timezone_map = {
        "IST": "Asia/Kolkata",
        "PST": "America/Los_Angeles",
        "EST": "America/New_York",
        "CET": "Europe/Berlin",
        "JST": "Asia/Tokyo",
        "GMT": "GMT",  
        "UTC": "UTC"       
    }

ALL_TIMEZONES = set(pytz.all_timezones) | set(timezone_map.keys())

def validate_timezones(source_tz, dest_tz_list):
    # Convert shorthand timezone to full form
    source_tz_new = timezone_map.get(source_tz, source_tz)

    if source_tz_new not in ALL_TIMEZONES:
        print(f"Error: Invalid source timezone '{source_tz}'. Run with --help to see available options.")
        sys.exit(1)

    for dest_tz in dest_tz_list:
        dest_tz_new = timezone_map.get(dest_tz, dest_tz)
        if dest_tz_new not in ALL_TIMEZONES:
            print(f"Error: Invalid destination timezone '{dest_tz}'. Run with --help to see available options.")
            sys.exit(1)

    return source_tz_new, [timezone_map.get(tz, tz) for tz in dest_tz_list]

def main(source_tz, dest_tz_list):

    format = "%Y-%m-%d %H:%M:%S"

    print(f"source timezone: {source_tz}")
    source_tz_new = timezone_map.get(source_tz, source_tz)
    source_time = datetime.now(pytz.timezone(source_tz_new))   
    print(f"Source time in {source_tz} timezone is {source_time}")    
    
    for dest_tz in dest_tz_list:
        dest_tz_new = timezone_map.get(dest_tz, dest_tz)

        converted_time = source_time.astimezone(pytz.timezone(dest_tz_new))
        print(f"Converted Time in {dest_tz} timezone is: {converted_time}")

if __name__ == "__main__":
    description_msg = f"""
    Convert time from one timezone to single/multiple target timezones.

    Example Usage:
      python timezone.py --from-timezone "UTC" --to-timezone "IST" "PST" "JST"

    Available Timezones:
      {', '.join(timezone_map.keys())}

    """

    parser = argparse.ArgumentParser(description=description_msg, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--from-timezone", required=True, help=f"Source Timezone name from list {timezones}")
    parser.add_argument("--to-timezone", nargs="+", required=True, help=f"One or more target Timezone names from {timezones}. For multiple time zones separated by space")
    args = parser.parse_args()
    validated_source_tz, validated_dest_tz_list = validate_timezones(args.from_timezone, args.to_timezone)

    #main(args.from_timezone, args.to_timezone)
    main(validated_source_tz, validated_dest_tz_list)
