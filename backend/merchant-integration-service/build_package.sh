#!/bin/bash
# Run the sdist command
python setup.py sdist --formats=gztar --dist-dir=../shared

# Remove the .egg-info directory
find . -name "*.egg-info" -type d -exec rm -r {} +