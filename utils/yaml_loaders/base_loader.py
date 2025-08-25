#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
from utils.paths import DATA


class BaseLoader:
    def __init__(self, yaml_filename):
        self.yaml_path = os.path.join(DATA, yaml_filename)
        self._data = None
    
    def _load_data(self):
        """加载YAML配置文件"""
        if self._data is None:
            with open(self.yaml_path, 'r', encoding='utf-8') as file:
                self._data = yaml.safe_load(file)
        return self._data