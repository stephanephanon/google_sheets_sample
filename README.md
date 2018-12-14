Sample project for meetup attendance helper application

Fetch data from meetup api, put into google sheets format, and save to google sheet

Getting Started with Google API
===============================

Register a New Google Project
-----------------------------

    1. Log into google.
    2. Go to https://console.developers.google.com/projectselector/iam-admin/serviceaccounts?supportedpurview=project
    3. Click 'create' to make a new google project
    4. Give the project a name.
    5. You'll end up on the dashboard. Scroll down to Getting Started.
    6. Click on APIs and Services
    7. You'll want to enable the Google Drive API


Google Project Credentials
--------------------------

    1. Click on the Credentials link.
    2. Click on Service Account.
    3. Name the service account.
    3. Click on Role -> Editor.
    4. Click on Key -> JSON.
    5. You'll get the JSON credentials file. Keep it safe and secure!
    6. Save the file as google_service_account_credentials.json. You'll need it for Settings and Config.


Application Prerequisites
=========================

    1. pip install -r requirements.txt (tested using python 3.7 virtual environment)
    2. Service account is set up in google API's credentials section under your own google account
    3. The file google_service_account_credentials.json is saved locally
    4. Google sheets spreadsheet already exists and is 'writable by anyone with link'.
    5. You have the spreadsheet id from the url: https://docs.google.com/spreadsheets/d/<this is the spreadsheet id>/edit#gid=0


Settings and Config
===================

    1. Update settings.ini with your values. Do NOT check settings.ini into git.
    2. Update google_service_account_credentials.json. See sample_google_service_account_credentials.json. Do NOT check credentials into git.
    3. settings.py will read in config for application


Command
=======

    Run with a meeting id, eg: https://www.meetup.com/Women-Who-Code-DC/events/253504356/

    python google_sheets_etl.py 253504356

