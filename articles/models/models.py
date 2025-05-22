# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Articles(models.Model):
    _name = 'articles.articles'
    _description = 'articles.articles'
    _rec_name = 'nom_article'

    id_article = fields.Char(string="ID de l'article:")
    nom_article = fields.Char(string="Nom de l'article:")
    descripcio = fields.Char(string="Descripcio de l'article:")
    preu_sense_iva = fields.Float(string="Preu unitari (sense iva):")
    preu_total = fields.Float(string="Preu total (+ IVA):", compute='_compute_preu_total')

    # Metode per la sequencia de la ID
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'id_article' not in vals or not vals['id_article']:
                # Crida al metode next_by_code del model ir.sequence
                vals['id_article'] = self.env['ir.sequence'].next_by_code('articles.sequence') or '/'
        return super(Articles, self).create(vals)

    # Calcul del preu total
    @api.depends('preu_sense_iva')
    def _compute_preu_total(self):
        for record in self:
            record.preu_total = record.preu_sense_iva + 1.21