#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Franplk

"""主程序入口"""

import multiprocessing
import os
import sys

from PyQt5.QtWidgets import QApplication

from helper import ConfigHelper
from qt.main import SystemTray

config_list = ConfigHelper.read_config('config/bat.config')
config_list = list(filter(lambda c: c['using'] == '1', config_list))


def run_qt():
    """启动QT界面应用进程"""
    qt_app = QApplication(sys.argv)

    tray_window = SystemTray(config_list)
    tray_window.display()

    sys.exit(qt_app.exec_())


def run_bat(bat_path):
    print('bat_path = '.format(bat_path))
    os.system(bat_path)


'''主进程启动'''
if __name__ == '__main__':
    # 设置支持多进程
    multiprocessing.freeze_support()

    # 开启多进程
    process_length = len(config_list) + 1
    process_pool = multiprocessing.Pool(process_length)
    process_pool.apply_async(run_qt)
    for config in config_list:
        process_pool.apply_async(run_bat, args=(config['start_bat'],))
    process_pool.close()

    # 使得主进程挂起而不退出
    process_pool.join()
