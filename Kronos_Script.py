#!/usr/bin/env python

"""
Author: Navneet Sinha
FileName: Kronos_Script.py
Description: Python script for time stamps on KRONOS
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("<THE LINK TO KRONOS>")
uname = driver.find_element_by_name("username")
uname.send_keys("<USERNAME>")
pwd = driver.find_element_by_name("password")
pwd.send_keys("<PASSWORD>")
driver.find_element_by_id("<THE BUTTON TO BE CLICKED>").click()
driver.close()