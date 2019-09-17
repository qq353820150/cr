# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)

class CrBaseProjectType(models.Model):

    _name = 'cr.base.project.type'
    _rec_name = 'cr_base_project_type_name'
    _description = u'业态类别'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_project_type_name = fields.Char(string=u'业态类别', track_visibility='onchange',required=True)

    cr_base_project_id = fields.One2many('cr.base.project','id',string='经营项目')


class CrBaseProject(models.Model):

    _name = 'cr.base.project'
    _rec_name = 'cr_base_project_name'
    _description = u'经营项目'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_project_name = fields.Char(string=u'经营项目', track_visibility='onchange',required=True)

    cr_base_project_id = fields.Char(string=u'项目id', track_visibility='onchange',required=True)

    cr_base_project_type_id =fields.Many2one('cr.base.project.type',u'业态类别')


