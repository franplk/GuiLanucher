#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Franplk
#
# 请描述文件功能

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtWidgets import QWidget

from qt.events import ExitAction
from qt.events import OpenAction
from qt.events import StopAction


class SystemTray(QWidget):
    """只有托盘"""

    def __init__(self, config_list):
        super().__init__()
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon('icons/app.ico'))
        self.add_menu(config_list)

    def add_menu(self, config_list):
        """托盘菜单"""
        tray_menu = QMenu()
        # 添加菜单
        for config in config_list:
            params = config.get('params')
            sys_name = params.get('name')
            tray_menu.addAction(OpenAction(params, self))
            stop_bat = params.get('stop_bat', None)
            if stop_bat:
                tray_menu.addAction(StopAction(sys_name, stop_bat, self))
        tray_menu.addAction(ExitAction(self))
        self.tray.setContextMenu(tray_menu)

    def display(self):
        """icon的值: 0-没有图标  1-是提示  2-是警告  3-是错误"""
        self.tray.show()
        self.tray.showMessage(u"启动成功", '请通过右键操作')
