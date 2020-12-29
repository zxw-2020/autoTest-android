from project.config.config_init import *
from project.library.library_init import *

print(get_Test_Steps('连接设备'))
print(get_Test_Steps('启动app'))
eval('device.device_get_connect()')
eval('device.start_app(pkg_name)')