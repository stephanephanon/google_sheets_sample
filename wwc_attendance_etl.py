"""
Main entry point into the Women Who Code Python attendance helper application

Fetch data from meetup api, put into google sheets format, and save to google sheet

Prerequisites:

    1. pip install -r requirements.txt (tested using python 3)
    2. Service account is set up in google APIs credentials section
    and credentials.json is saved locally
    3. Google sheets spreadsheet already exists and is 'writable by anyone with link'

Command:

    python google_sheets_etl.py 253504356

"""
import logging
import extract
import transform
import load
import argparse


logger = logging.getLogger(__name__)


def main(event_id, dry_run):
    """
    Ingest data from meetup.com, transform data, and upload into google sheet
    :param event_id: meetup.com event to process
    :param dry_run: if set, just print spreadsheet data instead of sending to google
    """
    event_info = extract.fetch_event_info(event_id)
    event_info = transform.get_event_info(event_info)

    attendees = extract.fetch_event_attendees(event_id)
    attendees = transform.get_rsvp_attendees_for_response(
        attendees, filter_responses='yes')

    spreadsheet_values = transform.generate_spreadsheet_body(event_info, attendees)

    if dry_run:
        print("----------DRY RUN. INFO ONLY. WILL NOT SAVE TO GOOGLE SHEET----------")
        print(spreadsheet_values)
    else:
        load.update_google_sheet(spreadsheet_values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'eventid',
        help=('meetup.com event id from url. '
              'For https://www.meetup.com/Women-Who-Code-DC/events/253504356/, '
              'the eventid is 253504356'))
    parser.add_argument(
        "--loglevel",
        default='INFO',
        help="Loglevel for information returned while running the script. "
             "DEBUG, INFO. Default is INFO."
    )
    parser.add_argument(
        "--dryrun",
        action='store_true',
        help="If set, download data from meetup.com and print spreadsheet values to "
             "console, but do NOT try to send data to google sheet."
    )

    args = parser.parse_args()

    # set up logging
    loglevel = args.loglevel
    logging.basicConfig(level=loglevel)

    # google's annoying :)
    logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

    # get the event_id from the command line
    event_id = args.eventid

    # dry run info
    dry_run = args.dryrun

    print("-----Start attendance script-----")
    main(event_id, dry_run)
    print("-----Script complete-----")
