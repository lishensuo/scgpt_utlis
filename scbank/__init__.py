# scBank is the single cell data bank toolbox for building up large-scale single
# cell dataset to allow flexible cell data access and manipulation across studies,
# and to support large-scale computing.
import logging
import sys

# 创建一个日志记录器
logger = logging.getLogger("scBank")
# 设置最低日志级别
logger.setLevel(logging.INFO)

# 创建一个控制台处理器
handler = logging.StreamHandler(sys.stdout) 
handler.setLevel(logging.INFO) # 只在控制台显示INFO及以上级别的日志

# 定义日志格式
formatter = logging.Formatter(
    "%(name)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S"
)
# 将格式应用到处理器
handler.setFormatter(formatter)
# 将处理器添加到日志记录器
logger.addHandler(handler)

from .databank import DataBank  # scabnk.DataBank
from .data import *
from .setting import Setting
from .postprocess import add_cls # scbank.add_cls