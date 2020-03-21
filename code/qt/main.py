#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Franplk
#
# 请描述文件功能

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtWidgets import QWidget

from qt.events import PageAction
from qt.events import ExitAction


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
        # name = 启动Eova
        # icon =
        # path = E:\develop\神华项目\eova - pro - release\eova.bat
        # page = http: // localhost: 80
        for config in config_list:
            tray_menu.addAction(PageAction(config, self))
        tray_menu.addAction(ExitAction(self))
        self.tray.setContextMenu(tray_menu)

    def display(self):
        """
        icon的值: 0-没有图标  1-是提示  2-是警告  3-是错误
        """
        self.tray.show()
        self.tray.showMessage(u"启动成功", '请通过右键操作')
