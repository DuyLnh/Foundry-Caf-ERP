from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'

    vietqr_bank_account = fields.Char(string='So tai khoan VietQR')
    vietqr_bank_code = fields.Char(string='Ma ngan hang', default='MB')
    vietqr_account_name = fields.Char(string='Ten chu tai khoan')