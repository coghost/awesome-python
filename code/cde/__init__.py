import os
import sys
import random
import datetime

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')

import logzero

from configs import Conf, LFormatter

cfg = Conf().cfg

# 检查日志配置, 是否写入文件
if cfg.get('log.enabled', False):
    logzero.logfile(
        cfg.get('log.file_pth', '/tmp/.code.log'),
        maxBytes=cfg.get('log.file_size', 5) * 1000000,
        backupCount=cfg.get('log.file_backups', 3),
        loglevel=cfg.get('log.level', 10),
    )

# bagua = '☼✔❄✖✄'
# bagua = '☰☷☳☴☵☲☶☱'  # 乾(天), 坤(地), 震(雷), 巽(xun, 风), 坎(水), 离(火), 艮(山), 兑(泽)
bagua = '🍺🍻♨️️😈☠'
formatter = LFormatter(bagua)
logzero.formatter(formatter)

from cde.dbs import MG_CFG_DICT, MG_CFG_STR, REDIS_CONF


def randint(start=0, end=100):
    return random.randint(start, end)


def now(fmt='%Y-%m-%d %H:%M:%S'):
    """
        获取当前时间的字符串表示

    :param fmt: ``默认(%Y-%m-%d %H:%M:%S)``
    :type fmt: str
    :return:
    :rtype: str
    """
    return datetime.datetime.now().strftime(fmt)
