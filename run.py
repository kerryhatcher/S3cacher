#!/usr/bin/env python

import s3cacher

cache = s3cacher.Cacher

cache.upload("test.html","http://example.com/test.asp")