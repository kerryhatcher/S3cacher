S3cacher
========

Simple script to download dynamic html page and upload it to s3


## Requires

- Fabric==1.8.3
- PyYAML==3.11
- boto==2.28.0
- ecdsa==0.11
- fabric-virtualenv==0.2.1
- paramiko==1.12.4
- pycrypto==2.6.1

## Usage

```python
#!/usr/bin/env python

import s3cacher

cache = s3cacher.Cacher

cache.upload("cachedResults.html","http://www.myweb.us/Results.asp")
```