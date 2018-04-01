#!/usr/bin/env python3

import sys, os

trace = True
dirname = sys.argv[1]
exts = sys.argv[2:]

all_lines = []
for (this_dir, subs_here, files_here) in os.walk(dirname):
    for filename in files_here:
        for ext in exts:
            if filename.endswith(ext):
                fullname = os.path.join(this_dir, filename)
                lines = sum(1 for line in open(fullname))
                all_lines.append(lines)
                if trace:
                    print('...', lines, fullname)

print('Total: ', sum(all_lines))
