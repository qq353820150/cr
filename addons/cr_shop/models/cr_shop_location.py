# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)


class CrSydw(models.Model):
    _name = 'cr.sydw'
    _rec_name = 'cr_sydw_customer_name'
    _description = u'商业点位'

    cr_sydw_customer_name = fields.Char(string=u'客户名称', track_visibility='onchange')
    cr_sydw_company = fields.Many2one('cr.base.company', string='所属分公司', required=True)
    cr_sydw_station = fields.Many2one('cr.base.station', string='所在车站', required=True)
    cr_sydw_part = fields.Many2one('cr.base.part', string='属站地段', required=True)
    cr_sydw_position = fields.Many2one('cr.base.position', string='经营位置', required=True)

    cr_sydw_address = fields.Char(string=u'商铺地址', track_visibility='onchange')

    cr_sydw_project_type = fields.One2many('cr.base.project.type', 'cr_base_project_type_name', string='业态类别', required=True)
    cr_sydw_project = fields.One2many('cr.base.project.type', 'cr_base_project_type_name', string='经营项目', required=True)

    cr_sydw_operator_name = fields.Char(string=u'经营者姓名', track_visibility='onchange', required=True)

    cr_sydw_operate_state = fields.Selection([('0', '营业'), ('1', '装修'), ('2', '停业'), ('3', '闲置')], string=u'经营状态', track_visibility='onchange', required=True)

    cr_sydw_operator_phone = fields.Char(string=u'经营者手机', track_visibility='onchange', required=True)
    cr_sydw_star = fields.Char(string=u'星级客户', track_visibility='onchange')
    cr_sydw_header = fields.Char(string=u'商铺日常负责人', track_visibility='onchange')
    cr_sydw_header_phone = fields.Char(string=u'商铺日常负责人手机', track_visibility='onchange')
    cr_sydw_others = fields.Char(string=u'其他从业人员', track_visibility='onchange')
    cr_sydw_qualifications = fields.Binary(string=u'经营资质', track_visibility='onchange')
    cr_sydw_EDI = fields.Binary(string=u'消电检', track_visibility='onchange')
    cr_sydw_shop_image = fields.Binary(string=u'商铺展示图', track_visibility='onchange')
    cr_sydw_customer_image = fields.Binary(string=u'客户头像', track_visibility='onchange')

    cr_sydw_start_time = fields.Date(string=u'经营开始日期', track_visibility='onchange')
    cr_sydw_end_time = fields.Date(string=u'经营结束日期', track_visibility='onchange')


