#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
dicts={"name":"lucy","sex":"boy"}

json_dicts=json.dumps(dicts,indent=4)
print(json_dicts)