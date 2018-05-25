# pyqualys


pyqualys is simple, easy Python api client library for Qualys users. Currently this is in working process, but there are few features are work.


Example
-----------
* Add Asset
```
# -*- coding: utf-8 -*-
import pyqualys

qualys = pyqualys.QualysAPI(username="admin",
                         password="admin",
                         host="https://qualys.com/")

service = qualys.service("vulnerability")
asset = service.add_asset(title="myLinux", ips="10.10.10.1")
print("Response", asset)
```
More example in main.py and example/ dir
