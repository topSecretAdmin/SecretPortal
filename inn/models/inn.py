from odoo import models, fields, api
from odoo.exceptions import ValidationError
import requests


class InfoBaza(models.Model):
    _inherit = 'crm.lead'

    info_baza = fields.Char(string='InfoBaza', index=True)
    phone_number = fields.Char(string='Phone', index=True)

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
        api_url = 'https://749f-193-93-219-131.ngrok-free.app/user'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Catch-Control': 'no-cache'}
        payload = {'lead_id': lead_id, 'inn_value': inn_value}

        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return
        else:
            raise ValidationError('За цим ІПН даних не знайдено')

    @api.constrains('phone_number')
    def _check_phone_number(self):
        for record in self:
            if record.phone_number:
                if not record.phone_number.isdigit():
                    raise ValidationError('Номер має складатись з цифр')

    def action_send_phone_number(self):
        phone_number_value = self.phone_number
        lead_id = self.id
        api_url = 'https://749f-193-93-219-131.ngrok-free.app/user'
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Catch-Control': 'no-cache'}
        payload = {'lead_id': lead_id, 'phone_number_value': phone_number_value}

        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            return
        else:
            raise ValidationError('За цим номером даних не знайдено')
