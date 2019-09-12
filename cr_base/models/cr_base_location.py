# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)


class CrBaseCompany(models.Model):

    _name = 'cr.base.company'
    _rec_name = 'cr_base_company_name'
    _description = u'分公司信息'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_company_name = fields.Char(string=u'分公司名称', track_visibility='onchange',required=True)

    cr_base_company_id = fields.Char(string=u'分公司id', track_visibility='onchange',required=True)

    cr_base_part_id = fields.One2many('cr.base.part','cr_base_company_id',string='属地站段')

class CrBasePart(models.Model):

    _name = 'cr.base.part'
    _rec_name = 'cr_base_part_name'
    _description = u'属地站段'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_part_name = fields.Char(string=u'站段名称', track_visibility='onchange',required=True)

    cr_base_part_id = fields.Char(string=u'站段id', track_visibility='onchange',required=True)

    cr_base_station_id = fields.One2many('cr.base.station','cr_base_part_id',string='车站')

    cr_base_company_id = fields.Many2one('cr.base.company',  string='分公司')

class CrBaseStation(models.Model):

    _name = 'cr.base.station'
    _rec_name = 'cr_base_station_name'
    _description = u'所在车站'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_station_name = fields.Char(string=u'车站名称', track_visibility='onchange',required=True)

    cr_base_station_id = fields.Char(string=u'车站id', track_visibility='onchange',required=True)

    cr_base_position_id = fields.One2many('cr.base.position','cr_base_station_id',string='经营位置')

    cr_base_part_id = fields.Many2one('cr.base.part',string='属地站段')

class CrBasePosition(models.Model):

    _name = 'cr.base.position'
    _rec_name = 'cr_base_position_name'
    _description = u'经营位置'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_base_position_name = fields.Char(string=u'位置名称', track_visibility='onchange',required=True)

    cr_base_position_id = fields.Char(string=u'位置id', track_visibility='onchange',required=True)

    cr_base_station_id = fields.Many2one('cr.base.station',string='所在车站')