from odoo import models, fields

class EDIProvider(models.Model):
    _name = 'edi.provider'
    _description = 'EDI Provider'

    name = fields.Char(string="Provider Name", required=True)
    communication_method = fields.Selection([
        ('as2', 'AS2'),
        ('as4', 'AS4'),
        ('sftp', 'SFTP'),
        ('ftp', 'FTP'),
        ('local', 'Local Folder'),
    ], string="Communication Method", required=True)
    auth_type = fields.Selection([
        ('basic', 'Basic Authentication'),
        ('oauth', 'OAuth 2.0'),
        ('cert', 'Certificate-Based Authentication'),
    ], string="Authentication Type", required=True)
    username = fields.Char(string="Username")
    password = fields.Char(string="Password")
    api_url = fields.Char(string="API URL")
    notes = fields.Text(string="Notes")
