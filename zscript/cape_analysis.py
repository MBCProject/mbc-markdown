"""
Analyze CAPEv2 community signature modules, extract information, and produce
CSV content.
"""
import argparse
import csv
import importlib
import inspect
import logging
import logging.config
import pathlib
import stix2
import stix2.utils
import sys

# From CAPEv2, or the stubs
import lib.cuckoo.common.abstracts

# From CAPEv2 community repo; successfully importing this module probably
# requires adding the appropriate path to $PYTHONPATH.
#
# See: https://github.com/kevoreilly/community
import modules.signatures


def parse_args():
    """
    Parse commandline arguments.
    """
    arg_parser = argparse.ArgumentParser(
        description="Analyze CAPEv2 community signatures and create CSV"
                    " content."
    )

    
    arg_parser.add_argument(
        "-o", "--out", required=True,
        help="""
        Directory path to the CAPE community repo.
        """
    )

    arg_parser.add_argument(
        "-o", "--out", required=True
        help="""
        A filename to write content to.  If not given, write to stdout.
        """
    )

    return arg_parser.parse_args()


def main():
    

if __name__ == "__main__":
    main()
