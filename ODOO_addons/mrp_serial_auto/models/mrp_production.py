from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    lot_producing_id = fields.Many2one('stock.lot', string='Serial Number', readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('product_id'):
            product = self.env['product.product'].browse(vals['product_id'])

            if product.tracking == 'serial' and product.default_code:
                year = datetime.now().year
                sequence = self.env['ir.sequence'].next_by_code('semi_finished_serial') or '00001'
                formatted_sequence = str(sequence).zfill(5)
                serial_number = f"{product.default_code}{year}{formatted_sequence}"

                existing_lots = self.env['stock.lot'].search([('name', '=', serial_number)])

                if len(existing_lots) >= 2:
                    raise UserError(_(f"Serijski broj {serial_number} je već dodijeljen dvaput i ne može se ponovo koristiti."))

                if existing_lots:
                    vals['lot_producing_id'] = existing_lots[0].id
                else:
                    lot = self.env['stock.lot'].create({
                        'name': serial_number,
                        'product_id': product.id,
                        'company_id': self.env.company.id
                    })
                    vals['lot_producing_id'] = lot.id

        return super(MrpProduction, self).create(vals)

    def action_confirm(self):
        res = super(MrpProduction, self).action_confirm()

        for production in self:
            if production.product_id.tracking == 'serial':
                semi_finished_moves = production.move_raw_ids.filtered(lambda m: m.product_id.tracking == 'serial')

                if semi_finished_moves:
                    semi_finished_lot = semi_finished_moves.mapped('move_line_ids.lot_id')

                    if semi_finished_lot:
                        serial_lot = semi_finished_lot[0]

                        existing_final_lots = self.env['stock.lot'].search([('name', '=', serial_lot.name)])

                        if len(existing_final_lots) >= 2:
                            raise UserError(_(f"Serijski broj {serial_lot.name} je već dodijeljen dvaput i ne može se ponovo koristiti."))

                        existing_lot = self.env['stock.lot'].search([
                            ('name', '=', serial_lot.name),
                            ('product_id', '=', production.product_id.id)
                        ], limit=1)

                        if not existing_lot:
                            existing_lot = self.env['stock.lot'].create({
                                'name': serial_lot.name,
                                'product_id': production.product_id.id,
                                'company_id': self.env.company.id
                            })

                        production.lot_producing_id = existing_lot

                        for move in semi_finished_moves:
                            move_line = move.move_line_ids.filtered(lambda ml: ml.lot_id == serial_lot)
                            if move_line:
                                move_line.write({'qty_done': move.product_uom_qty})
                            else:
                                self.env['stock.move.line'].create({
                                    'move_id': move.id,
                                    'lot_id': serial_lot.id,
                                    'product_id': move.product_id.id,
                                    'qty_done': move.product_uom_qty,
                                    'location_id': move.location_id.id,
                                    'location_dest_id': move.location_dest_id.id,
                                })

                        production.move_raw_ids.filtered(lambda m: m.product_id.tracking == 'serial').write({'quantity_done': 1})
        return res
