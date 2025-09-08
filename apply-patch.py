#!/bin/env python3
import os
import sys
import time
i=1
for i in range (60,72):
    patch_number=f"{i:04d}"
    print(f'正在应用第{i}个补丁')
    os.system(f"git apply {patch_number}-*.patch")
    input('- 输入任意键继续')
sys.exit(0)

