"""
Women Who Code Python Meeting Attendance Download script

Extract data from meetup.com API
"""
import logging
import requests
import requests.exceptions
import settings


logger = logging.getLogger(__name__)


HTTP_200_OK = 200


def _fetch_url_response(url):
    """
    Fetch the response for this url
    :param url: meetup api url
    :return: dictionary or list
    :raise: requests HTTP exception if not 200 status
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
    except requests.exceptions.HTTPError as e:
        logger.exception(e)
        raise e
    return data

def fetch_event_info(event_id):
    """
    Get the event info for the given event id
    :param event_id: an event_id from meetup url, like 253504356
    :return: python dictionary
    :raise: requests HTTP exception if not 200 status
    """
    url = settings.EVENT_URL.format(event_id, settings.API_KEY)
    return _fetch_url_response(url)

def fetch_event_attendees(event_id):
    """
    Fetch the attendees for the given event id
    :param event_id: an event_id from meetup url, like 253504356
    :return: list of attendee dictionaries
    :raise: requests HTTP exception if not 200 status
    """
    url = settings.ATTENDANCE_URL.format(event_id, settings.API_KEY)
    return _fetch_url_response(url)
