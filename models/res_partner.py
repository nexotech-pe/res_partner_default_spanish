from odoo import models, fields, api

class ResPartnerCustom(models.Model):
    _inherit = 'res.partner'

    @api.model
    def default_get(self, default_fields):
        # Primero llamamos al método super() para obtener los valores por defecto existentes
        values = super(ResPartnerCustom, self).default_get(default_fields)

        # Cambiar el valor predeterminado del campo 'lang' a 'es_PE'
        if 'lang' in default_fields:
            values['lang'] = 'es_PE'

        return values