import re
from typing import List


class ListRemove:

    def __init__(self):
        pass

    def check_seq(self, local_list: List, history_list: List):
        flag = True
        rst_list = []
        for dat in local_list:
            dat_rst = self.hit_re(dat, history_list)
            if len(dat_rst) > 0:
                hit_index = history_list.index(dat_rst[0])
                del (history_list[:hit_index + 1])
                flag_temp = True
            else:
                flag_temp = False
            rst_list.append(flag_temp)
        if False in rst_list:
            flag = False
        return flag

    def check_seq_not(self, local_list: List, history_list: List):
        flag = True
        rst_list = []
        for dat in local_list:
            dat_rst = self.hit_re(dat, history_list)
            if len(dat_rst) > 0:
                flag_temp = False
            else:
                flag_temp = True
            rst_list.append(flag_temp)
        if False in rst_list:
            flag = False
        return flag

    def hit_re(self, _re, lis: List):
        ret = []
        for dat in lis:
            hit = re.findall(_re, dat)
            if hit:
                ret.append(hit[0])
        return ret


if __name__ == '__main__':
    history = [
        "we are the first ................(12ms) pass",
        "done open door ................(112ms) pass",
        "done close door ................(132ms) pass",
        "we are the second ................(11ms) pass",
        "done open door ................(154ms) pass",
        "done close door ................(121ms) pass",
        "we are the third ................(123ms) pass",
        "done open door ................(18ms) pass",
        "done close door ................(133ms) pass",
        "we are the end ................(133ms) pass"
    ]
    local_list = ["we are the first.*\(\d+ms\) pass","we are the second.*\(\d+ms\) pass"]
    lis = ListRemove()
    print(lis.check_seq_not(local_list, history))
