# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)


class CrBaseEmployee(models.Model):

    _name = 'cr.base.employee'
    _rec_name = 'cr_base_fault_type_name'

    _description = u'问题分类'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_fault_type_name = fields.Char(string=u'问题分类名称', track_visibility='onchange',required=True)

    cr_base_fault_type_id = fields.Char(string=u'问题分类id', track_visibility='onchange',required=True)

    cr_base_refine_type_id = fields.One2many('cr.base.refine.type','cr_base_refine_type_id',string='细化分类')

class CrBaseRefineType(models.Model):

    _name = 'cr.base.refine.type'
    _rec_name = 'cr_base_refine_type_name'
    _description = u'细化分类'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_refine_type_name = fields.Char(string=u'细化分类名称', track_visibility='onchange',required=True)

    cr_base_refine_type_id = fields.Char(string=u'细化分类id', track_visibility='onchange',required=True)

    cr_base_fault_content_id = fields.One2many('cr.base.fault.content','cr_base_fault_content_id',string='问题内容')


class CrBaseFaultContent(models.Model):

    _name = 'cr.base.fault.content'
    _rec_name = 'cr_base_fault_content_name'
    _description = u'问题内容'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_fault_content_name = fields.Char(string=u'问题名称', track_visibility='onchange',required=True)

    cr_base_fault_content_id = fields.Char(string=u'问题id', track_visibility='onchange',required=True)

