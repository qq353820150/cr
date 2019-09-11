# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)


class CrCcLdjh(models.Model):

    _name = 'cr.cc.ldjh'
    _rec_name = 'cr_ccls_news_title'
    _description = u'领导讲话'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_ccls_news_title = fields.Char(string=u'新闻标题', track_visibility='onchange',required=True)

    cr_ccls_datetime = fields.Datetime(string=u'编辑时间', track_visibility='onchange')

    cr_ccls_introduction = fields.Char(string=u'简介', track_visibility='onchange')

    cr_ccls_filepath = fields.Binary(string=u'文件地址', track_visibility='onchange')

    cr_ccls_order = fields.Integer(string=u'排序值', track_visibility='onchange')

    cr_ccls_content = fields.Text(string=u'内容', track_visibility='onchange')
