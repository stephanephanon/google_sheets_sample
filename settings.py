import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

# depends on user
API_KEY = config['meetup']['API_KEY']

# https://api.meetup.com/Women-Who-Code-DC/events/253504356/attendance
EVENT_URL = "https://api.meetup.com/Women-Who-Code-DC/events/{}?key={}"
ATTENDANCE_URL = "https://api.meetup.com/Women-Who-Code-DC/events/{}/attendance?key={}"

# google sheets
SPREADSHEET_ID = config['google']['SPREADSHEET_ID']
MEETUP_DATA_RANGE = config['google']['MEETUP_DATA_RANGE']

GOOGLE_SERVICE_ACCOUNT_CREDS = "google_service_account_credentials.json"
GOOGLE_SERVICE_ACCOUNT_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
