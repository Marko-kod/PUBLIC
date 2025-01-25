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

    # SOAP WS
    soap_ws_url = fields.Char(string="SOAP WS URL")
    soap_ws_username = fields.Char(string="SOAP Username")
    soap_ws_password = fields.Char(string="SOAP Password")

    # AS2
    as2_partner_url = fields.Char(string="AS2 Partner URL")
    as2_certificate = fields.Binary(string="AS2 Certificate")
    as2_encryption_method = fields.Selection([
        ('none', 'None'),
        ('3des', '3DES'),
        ('aes', 'AES'),
    ], string="AS2 Encryption Method")

    # AS4
    as4_partner_url = fields.Char(string="AS4 Partner URL")
    as4_certificate = fields.Binary(string="AS4 Certificate")
    as4_encryption_method = fields.Selection([
        ('none', 'None'),
        ('3des', '3DES'),
        ('aes', 'AES'),
    ], string="AS4 Encryption Method")

    # SFTP
    sftp_host = fields.Char(string="SFTP Host")
    sftp_port = fields.Integer(string="SFTP Port", default=22)
    sftp_username = fields.Char(string="SFTP Username")
    sftp_password = fields.Char(string="SFTP Password")
    sftp_remote_path = fields.Char(string="SFTP Remote Path")

    # FTP
    ftp_host = fields.Char(string="FTP Host")
    ftp_port = fields.Integer(string="FTP Port", default=21)
    ftp_username = fields.Char(string="FTP Username")
    ftp_password = fields.Char(string="FTP Password")
    ftp_remote_path = fields.Char(string="FTP Remote Path")
