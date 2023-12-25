from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    custom_field = fields.Char(string='Custom Field')
