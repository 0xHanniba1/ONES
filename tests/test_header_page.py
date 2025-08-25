#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.pages.header_page import HeaderPage
from config.conf import BASE_URL
import time
from loguru import logger
from utils.yaml_loaders.product_menu_loader import *


def test_product_menu_hover(setup_driver):
    """测试产品菜单悬停功能"""
    driver = setup_driver
    header_page = HeaderPage(driver)

    driver.get(BASE_URL)

    logger.info("测试产品菜单悬停...")
    header_page.hover_product_menu()
    # time.sleep(1) # 暂停 1s 看效果
    assert header_page.is_element_visible(header_page.PRODUCT_DROPDOWN)
    logger.info("产品菜单悬停测试完成")


def test_solution_menu_hover(setup_driver):
    """测试解决方案菜单悬停功能"""
    driver = setup_driver
    header_page = HeaderPage(driver)

    driver.get(BASE_URL)

    logger.info("测试解决方案菜单悬停...")
    header_page.hover_solution_menu()
    # time.sleep(1) # 暂停 1s 看效果
    assert header_page.is_element_visible(header_page.SOLUTION_DROPDOWN)
    logger.info("解决方案菜单悬停测试完成")


def test_case_menu_hover(setup_driver):
    """测试客户案例菜单悬停功能"""
    driver = setup_driver
    header_page = HeaderPage(driver)

    driver.get(BASE_URL)

    logger.info("测试客户案例菜单悬停...")
    header_page.hover_case_menu()
    # time.sleep(1) # 暂停 1s 看效果
    assert header_page.is_element_visible(header_page.CASE_DROPDOWN)
    logger.info("客户案例菜单悬停测试完成")


def test_support_menu_hover(setup_driver):
    """测试技术支持菜单悬停功能"""
    driver = setup_driver
    header_page = HeaderPage(driver)

    driver.get(BASE_URL)

    logger.info("测试技术支持菜单悬停...")
    header_page.hover_support_menu()
    # time.sleep(1) # 暂停 1s 看效果
    assert header_page.is_element_visible(header_page.SUPPORT_DROPDOWN)
    logger.info("技术支持菜单悬停测试完成")


@pytest.mark.parametrize("menu_item", ProductMenuLoader().get_product_keys())
def test_product_submenu_click(setup_driver, menu_item):
    driver = setup_driver
    driver.get(BASE_URL)

    header_page = HeaderPage(driver)

    header_page.click_product_submenu_item(menu_item)
    current_url = driver.current_url
    logger.info(f"产品 > {menu_item}点击测试完成，跳转 URL: {current_url}")

    assert current_url != BASE_URL or current_url.endswith('/')
