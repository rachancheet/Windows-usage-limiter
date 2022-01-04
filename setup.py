import os
import shutil


name = input('Windows Username:')

shutil.move('break.pyw',f'C:/Users/{name}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup')
shutil.move('windows_usage_limiter','C:/')
