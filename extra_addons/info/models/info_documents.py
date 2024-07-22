from odoo import models, fields


class Document(models.Model):
    _name = 'document.management'
    _description = 'Document Management'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company')
    user_id = fields.Many2one('res.users', string='Created By', default=lambda self: self.env.user)
    employee_ids = fields.Many2many('hr.employee', string='Responsible Employees')
    date_field = fields.Date(string='Date Field', default=lambda self: fields.Date.context_today(self))