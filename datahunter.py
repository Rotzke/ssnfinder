#!/usr/bin/env python2.7
"""Simple SSN and CC numbers parser for local files."""
import logging
import os
import re
import zipfile

import textract

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s',
                    level=logging.INFO, datefmt='%Y/%m/%dT%H:%M:%S')

FOLDER = "Identity_Finder_Test_Data"

CC_PATTERN = '''(?:
(?P<visa>4[0-9]{12}(?:[0-9]{3})?) |
(?P<mastercard>5[1-5][0-9]{14}) |
(?P<discover>6(?:011|5[0-9]{2})[0-9]{12}) |
(?P<amex>3[47][0-9]{13}) |
(?P<diners>3(?:0[0-5]|[68][0-9])[0-9]{11}) |
(?P<jcb>(?:2131|1800|35[0-9]{3})[0-9]{11})
)'''
cc_regex = re.compile(CC_PATTERN)

SSN_PATTERN = '([1-9])(?!\1{2}-\1{2}-\1{4})[1-9]{2}-[1-9]{2}-[1-9]{4}'
ssn_regex = re.compile(SSN_PATTERN)

# TODO Add zip files handler
files = [os.path.join(dp, f) for dp, dn, fn in
         os.walk(os.path.expanduser(FOLDER)) for f in fn]

# TODO Add .mdb support
for f in files:
    try:
        body = textract.process(f)
    except textract.exceptions.ExtensionNotSupported:
        logging.warning('Extension is not supported!')
    print(re.findall(cc_regex, body))
