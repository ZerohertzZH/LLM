import sys
import os

# 当前文件所在的目录
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# 获取项目的根目录
BASE_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))
# log目录的路径
LOG_DIR = os.path.join(BASE_DIR, "log")
# output目录的路径
OUTPUT_DIR = os.path.join(BASE_DIR, "output")