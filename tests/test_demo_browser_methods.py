import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from unittest.mock import patch, MagicMock
from LearningSelenium.demo_browser_methods import DemoBrowserMethods

class TestDemoBrowserMethods(unittest.TestCase):
    def setUp(self):
        self.demo = DemoBrowserMethods()

    @patch('selenium.webdriver.Chrome')
    @patch('selenium.webdriver.chrome.service.Service')
    @patch('webdriver_manager.chrome.ChromeDriverManager')
    def test_browser_methods_navigation(self, mock_driver_manager, mock_service, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_driver_manager().install.return_value = "path/to/chromedriver"

        self.demo.demo_browser_methods()

        mock_driver.get.assert_called_once_with("https://training.rcvacademy.com/m")
        mock_driver.maximize_window.assert_called_once()
        mock_driver.fullscreen_window.assert_called_once()
        mock_driver.refresh.assert_called_once()
        mock_driver.minimize_window.assert_called_once()
        mock_driver.quit.assert_called_once()

    @patch('selenium.webdriver.Chrome')
    @patch('selenium.webdriver.chrome.service.Service')
    @patch('webdriver_manager.chrome.ChromeDriverManager')
    def test_browser_methods_properties(self, mock_driver_manager, mock_service, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_driver.current_url = "https://training.rcvacademy.com/m"
        mock_driver.title = "RCV Academy"

        with patch('builtins.print') as mock_print:
            self.demo.demo_browser_methods()
            mock_print.assert_any_call("https://training.rcvacademy.com/m")
            mock_print.assert_any_call("RCV Academy")

    @patch('selenium.webdriver.Chrome')
    @patch('selenium.webdriver.chrome.service.Service')
    @patch('webdriver_manager.chrome.ChromeDriverManager')
    def test_browser_methods_element_interaction(self, mock_driver_manager, mock_service, mock_chrome):
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_element = MagicMock()
        mock_driver.find_element.return_value = mock_element

        self.demo.demo_browser_methods()

        mock_driver.find_element.assert_called_with(By.linktext, "ALL COURSES")
        mock_element.click.assert_called_once()

if __name__ == '__main__':
    unittest.main()
