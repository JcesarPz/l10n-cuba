from odoo import models, _
from odoo.addons.account.models.chart_template import template

class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template('cu_common')
    def _get_cu_common_template_data(self):
        return {
            'name': _('Plan Contable Común (494/2016 modified by 407/2019)'),
            'visible': False,
            'code_digits': '3',
            'property_account_receivable_id': 'account_common_1350020',#OK
            'property_account_payable_id': 'account_common_4050020',#OK
            'property_account_expense_categ_id': 'account_common_826',
            'property_account_income_categ_id': 'account_common_900',
        }

    @template('cu_common', 'res.company')
    def _get_cu_common_res_company(self):
        return {
            self.env.company.id: {
                'account_fiscal_country_id': 'base.cu',
                'bank_account_code_prefix': '109.', #OK
                'cash_account_code_prefix': '101.', #OK
                'transfer_account_code_prefix': '108.',#OK
                'account_default_pos_receivable_account_id': 'account_common_1300020', #OK
                'account_journal_payment_debit_account_id':'account_common_106',
                'account_journal_payment_credit_account_id':'account_common_107',
                #'income_currency_exchange_account_id': 'a754',
                #'expense_currency_exchange_account_id': 'a654',
                'account_journal_suspense_account_id': 'account_common_6993',
                'account_journal_early_pay_discount_loss_account_id': 'account_common_835',
                'account_journal_early_pay_discount_gain_account_id': 'account_common_920',
                #'account_sale_tax_id': 'attn_VAT-OUT-21-L',
                #'account_purchase_tax_id': 'attn_VAT-IN-V81-21',
                'default_cash_difference_income_account_id': 'account_common_924',
                'default_cash_difference_expense_account_id': 'account_common_839',
                #'transfer_account_id': 'a58',
            },
        }
