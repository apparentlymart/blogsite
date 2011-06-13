
# Create symlinks in the current directory (which
# the repository must be a subdirectory of) to
# make the tree that can be used to push to
# dotcloud without dotcloud trying to use git to push.

import os


source_dir = os.path.dirname(__file__)
needed_files = (
    "bee",
    "blogsite",
    "serviceconfig",
    "web",
    "worker",
    "dotcloud_build.yml",
)

for fn in needed_files:
    source = "%s/%s" % (source_dir, fn)
    target = fn
    print "%s -> %s" % (source, target)
    os.symlink(source, target)

