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

CC_PATTERN = '''(?:4[0-9]{12}(?:[0-9]{3})?|(?:5[1-5][0-9]{2}
|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}
|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011
|5[0-9]{2})[0-9]{12}|(?:2131|1800|35\d{3})\d{11})'''
cc_regex = re.compile(CC_PATTERN)

SSN_PATTERN = '''^(?!b(d)1+-(d)1+-(d)1+b)(?!123-45-6789
|219-09-9999|078-05-1120)(?!666|000|9d{2})d{3}-(?!00)d{2}-(?!0{4})d{4}$'''
ssn_regex = re.compile(SSN_PATTERN)


# def unpack_zip(filename, dir_to, test_id, test_run_id):
#     def get_root_dir_from_zip(zipIO):
#         zip_inside = (x for x in zipIO.namelist())
#         zip_first = next(zip_inside)
#         first_dir = zip_first[:zip_first.find('/') + 1]
#         return first_dir
#
#     with zipfile.ZipFile(filename, 'r') as z:
#         dir = get_root_dir_from_zip(z)
#         dirname = check_dir(dir_to, test_id, test_run_id)
#         z.extractall(dirname)
#     return dirname + dir

# TODO Add zip files handler
files = [os.path.join(dp, f) for dp, dn, fn in
         os.walk(os.path.expanduser(FOLDER)) for f in fn]

# TODO Add .mdb support
for f in files:
    if 'fake_ssn.txt' in f:
        try:
            body = textract.process(f)
        except textract.exceptions.ExtensionNotSupported:
            logging.warning('Extension is not supported!')
        print(ssn_regex.findall(body))
