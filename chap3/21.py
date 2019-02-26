import gzip
import json
import re

with gzip.open("jawiki-country.json.gz", "rt") as f:
    for i in f:
        obj=json.loads(i)

        if re.match(obj['title'], r'イギリス'):
            text = obj['text']
            pattern = re.compile(r'.*\[\[Category:.*\]\].*', re.MULTILINE)
            for c in pattern.findall(text):
                print(c)

