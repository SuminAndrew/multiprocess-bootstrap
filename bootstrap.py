#!/usr/bin/env python
# coding=utf-8

"""Usage:

./bootstrap.py --num=32 --cmd='/usr/bin/frontik --config=/etc/hh-xhh/frontik.cfg --app=xhh --port=15{num:0>2}'

"""

import argparse
import logging
import signal
import subprocess
import sys

_PROCESSES = []

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(message)s')


def start():
    parser = argparse.ArgumentParser(description='Simple supervisor for docker')
    parser.add_argument('--cmd', type=str, help='Command to be executed')
    parser.add_argument('--num', type=int, help='Processes count')
    args = parser.parse_args()

    signal.signal(signal.SIGTERM, sigterm_action)

    for i in range(args.num):
        start_process(i, args)

    for proc in _PROCESSES:
        proc.wait()


def sigterm_action(signum, stack):
    logging.debug('received SIGTERM')

    for i, proc in enumerate(_PROCESSES):
        logging.debug('sending SIGTERM to process #%s', i)
        proc.send_signal(signum)


def start_process(process_num, args):
    cmd_formatted = args.cmd.format(num=process_num)
    logging.debug('starting process #%s, executing "%s"', process_num, cmd_formatted)

    _PROCESSES.append(subprocess.Popen(cmd_formatted.split()))


if __name__ == '__main__':
    start()
