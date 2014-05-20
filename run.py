#!/usr/bin/env python

import s3cacher

cache = s3cacher.Cacher

cache.upload("test.html","http://www.co.bibb.ga.us/VotersAuto/ExternalVoters/ScrollingResults.asp")