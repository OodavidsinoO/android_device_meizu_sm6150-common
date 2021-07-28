# Copyright (C) 2009 The Android Open Source Project
# Copyright (C) 2020 The MoKee Open Source Project
#
# SPDX-License-Identifier: Apache-2.0
#

import re

def FullOTA_Assertions(info):
  AddModemAssertion(info)
  return

def IncrementalOTA_Assertions(info):
  AddModemAssertion(info)
  return

def AddModemAssertion(info):
  android_info = info.input_zip.read("OTA/android-info.txt")
  m = re.search(r'require\s+version-modem\s*=\s*(.+)', android_info)
  if m:
    version = m.group(1).rstrip()
    if len(version) and '*' not in version:
      cmd = 'assert(meizu_sm6150.verify_modem("' + version + '") == "1");'
      info.script.AppendExtra(cmd)
  return
