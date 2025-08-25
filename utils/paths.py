#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

# 项目根目录
ROOT = Path(__file__).resolve().parents[1]

# 一级目录
CONFIG = ROOT / 'config'
DATA = ROOT / 'data'
REPORTS = ROOT / 'reports'
TESTS = ROOT / 'tests'
UTILS = ROOT / 'utils'
SRC = ROOT / 'src'

# src 子目录
CORE = SRC / 'core'
PAGES = SRC / 'pages'

# 使用示例
if __name__ == '__main__':
    print("项目结构:")
    print(f"├── 项目根目录: {ROOT}")
    print(f"├── 配置目录: {CONFIG}")
    print(f"├── 数据目录: {DATA}")
    print(f"├── 报告目录: {REPORTS}")
    print(f"├── 测试目录: {TESTS}")
    print(f"├── 工具目录: {UTILS}")
    print(f"└── 源码目录: {SRC}")
    print(f"    ├── 核心模块: {CORE}")
    print(f"    └── 页面模块: {PAGES}")
