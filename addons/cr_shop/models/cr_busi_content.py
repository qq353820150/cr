# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError


import logging
_logger = logging.getLogger(__name__)


class CrSydwCyry(models.Model):
    _name = 'cr.sydw.cyry'
    _rec_name = 'cr_cyry_name'
    _description = u'从业人员'
    cr_cyry_business_name= fields.Char(string=u'商户名称', track_visibility='onchange')
    cr_cyry_name= fields.Char(string=u'姓名', track_visibility='onchange')
    cr_cyry_gender= fields.Char(string=u'性别', track_visibility='onchange')
    cr_cyry_number= fields.Char(string=u'工号', track_visibility='onchange')
    cr_cyry_health_validity= fields.Char(string=u'健康证有效期', track_visibility='onchange')
    cr_cyry_phone= fields.Char(string=u'手机', track_visibility='onchange')
    cr_cyry_score= fields.Char(string=u'入职考试成绩', track_visibility='onchange')
    cr_cyry_remark= fields.Char(string=u'备注', track_visibility='onchange')

    cr_cyry_health_start = fields.Date(string=u'健康证有效期起', track_visibility='onchange')
    cr_cyry_health_end = fields.Date(string=u'健康证有效期止', track_visibility='onchange')
    cr_cyry_badge_start = fields.Date(string=u'胸卡有效期起', track_visibility='onchange')
    cr_cyry_badge_end = fields.Date(string=u'胸卡有效期止', track_visibility='onchange')

    cr_cyry_badge = fields.Binary(string=u'胸卡', track_visibility='onchange')
    cr_cyry_health_certificate = fields.Binary(string=u'健康证', track_visibility='onchange')

    cr_cyry_post = fields.Selection([('0', '店长'), ('1', '经理')], string=u'职务', track_visibility='onchange')

class CrSydwYdss(models.Model):
    _name = 'cr.sydw.ydss'
    _rec_name = 'cr_ydss_device_name'
    _description = u'用电设施'

    cr_ydss_device_name= fields.Char(string=u'设备名称', track_visibility='onchange')
    cr_ydss_business_name= fields.Char(string=u'商户名称', track_visibility='onchange')
    cr_ydss_device_model= fields.Char(string=u'设备型号', track_visibility='onchange')
    cr_ydss_voltage= fields.Char(string=u'额定电压（V）', track_visibility='onchange')
    cr_ydss_power= fields.Char(string=u'额定功率（W）', track_visibility='onchange')
    cr_ydss_electricity= fields.Char(string=u'额定电流（A）', track_visibility='onchange')
    cr_ydss_use= fields.Char(string=u'用途', track_visibility='onchange')
    cr_ydss_header= fields.Char(string=u'负责人', track_visibility='onchange')
    cr_ydss_main_power= fields.Char(string=u'总电源', track_visibility='onchange')
    cr_ydss_ambient_temp= fields.Char(string=u'环境温度', track_visibility='onchange')
    cr_ydss_damaged= fields.Char(string=u'有无破损', track_visibility='onchange')
    cr_ydss_check_cycle= fields.Char(string=u'检查周期', track_visibility='onchange')
    cr_ydss_clean= fields.Char(string=u'清洗公司', track_visibility='onchange')
    cr_ydss_surface_temp= fields.Char(string=u'表面温度', track_visibility='onchange')
    cr_ydss_dielectric= fields.Char(string=u'绝缘强度', track_visibility='onchange')
    cr_ydss_checker= fields.Char(string=u'检查人', track_visibility='onchange')
    cr_ydss_remark= fields.Char(string=u'备注', track_visibility='onchange')

    cr_ydss_install_date = fields.Date(string=u'安装日期', track_visibility='onchange')
    cr_ydss_cleaning_time = fields.Date(string=u'清洗时间', track_visibility='onchange')

    cr_ydss_running_state = fields.Binary(string=u'运行状态', track_visibility='onchange')


class CrSydwXfss(models.Model):
    _name = 'cr.sydw.xfss'
    _rec_name = 'cr_xfss_device_name'
    _description = u'消防设施'

    cr_xfss_device_name= fields.Char(string=u'设备名称', track_visibility='onchange')
    cr_xfss_business_name= fields.Char(string=u'商户名称', track_visibility='onchange')
    cr_xfss_device_model= fields.Char(string=u'设备型号', track_visibility='onchange')
    cr_xfss_header= fields.Char(string=u'负责人', track_visibility='onchange')
    cr_xfss_manufacturer= fields.Char(string=u'生产厂家', track_visibility='onchange')
    cr_xfss_exit_number= fields.Char(string=u'出厂编号', track_visibility='onchange')
    cr_xfss_defend_cycle= fields.Char(string=u'维护周期', track_visibility='onchange')
    cr_xfss_check_cycle= fields.Char(string=u'检查周期', track_visibility='onchange')
    cr_xfss_age_limit= fields.Char(string=u'准用年限', track_visibility='onchange')
    cr_xfss_remark= fields.Char(string=u'备注', track_visibility='onchange')

    cr_xfss_install_date = fields.Date(string=u'安装日期', track_visibility='onchange')


