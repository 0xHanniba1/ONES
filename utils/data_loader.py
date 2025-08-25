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


def read_yaml_as_list(file_path, section=None):
    """
    读取YAML文件，每行数据为一个列表，类似pandas read_excel
    
    Args:
        file_path: YAML文件路径
        section: 可选，指定要提取的节点路径，如 "解决方案" 或 ["解决方案", "业务解决方案"]
    """
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # 如果指定了section，先提取对应的数据但保留路径
    section_path = []
    if section is not None:
        if isinstance(section, str):
            section = [section]

        section_path = section[:]  # 保存section路径
        for key in section:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return []  # 如果路径不存在，返回空列表

    def flatten_to_list(data, path=None):
        if path is None:
            path = []
        result = []
        if isinstance(data, dict):
            for key, value in data.items():
                result.extend(flatten_to_list(value, path + [key]))
        elif isinstance(data, list):
            for item in data:
                result.append(path + [item])
        else:
            result.append(path + [data])
        return result

    return flatten_to_list(data)


if __name__ == '__main__':
    from utils.paths import DATA

    print(read_yaml_as_list(DATA / "menus.yaml", section='解决方案'))
    print(read_yaml_as_list(DATA / "menus.yaml"))
