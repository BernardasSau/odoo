from odoo import models, fields


class InfoFilterWizard(models.TransientModel):
    _name = 'info.filter.wizard'
    _description = 'Info Filter Wizard'

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_id = fields.Many2one('hr.employee', string='Employee')

    def action_filter_infos(self):
        domain = []
        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))
        if self.employee_id:
            domain.append(('employee_ids', 'in', [self.employee_id.id]))

        return {
            'name': 'Filtered Documents',
            'type': 'ir.actions.act_window',
            'res_model': 'document.management',
            'view_mode': 'tree,form',
            'domain': domain,
        }

    def action_generate_report(self):
        domain = []
        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))
        if self.employee_id:
            domain.append(('employee_ids', 'in', [self.employee_id.id]))

        report_action = self.env.ref('info.document_management_report')
        return report_action.report_action(self.env['document.management'].search(domain))
