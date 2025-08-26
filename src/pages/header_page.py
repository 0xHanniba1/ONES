#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from src.core.base_page import BasePage
import time


class HeaderPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "a.oac-cursor-pointer img[src*='ones-logo']")

    PRODUCT_MENU = (By.ID, "header_menu_menu_product")
    PRODUCT_DROPDOWN = (By.CSS_SELECTOR, "#header_menu_menu_product div.ease-in-panel-content")

    SOLUTION_MENU = (By.ID, "header_menu_menu_solution")
    SOLUTION_DROPDOWN = (By.CSS_SELECTOR, "#header_menu_menu_solution div.ease-in-panel-content")

    CASE_MENU = (By.ID, "header_menu_menu_customer")
    CASE_DROPDOWN = (By.CSS_SELECTOR, "#header_menu_menu_customer div.ease-in-panel-content")

    SUPPORT_MENU = (By.ID, "header_menu_menu_resource")
    SUPPORT_DROPDOWN = (By.CSS_SELECTOR, "#header_menu_menu_resource div.ease-in-panel-content")

    PRICING_MENU = (By.ID, "header_menu_menu_price")
    INSTALL_BTN = (By.CSS_SELECTOR, "div.oac-hidden button.ones-button.ones-button-default")

    PHONE_BTN = (By.CSS_SELECTOR, "div.oac-hidden button.ones-button-default")
    LOGIN_BTN = (By.XPATH, "//a[normalize-space()='登录']")
    FREE_TRIAL_BTN = (By.XPATH, "//div[normalize-space()='免费试用']")

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)

    def click_logo(self):
        self.click(self.LOGO)

    def hover_menu(self, menu_locator, dropdown_locator):
        """
        通用菜单悬浮方法
        1.确认：主菜单可见
        2.执行：悬浮操作
        3.等待：下拉面板出现
        """
        self.wait_for_element_visible(menu_locator)
        self.hover_over_element(menu_locator)
        self.wait_for_element_visible(dropdown_locator)

    def hover_product_menu(self):
        """悬停产品菜单"""
        self.hover_menu(self.PRODUCT_MENU, self.PRODUCT_DROPDOWN)

    def hover_solution_menu(self):
        """悬停解决方案菜单"""
        self.hover_menu(self.SOLUTION_MENU, self.SOLUTION_DROPDOWN)

    def hover_case_menu(self):
        """悬停客户案例菜单"""
        self.hover_menu(self.CASE_MENU, self.CASE_DROPDOWN)

    def hover_support_menu(self):
        """悬停技术支持菜单"""
        self.hover_menu(self.SUPPORT_MENU, self.SUPPORT_DROPDOWN)

    def click_pricing(self):
        self.click(self.PRICING_MENU)

    def click_install(self):
        self.click(self.INSTALL_BTN)

    def click_phone(self):
        self.click(self.PHONE_BTN)

    def click_login(self):
        self.click(self.LOGIN_BTN)

    def click_free_trial(self):
        self.click(self.FREE_TRIAL_BTN)


    def click_product_submenu_item(self, item_text):
        self.hover_product_menu()
        # time.sleep(1)

        submenu_item = (By.CSS_SELECTOR, f"#header_menu_menu_product a[href='/products/{item_text}']")
        self.click(submenu_item)