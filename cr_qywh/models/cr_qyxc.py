# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)

class CrCcQyxc(models.Model):

    _name = 'cr.cc.qyxc'
    _rec_name = 'cr_ccxc_introduction'
    _description = u'企业相册'
    # _inherit = ['mail.thread', 'ir.needaction_mixin']  # 备注信息轨迹记录

    cr_ccxc_introduction = fields.Char(string=u'简介', track_visibility='onchange')

    cr_ccxc_photo = fields.Binary(string=u'图片', track_visibility='onchange')

    cr_ccxc_groupname = fields.Char(string=u'分组名称', track_visibility='onchange')

    cr_ccxc_creater = fields.Many2one('res.user',string=u'创建人', track_visibility='onchange')
