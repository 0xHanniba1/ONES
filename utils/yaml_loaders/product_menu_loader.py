#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.yaml_loaders.base_loader import BaseLoader


class ProductMenuLoader(BaseLoader):
    def __init__(self):
        super().__init__("product_menu.yaml")
    
    def get_project_info(self):
        """获取project的信息，包括name, desc, group, path"""
        data = self._load_data()
        products = data.get('products', {})
        return products.get('project')
    
    def get_project_path(self):
        """获取project的路径"""
        project_info = self.get_project_info()
        return project_info.get('path') if project_info else None
    
    def get_all_products(self):
        """获取所有产品信息"""
        data = self._load_data()
        return data.get('products', {})
    
    def get_product_by_name(self, product_name):
        """根据产品名称获取产品信息"""
        products = self.get_all_products()
        return products.get(product_name)
    
    def get_product_keys(self):
        """从YAML中获取所有产品的键名"""
        products = self.get_all_products()
        return list(products.keys())

# a = ProductMenuLoader()
# print(a.get_product_keys())
# print(a.get_all_products())