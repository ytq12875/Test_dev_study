import re
from typing import List


class ListRemove:

    def __init__(self):
        pass

    def check_seq(self, local_list: List, history_list: List):
        flag = True
        for dat in local_list:
            try:
                dat = self.hit_re(dat, history_list)
                hit_index = history_list.index(dat)
                del (history_list[:hit_index + 1])
            except Exception as e:
                flag = False
        return flag

    def hit_re(self, _re, lis: List):
        ret = []
        for dat in lis:
            hit = re.findall(_re, dat)
            if hit:
                ret.append(hit[0])
        return ret[0]


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
    local_list = ["we are the second.*\(\d+ms\) pass","we are the first.*\(\d+ms\) pass"]
    lis = ListRemove()
    print(lis.check_seq(local_list, history))
