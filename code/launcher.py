#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Franplk

"""主程序入口"""

import multiprocessing
import os
import sys
from multiprocessing import Process

from PyQt5.QtWidgets import QApplication

from helper import ConfigHelper
from qt.main import SystemTray

config_list = ConfigHelper.read_config('config/bat.config')
config_list = list(filter(lambda c: c['params']['using'] == '1', config_list))


def run_qt():
    """启动QT界面应用进程"""
    qt_app = QApplication(sys.argv)

    tray_window = SystemTray(config_list)
    tray_window.display()

    sys.exit(qt_app.exec_())


def run_bat(bat_path):
    print('bat_path = {}'.format(bat_path))
    command = 'cmd.exe /c {}'.format(bat_path)
    os.system(command)


'''主进程启动'''
if __name__ == '__main__':
    # 设置支持多进程
    multiprocessing.freeze_support()
    for config in config_list:
        name, params = config.get('name'), config.get('params')
        process = Process(target=run_bat, name=name, args=(params['start_bat'],), daemon=True)
        process.start()
    run_qt()
