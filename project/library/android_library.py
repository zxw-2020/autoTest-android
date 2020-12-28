from project.config.import_init import *

class android_library(object):

    def __init__(self):
        self.driver = None

    def device_get_connect(self, device=None):
        """
            连接手机的函数，connect，根据device连接制定的设备
        """
        try:
            self.driver = u2.connect(device)
        except:
            self.driver = u2.connect_usb()

    def start_app(self,pkg_name):
        self.driver.app_start(pkg_name)