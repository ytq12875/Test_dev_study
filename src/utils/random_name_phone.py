#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/3/9 10:35
# @Author  :ytq
# @File    :random_name_phone.py
import random

from src.utils.random_id_card import RandomIdCard

list_tel = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '178',
            '182', '183', '184', '187', '188', '198', '130', '131', '132', '155', '156', '145', '176', '185',
            '186', '166', '133', '149', '153', '173', '177', '180', '181', '189', '199']

list_tel4 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

list_post = ['总经理', '副总裁', '第一副总裁', '副总裁助理', '首席执行官', '首席信息官', '首席财务官', '首席技术官', '首席运营官', '人力资源总监', '运营总监', '市场总监',
             '运作经理', '生产经理', '产品经理', '艺术总监', '商务总监', '内容总监', '开发总监', '政府关系', '知识总监', '工会主席', '市场总监', '首席谈判官', '质控总监',
             '研究总监', '销售总监', '客户总监', '评估总监', '测试工程师', '开发工程师', '其他工程师']

list_first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨',
                   '朱', '秦', '尤', '许', '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜',
                   '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘', '葛', '奚', '范', '彭', '郎',
                   '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐',
                   '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                   '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄',
                   '和', '穆', '萧', '尹', '姚', '邵', '舒', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧',
                   '计', '伏', '成', '戴', '谈', '宋', '茅', '庞', '熊', '纪', '屈', '项', '祝', '董', '杜', '阮',
                   '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄', '危', '江', '童', '颜', '郭', '梅', '盛',
                   '林', '刁', '钟', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万',
                   '支', '柯', '咎', '管', '卢', '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '宣', '丁',
                   '贲', '邓', '郁', '单', '杭', '洪', '包', '诸', '左', '石', '崔', '吉', '钮', '龚', '程', '嵇',
                   '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄', '加', '封', '芮', '羿', '储',
                   '靳', '汲', '邴', '糜', '松', '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山',
                   '谷', '车', '侯', '宓', '蓬', '全', '郗', '班', '仰', '秋', '仲', '伊', '宫', '宁', '仇', '栾',
                   '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '詹', '束', '龙', '叶', '幸', '司', '韶',
                   '郜', '黎', '蓟', '薄', '印', '宿', '白', '怀', '蒲', '台', '从', '鄂', '索', '咸', '籍', '赖',
                   '卓', '蔺', '屠', '蒙', '池', '乔', '阴', '胥', '能', '苍', '双', '闻', '莘', '党', '翟', '谭',
                   '贡', '劳', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '璩', '桑', '桂', '濮', '牛',
                   '寿', '通', '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿',
                   '阎', '充', '慕', '连', '茹', '习', '宦', '艾', '鱼', '容', '向', '古', '易', '慎', '戈', '廖',
                   '庚', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文', '寇', '广', '禄',
                   '阙', '东', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖',
                   '融', '冷', '訾', '辛', '阚', '那', '简', '饶', '空', '曾', '毋', '沙', '乜', '养', '鞠', '须',
                   '丰', '巢', '关', '蒯', '相', '查', '后', '红', '游', '竺', '权', '逯', '盖', '益', '桓', '公',
                   '晋', '楚', '法', '汝', '鄢', '涂', '钦', '缑', '亢', '况', '有', '商', '牟', '佘', '佴', '伯',
                   '赏', '墨', '哈', '谯', '笪', '年', '爱', '阳', '佟', '琴', '言', '福', '百', '家', '姓', '续',
                   '岳', '帅', '第五', '梁丘', '左丘', '东门', '百里', '东郭', '南门', '呼延',
                   '万俟', '南宫', '段干', '西门', '司马', '上官', '欧阳', '夏侯',
                   '诸葛', '闻人', '东方', '赫连', '皇甫', '尉迟', '公羊', '澹台',
                   '公冶', '宗政', '濮阳', '淳于', '仲孙', '太叔', '申屠', '公孙',
                   '乐正', '轩辕', '令狐', '钟离', '闾丘', '长孙', '慕容', '鲜于',
                   '宇文', '司徒', '司空', '亓官', '司寇', '子车', '颛孙', '端木',
                   '巫马', '公西', '漆雕', '壤驷', '公良', '夹谷', '宰父', '微生', '羊舌']

list_last_name = ['梦', '琪', '忆', '柳', '之', '绿', '冰', '蓝', '灵', '槐', '平', '安', '书', '翠', '翠', '风',
                  '香', '巧', '代', '云', '梦', '曼', '幼', '翠', '友', '巧', '听', '寒', '梦', '柏', '醉', '易',
                  '旋', '亦', '玉', '凌', '萱', '访', '卉', '怀', '亦', '笑', '蓝', '春', '翠', '靖', '柏', '夜',
                  '蕾', '冰', '夏', '梦', '松', '书', '雪', '乐', '枫', '念', '薇', '靖', '雁', '寻', '春', '恨',
                  '山', '从', '寒', '忆', '香', '觅', '波', '静', '曼', '凡', '旋', '以', '亦', '念', '露', '芷',
                  '蕾', '千', '兰', '新', '波', '代', '真', '新', '蕾', '雁', '玉', '冷', '卉', '紫', '山', '千',
                  '琴', '恨', '天', '傲', '芙', '盼', '山', '怀', '蝶', '冰', '兰', '山', '柏', '翠', '萱', '恨',
                  '松', '问', '旋', '从', '南', '白', '易', '问', '筠', '如', '霜', '半', '芹', '丹', '珍', '冰',
                  '彤', '亦', '寒', '寒', '雁', '怜', '云', '寻', '文', '乐', '丹', '翠', '柔', '谷', '山', '之',
                  '瑶', '冰', '露', '尔', '珍', '谷', '雪', '乐', '萱', '涵', '菡', '海', '莲', '傲', '蕾', '青',
                  '槐', '冬', '儿', '易', '梦', '惜', '雪', '宛', '海', '之', '柔', '夏', '青', '亦', '瑶', '妙',
                  '菡', '春', '竹', '痴', '梦', '紫', '蓝', '晓', '巧', '幻', '柏', '元', '风', '冰', '枫', '访',
                  '蕊', '南', '春', '芷', '蕊', '凡', '蕾', '凡', '柔', '安', '蕾', '天', '荷', '含', '玉', '书',
                  '兰', '雅', '琴', '书', '瑶', '春', '雁', '从', '安', '夏', '槐', '念', '芹', '怀', '萍', '代',
                  '曼', '幻', '珊', '谷', '丝', '秋', '翠', '白', '晴', '海', '露', '代', '荷', '含', '玉', '书',
                  '蕾', '听', '白', '访', '琴', '灵', '雁', '秋', '春', '雪', '青', '乐', '瑶', '含', '烟', '涵',
                  '双', '平', '蝶', '雅', '蕊', '傲', '之', '灵', '薇', '绿', '春', '含', '蕾', '从', '梦', '从',
                  '蓉', '初', '丹', '听', '兰', '听', '蓉', '语', '芙', '夏', '彤', '凌', '瑶', '忆', '翠', '幻',
                  '灵', '怜', '菡', '紫', '南', '依', '珊', '妙', '竹', '访', '烟', '怜', '蕾', '映', '寒', '友',
                  '绿', '冰', '萍', '惜', '霜', '凌', '香', '芷', '蕾', '雁', '卉', '迎', '梦', '元', '柏', '代',
                  '萱', '紫', '真', '千', '青', '凌', '寒', '紫', '安', '寒', '安', '怀', '蕊', '秋', '荷', '涵',
                  '雁', '以', '山', '凡', '梅', '盼', '曼', '翠', '彤', '谷', '冬', '新', '巧', '冷', '安', '千',
                  '萍', '冰', '烟', '雅', '阳', '友', '绿', '南', '松', '诗', '云', '飞', '风', '寄', '灵', '书',
                  '芹', '幼', '蓉', '以', '蓝', '笑', '寒', '忆', '寒', '秋', '烟', '芷', '巧', '水', '香', '映',
                  '之', '醉', '波', '幻', '莲', '夜', '山', '芷', '卉', '向', '彤', '小', '玉', '幼', '南', '凡',
                  '梦', '尔', '曼', '念', '波', '迎', '松', '青', '寒', '笑', '天', '涵', '蕾', '碧', '菡', '映',
                  '秋', '盼', '烟', '忆', '山', '以', '寒', '寒', '香', '小', '凡', '代', '亦', '梦', '露', '映',
                  '波', '友', '蕊', '寄', '凡', '怜', '蕾', '雁', '枫', '水', '绿', '曼', '荷', '笑', '珊', '寒',
                  '珊', '谷', '南', '慕', '儿', '夏', '岚', '友', '儿', '小', '萱', '紫', '青', '妙', '菱', '冬',
                  '寒', '曼', '柔', '语', '蝶', '青', '筠', '夜', '安', '觅', '海', '问', '安', '晓', '槐', '雅',
                  '山', '访', '云', '翠', '容', '寒', '凡', '晓', '绿', '以', '菱', '冬', '云', '含', '玉', '访',
                  '枫', '含', '卉', '夜', '白', '冷', '安', '灵', '竹', '醉', '薇', '元', '珊', '幻', '波', '盼',
                  '夏', '元', '瑶', '迎', '曼', '水', '云', '访', '琴', '谷', '波', '乐', '之', '笑', '白', '之',
                  '山', '妙', '海', '紫', '霜', '平', '夏', '凌', '旋', '孤', '丝', '怜', '寒', '向', '萍', '凡',
                  '松', '青', '丝', '翠', '安', '如', '天', '凌', '雪', '绮', '菱', '代', '云', '南', '莲', '寻',
                  '南', '春', '文', '香', '薇', '冬', '灵', '凌', '珍', '采', '绿', '天', '春', '沛', '文', '紫',
                  '槐', '幻', '柏', '采', '文', '春', '梅', '雪', '旋', '盼', '海', '映', '梦', '安', '雁', '映',
                  '容', '凝', '阳', '访', '风', '天', '亦', '平', '绿', '香', '风', '霜', '雪', '柳', '雪', '靖',
                  '白', '梦', '飞', '绿', '如', '波', '又', '晴', '友', '香', '菱', '冬', '亦', '问', '妙', '春',
                  '海', '冬', '半', '安', '平', '春', '幼', '柏', '秋', '灵', '凝', '芙', '念', '烟', '白', '山',
                  '从', '灵', '尔', '芙']


def get_name():
    first_name = random.choice(list_first_name)
    last_name = ''.join(random.sample(list_last_name, random.randint(1, 2)))
    return first_name + last_name


def get_phone():
    str_phone = ""
    for i in range(8):
        phone_part = random.choice(list_tel4)
        str_phone += phone_part
    return random.choice(list_tel) + str_phone


def get_post():
    return random.choice(list_post)


if __name__ == '__main__':
    name = ""
    while len(name) < 4:
        id_info = RandomIdCard().get_id_card()
        name = get_name()
        post = get_post()
        id_card = id_info[0]
        add = id_info[1]
        print(name + " 身份证号为：" + id_card + "，电话为 " + get_phone() + "，来自于" + add + ", 职位为：" + post)
