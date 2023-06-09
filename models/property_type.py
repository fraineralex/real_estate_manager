from odoo import models, fields

class PropertyType(models.Model):
    _name = 'property.type'
    _description = 'Tipo de Propiedad'

    name = fields.Char(string='Nombre del Tipo de Propiedad', required=True)
    description = fields.Text(string='Descripción', required=True)