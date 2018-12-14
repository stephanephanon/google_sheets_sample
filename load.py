"""
Women Who Code Python Meeting Attendance Google Doc script

Load data into google sheet
"""
import logging
from google.oauth2 import service_account
from googleapiclient import discovery
import settings


logger = logging.getLogger(__name__)


def update_google_sheet(attendance_data):
    """
    Update the google sheet with the latest
    attendance data.

    Prerequisites:
    1. Sheets file is 'writable by anyone with link'
    2. Service account is set up in google APIs credentials section
    and credentials.json is saved locally

    :param attendance_data:
    :return:
    """
    credentials = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_SERVICE_ACCOUNT_CREDS,
        scopes=settings.GOOGLE_SERVICE_ACCOUNT_SCOPES)

    service = discovery.build('sheets', 'v4', credentials=credentials)
    spreadsheet_id = settings.SPREADSHEET_ID

    # The A1 notation of a range to search for a logical table of data.
    # Values will be appended after the last row of the existing table found
    range_name = settings.MEETUP_DATA_RANGE

    # How the input data should be interpreted.
    value_input_option = 'USER_ENTERED'

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'

    body = {
        "values": attendance_data
    }

    logger.debug("Google Sheets API Call")
    logger.debug(spreadsheet_id)
    logger.debug(range_name)
    logger.debug(body)

    request = service.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        valueInputOption=value_input_option,
        insertDataOption=insert_data_option,
        body=body)

    response = request.execute()
    logger.info("Google Sheets API returned response: {}".format(response))
