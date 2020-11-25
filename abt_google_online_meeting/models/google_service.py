# -*- coding: utf-8 -*-
# Part of Alpha Brains Technologies.

# Import Odoo libs
from odoo import api, models


class ABTGoogleService(models.TransientModel):
    _inherit = 'google.service'

    @api.model
    def _do_request(self, uri, params={}, headers={}, type='POST', preuri="https://www.googleapis.com"):
        # Initialize variables
        abt_is_conference = self.env.context.get('abt_is_conference')

        # If the event is a conference then add 'conferenceDataVersion' field to URI
        if abt_is_conference:
            uri += "&conferenceDataVersion=1"

        # Call super method & return
        return super(ABTGoogleService, self)._do_request(uri, params, headers, type, preuri)
