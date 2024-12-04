import os

from datetime import datetime

from chan.Common.CEnum import DATA_FIELD, KL_TYPE
from chan.Common.ChanException import CChanException, ErrCode
from chan.Common.CTime import CTime
from chan.Common.func_util import str2float
from chan.KLine.KLine_Unit import CKLine_Unit

from .CommonStockAPI import CCommonStockApi

def parse_time_column(inp):
    # 20210902113000000
    # 2021-09-13
    if len(inp) == 10:
        year = int(inp[:4])
        month = int(inp[5:7])
        day = int(inp[8:10])
        hour = minute = 0
    elif len(inp) == 17:
        year = int(inp[:4])
        month = int(inp[4:6])
        day = int(inp[6:8])
        hour = int(inp[8:10])
        minute = int(inp[10:12])
    elif len(inp) == 19:
        year = int(inp[:4])
        month = int(inp[5:7])
        day = int(inp[8:10])
        hour = int(inp[11:13])
        minute = int(inp[14:16])
    else:
        raise Exception(f"unknown time column from csv:{inp}")
    return CTime(year, month, day, hour, minute)

class DataFrame_API(CCommonStockApi):
    def __init__(self, code, k_type=KL_TYPE.K_DAY, begin_date=None, end_date=None, autype=None):
        self.dataframe = None
        super(DataFrame_API, self).__init__(code, k_type, begin_date, end_date, autype)

    def set_dataframe(self, dataframe):
        self.dataframe = dataframe


    def get_kl_data(self):
        dict_list = self.dataframe.to_dict('records')
        # 遍历字典列表
        for index, row_dict in enumerate(dict_list):
            time_str = row_dict['date'].strftime('%Y-%m-%d %H:%M:%S')
            row_dict[DATA_FIELD.FIELD_TIME] = parse_time_column(time_str)
            print(f"第 {index} 行的数据：{row_dict}")
            yield CKLine_Unit(row_dict)

    def SetBasciInfo(self):
        pass

    @classmethod
    def do_init(cls):
        pass

    @classmethod
    def do_close(cls):
        pass
