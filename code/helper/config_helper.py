#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Franplk
# 
# 配置文件读取工具类

import configparser


class ConfigHelper(object):

    @staticmethod
    def read_config(file_paths):
        config_parse = configparser.ConfigParser()
        config_parse.read(file_paths, encoding="utf-8-sig")
        config_list = [
            {
                'name': section,
                'params': dict(config_parse.items(section))
            } for section in config_parse.sections()
        ]
        return config_list


if __name__ == '__main__':
    map_config = ConfigHelper.read_config(r'E:\xxx\bat.config')
    print(map_config)
