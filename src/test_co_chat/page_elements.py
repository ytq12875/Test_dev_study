#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Yang Tie Qiao"

class ContactPageElements:
    add_member_contact_menu = 'id=>menu_contacts'
    add_member_contact_list = 'id=>member_list'
    add_member_button = 'selector_selector=>.ww_operationBar .js_add_member'
    add_member_title_form = 'id=>js_upload_file'
    add_member_select_pic = 'xpath=>//*[@id="__dialog__avatarEditor__"]/div/div[2]/div/div[1]/div[2]/a/input'
    add_member_reupload = 'selector_selector=>.js_file_reupload'
    add_member_save_pic = 'selector_selector=>.js_save'
    add_member_radio = 'selector_selector=>.member_edit_item_right .ww_radio'
    add_member_mem_name = 'id=>username'
    add_member_mem_english_name = 'id=>memberAdd_english_name'
    add_member_mem_acctid = 'id=>memberAdd_acctid'
    add_member_mem_phone = 'id=>memberAdd_phone'
    add_member_mem_telephone = 'id=>memberAdd_telephone'
    add_member_mem_email = 'id=>memberAdd_mail'
    add_member_mem_address = 'id=>memberEdit_address'
    add_member_mem_title = 'id=>memberAdd_title'
    add_member_mem_other_title = 'selector_selector=>.util_d_n'
    add_member_save = 'selector_selector=>.js_btn_save'
    add_member_tips = 'id=>js_tips'


class ProfilePageElements:
    member_list_parent_name = 'selector_selector=>.member_colRight_memberTable_tr_Inactive'
    member_list_parent_disable_name = 'selector_selector=>.member_colRight_memberTable_tr_Disabled'
    member_list_son_name = 'selector_selector=>td:nth-child(2)'
    member_list_search = 'memberSearchInput'
    member_edit_button = 'selector_selector=>.js_edit'
    member_edit_page = 'selector_selector=>.member_edit'
    member_edit_phone = 'name=>mobile'
    member_edit_telephone = 'name=>ext_tel'
    member_edit_email = 'name=>alias'
    member_edit_save = 'selector_selector=>.js_save'
    member_edit_tips = 'id=>js_tips'
    member_edit_status = 'selector_selector=>.js_disable'
    member_edit_unused_do ='selector_selector=>#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue'