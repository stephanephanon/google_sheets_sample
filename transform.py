"""
Women Who Code Python Meeting Attendance Google Doc script

Transform data into format needed for google sheet
"""
import logging

logger = logging.getLogger(__name__)


def get_event_info(event_info):
    """
    Get the event info that we need for the
    google doc. We track date and event name
    :param event_info: dictionary of event fields
    :return: tuple of date and name
    """
    event_date = event_info.get('local_date')
    event_name = event_info.get('name')

    logger.info("Event Details: {}, {}".format(event_date, event_name))
    return event_date, event_name


def get_rsvp_attendees_for_response(attendees, filter_responses="all"):
    """
    Build the list of attendees who rsvp'd yes.
    We capture attendee_id, name, and rsvp response
    :param attendees: list of members, where member is
    dict like
        # {'member': {'id': 12345, 'name': 'Sam',
        'event_context': {'host': False}},
        'rsvp': {'id': 1743141827, 'response':
        'no', 'guests': 0, 'updated': 1534371163000}}
    :param filter_responses: comma-separated list of responses to keep. default is 'yes'.
        values are 'no', 'yes', 'waitlist', and 'all'
    :return: list of tuples: [(member_id, member_name), ...]
        where rsvp_response = filtered response
    """
    import pprint
    pprint.pprint(attendees)
    if filter_responses == 'all':
        filter_responses = ("no", "yes", "waitlist")
    filter_responses = filter_responses.split(",")

    rsvp_filtered_attendees = []
    for attendee in attendees:
        member = attendee.get("member")
        rsvp = attendee.get("rsvp")

        member_id = member.get('id')
        member_name = member.get('name')
        rsvp_response = rsvp.get("response")

        if rsvp_response in filter_responses:
            rsvp_filtered_attendees.append((member_id, member_name))

    logger.info("RSVP Attendees Count for user responses in: {}: {}"
                .format(filter_responses, len(rsvp_filtered_attendees)))

    logger.debug("filter responses: %s", filter_responses)
    logger.debug("rsvp attendees: %s", rsvp_filtered_attendees)

    return rsvp_filtered_attendees

def generate_spreadsheet_body(event_data, yes_attendees_data):
    """
    Combine the event_data and the yes_attendees_data into the
    format needed for appending to the google doc
    :param event_data:
    :param yes_attendees_data:
    :return: a list of tuples, where inner tuple is:
        ('2018-08-15', 'Python Lab: Data Control Flow', 12345, 'Sam', )
    """
    # columns: Date, Name, Attendee ID, Name, Did they Attend? (0 True, 1 False)
    # the google write range api expects a list of lists for 'values' key
    row_data = []
    for attendee in yes_attendees_data:
        row_data.append(event_data + attendee)

    logger.debug("spreadsheet body %s", row_data)
    return row_data
