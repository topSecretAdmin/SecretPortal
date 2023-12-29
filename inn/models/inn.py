from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests


class InfoBaza(models.Model):
    _inherit = 'crm.lead'

    info_baza = fields.Char(string='InfoBazaS', index=True)

    @api.constrains('info_baza')
    def _check_info_baza(self):
        for record in self:
            if record.info_baza:
                if not record.info_baza.isdigit():
                    raise ValidationError('ІПН має складатись з цифр')
                if len(record.info_baza) != 10:
                    raise ValidationError('ІПН має складатись з 10 цифр')

    def action_send_inn(self):
        inn_value = self.info_baza
        lead_id = self.id
        api_url = 'https://3f21-193-93-219-131.ngrok-free.app/user'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Catch-Control': 'no-cache'}
        payload = {'lead_id': lead_id, 'inn_value': inn_value}

        return requests.post(api_url, headers=headers, json=payload)
