from odoo import models, fields
import odoo.addons.decimal_precision as dp


class AccountTaxWithholdingRule(models.Model):
    _name = "account.tax.withholding.rule"
    _order = "sequence"

    sequence = fields.Integer(
        default=10,
    )
    # name = fields.Char(
    #     required=True,
    #     )
    domain = fields.Char(
        required=True,
        default="[]",
        help='Write a domain over account voucher module'
    )
    tax_withholding_id = fields.Many2one(
        'account.tax',
        'Tax Withholding',
        required=True,
        ondelete='cascade',
    )
    percentage = fields.Float(
        'Percentage',
        digits=(16, 4),
        help="Enter % ratio between 0-1."
    )
    fix_amount = fields.Float(
        'Amount',
        digits=dp.get_precision('Account'),
        help="Fixed Amount after percentaje"
    )
