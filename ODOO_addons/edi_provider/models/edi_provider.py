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

    # ✅ Active Connection Checkboxes
    active_soap_ws = fields.Boolean(string="Active SOAP WS")
    active_as2 = fields.Boolean(string="Active AS2")
    active_as4 = fields.Boolean(string="Active AS4")
    active_sftp = fields.Boolean(string="Active SFTP")
    active_ftp = fields.Boolean(string="Active FTP")

    # SOAP WS Fields
    soap_ws_url = fields.Char(string="SOAP WS URL")
    soap_ws_username = fields.Char(string="SOAP WS Username")
    soap_ws_password = fields.Char(string="SOAP WS Password")

    # AS2 Fields
    as2_partner_url = fields.Char(string="AS2 Partner URL")
    as2_certificate = fields.Binary(string="AS2 Certificate")
    as2_encryption_method = fields.Char(string="AS2 Encryption Method")

    # AS4 Fields
    as4_partner_url = fields.Char(string="AS4 Partner URL")
    as4_certificate = fields.Binary(string="AS4 Certificate")
    as4_encryption_method = fields.Char(string="AS4 Encryption Method")

    # SFTP Fields
    sftp_host = fields.Char(string="SFTP Host")
    sftp_port = fields.Integer(string="SFTP Port")
    sftp_username = fields.Char(string="SFTP Username")
    sftp_password = fields.Char(string="SFTP Password")
    sftp_remote_path = fields.Char(string="SFTP Remote Path")

    # FTP Fields
    ftp_host = fields.Char(string="FTP Host")
    ftp_port = fields.Integer(string="FTP Port")
    ftp_username = fields.Char(string="FTP Username")
    ftp_password = fields.Char(string="FTP Password")
    ftp_remote_path = fields.Char(string="FTP Remote Path")
