# -*- coding: utf-8 -*-

"""Console script for ebr_board."""
import sys
import argparse


def parse_args(args):
    """Returns parsed commandline arguments.
    """

    parser = argparse.ArgumentParser(description="Commandline interface for ebr_board")
    parser.add_argument("--foo")
    return parser.parse_args(args)


def main():
    """Console script for ebr_board."""
    parse_args(sys.argv[1:])
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
