# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)


class CrCkRecord(models.Model):

    _name = 'cr.check.record'
    _rec_name = 'cr_check_customer_name'
    _description = u'现场检查'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_check_start_time = fields.Datetime(string=u'开始时间', track_visibility='onchange',required=True)

    cr_check_end_time = fields.Datetime(string=u'结束时间', track_visibility='onchange')

    cr_check_station = fields.Many2one('cr.base.station',string=u'所在车站', track_visibility='onchange')

    cr_check_customer_type = fields.Selection([('0',u'商业点位'),('1',u'自营点位')],string=u'客户类型', track_visibility='onchange')

    cr_check_company_name = fields.Many2one('cr.base.company',string=u'分公司名称', track_visibility='onchange')

    #to_do
    cr_check_customer_name = fields.Char(string=u'客户名称', track_visibility='onchange',required=True)

    cr_check_part = fields.Many2one('cr.base.part',string=u'属地站段', track_visibility='onchange')

    cr_check_position = fields.Many2one('cr.base.position',string=u'经营位置', track_visibility='onchange')

    cr_check_address = fields.Char(string=u'商铺地址', track_visibility='onchange')

    cr_check_checker = fields.Many2one('res.user',string=u'检查人', track_visibility='onchange')

    cr_check_check_date = fields.Datetime(string=u'检查日期', track_visibility='onchange')

#to_do 'res.user'
    cr_check_problem_type = fields.Many2one('res.user',string=u'问题分类', track_visibility='onchange')

    cr_check_refine_type = fields.Many2one('res.user',string=u'细化分类', track_visibility='onchange')

    cr_check_problem_content = fields.Many2one('res.user',string=u'问题内容', track_visibility='onchange')

    cr_check_description = fields.Text(string=u'详细描述', track_visibility='onchange')

    cr_check_problem_preview = fields.Text(string=u'问题预览', track_visibility='onchange')

    cr_check_problem_image = fields.Binary(string=u'问题图片', track_visibility='onchange')

    cr_check_problem_nature = fields.Selection([('0',u'不发牌'),('1',u'红牌'),('2',u'黄牌'),('3',u'白牌')],string=u'问题性质', track_visibility='onchange')

    cr_check_disposal_status = fields.Selection([('0',u'不发牌'),('1',u'处置中'),('2',u'待销号'),('3',u'已销号')],string=u'处置状态', track_visibility='onchange')















