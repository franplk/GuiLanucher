#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date: 2020-03-22
# @Author Franplk

import os

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QAction


class StopAction(QAction):
    def __init__(self, name, stop_bat, parent=None):
        menu_name = '关闭{}'.format(name)
        icon = QIcon('resources/icons/exit.png')
        super().__init__(icon, menu_name, parent)
        self.stop_bat = stop_bat
        self.triggered.connect(self.stop_system)

    def stop_system(self):
        os.system(self.stop_bat)
        pass
