from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests


class Avtovin(models.Model):
    _inherit = 'crm.lead'

    avtovin = fields.Char(string='AutoVIN', index=True)

    @api.constrains('avtovin')
    def _check_avtovin(self):
        for record in self:
            if record.avtovin:
                if len(record.avtovin) == 0:
                    raise ValidationError('VIN не має бути порожнім')

    def action_send_vin(self):
        vin_value = self.avtovin
        lead_id = self.id
        api_url = 'https://2d47-193-93-219-131.ngrok-free.app/avtovin'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Catch-Control': 'no-cache'}
        payload = {'lead_id': lead_id, 'vin_value': vin_value}

        response = requests.post(api_url, headers=headers, json=payload)
        response_json = response.json()

        if response.status_code == 200 and response_json.status == true:
            return
        elif response_json.status == false:
            raise ValidationError('Помилка: ' + response_json.error)
        else:
            raise ValidationError('Невідома помилка')
