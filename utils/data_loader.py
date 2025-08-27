#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import yaml


def read_excel(file_path, sheet_name=0, columns=None):
    """
    读取Excel文件，每行数据为一个字典
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns)
    df = df.fillna('')  # 处理空值
    return df.to_dict('records')


def read_csv(file_path, columns=None):
    """
    读取CSV文件，每行数据为一个字典
    """
    df = pd.read_csv(file_path, usecols=columns)
    df = df.fillna('')  # 处理空值
    return df.to_dict('records')


def read_excel_as_list(file_path, sheet_name=0, columns=None):
    """
    读取Excel文件，每行数据为一个列表
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns)
    df = df.fillna('')
    return df.values.tolist()


if __name__ == '__main__':
    pass
