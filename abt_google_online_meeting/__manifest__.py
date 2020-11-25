# -*- coding: utf-8 -*-
# Part of Alpha Brains Technologies.
{
    "name": "Google Online Meeting",
    "author": "Alpha Brains Technologies",
    "category": "Tools",
    "description": """This module allows users to create an online meeting events on Odoo Calendar using one of 
    the solutions provided by google (Hangouts or Meet) and synchronize the event with Google Calendar.
    """,
    "support": "odoo@alpha-brains.com",
    "website": "https://www.alpha-brains.com",
    "version": "1.0.0",
    "depends": [
        'google_calendar'
    ],
    "data": [
        'views/calendar_event_views.xml',
    ],
    "images": [
        'static/description/background.gif',
    ],
    "application": False,
    "installable": True,
    "price": 49.99,
    "currency": 'USD',
}
