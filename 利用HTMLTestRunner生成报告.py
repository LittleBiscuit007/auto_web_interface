import time

from auto_web_interface import HTMLTestRunner
import unittest

discover_path = './'
discover = unittest.defaultTestLoader.discover(discover_path, pattern="automation_web_interface.py")

if __name__ == '__main__':
    file_time = time.strftime('%Y-%m-%d %H-%M-%S')
    file_path = './HTML_log/'
    with open(file_path+file_time+'_Redfish.html', 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='HS BMC Redfish', description="接口测试")
        runner.run(discover)
