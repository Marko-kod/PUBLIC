from odoo import models, fields

class EDIProvider(models.Model):
    _name = 'edi.provider'
    _description = 'EDI Provider'
    
    name = fields.Char(string="Provider Name", required=True)
    streat = fields.Char(string="Streat")
    town = fields.Char(string="Town")
    zip = fields.Char(string="Zip code")
    vat = fields.Char(string="VAT number")
    notes = fields.Text(string="Notes")

    # SOAP WS
    is_active_soap = fields.Boolean(string="Active SOAP WS")
    soap_ws_url = fields.Char(string="SOAP WS URL")
    soap_ws_username = fields.Char(string="SOAP Username")
    soap_ws_password = fields.Char(string="SOAP Password")

    # AS2
    is_active_as2 = fields.Boolean(string="Active AS2")
    as2_partner_url = fields.Char(string="AS2 Partner URL")
    as2_certificate = fields.Binary(string="AS2 Certificate")
    as2_encryption_method = fields.Selection([
        ('none', 'None'),
        ('3des', '3DES'),
        ('aes', 'AES'),
    ], string="AS2 Encryption Method")

    # AS4
    is_active_as4 = fields.Boolean(string="Active AS4")
    as4_partner_url = fields.Char(string="AS4 Partner URL")
    as4_certificate = fields.Binary(string="AS4 Certificate")
    as4_encryption_method = fields.Selection([
        ('none', 'None'),
        ('3des', '3DES'),
        ('aes', 'AES'),
    ], string="AS4 Encryption Method")

    # SFTP
    is_active_sftp = fields.Boolean(string="Active SFTP")
    sftp_host = fields.Char(string="SFTP Host")
    sftp_port = fields.Integer(string="SFTP Port", default=22)
    sftp_username = fields.Char(string="SFTP Username")
    sftp_password = fields.Char(string="SFTP Password")
    sftp_remote_path = fields.Char(string="SFTP Remote Path")

    # FTP
    is_active_ftp = fields.Boolean(string="Active FTP")
    ftp_host = fields.Char(string="FTP Host")
    ftp_port = fields.Integer(string="FTP Port", default=21)
    ftp_username = fields.Char(string="FTP Username")
    ftp_password = fields.Char(string="FTP Password")
    ftp_remote_path = fields.Char(string="FTP Remote Path")
