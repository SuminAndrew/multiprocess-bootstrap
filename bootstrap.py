#!/usr/bin/env python
# coding=utf-8

"""Usage:

/usr/bin/bootstrap --num=32 --cmd='/usr/bin/frontik --config=/etc/hh-xhh/frontik.cfg --app=xhh --port=15{num:0>2}'

"""

import argparse
import logging
import signal
import subprocess
import sys
import time

_PROCESSES = []


def start():
    parser = argparse.ArgumentParser(description='Simple supervisor for docker')
    parser.add_argument('--cmd', type=str, help='Command to be executed')
    parser.add_argument('--num', type=int, help='Processes count')
    parser.add_argument('--log', type=str, help='Logfile path (uses stderr if empty)')
    args = parser.parse_args()

    if args.log is None:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(asctime)s %(message)s')
    else:
        logging.basicConfig(filename=args.log, level=logging.DEBUG, format='%(asctime)s %(message)s')

    signal.signal(signal.SIGTERM, sigterm_action)

    for i in range(args.num):
        start_process(i, args)

    while True:
        for i, proc in enumerate(_PROCESSES):
            return_code = proc.poll()
            if return_code is not None:
                logging.info('child #%s was shut down, exit code: %s', i, return_code)

                cmd_formatted = args.cmd.format(num=i)
                logging.info('restarting process #%s, executing "%s"', i, cmd_formatted)

                _PROCESSES[i] = subprocess.Popen(cmd_formatted.split())

            time.sleep(1)

        if not _PROCESSES:
            logging.info('all children terminated, exiting')
            sys.exit(0)


def sigterm_action(signum, stack):
    logging.info('received SIGTERM')

    term_processes = _PROCESSES[:]
    _PROCESSES[:] = []

    for i, proc in enumerate(term_processes):
        logging.info('sending SIGTERM to process #%s', i)
        proc.send_signal(signum)


def start_process(process_num, args):
    cmd_formatted = args.cmd.format(num=process_num)
    logging.info('starting process #%s, executing "%s"', process_num, cmd_formatted)

    _PROCESSES.append(subprocess.Popen(cmd_formatted.split()))


if __name__ == '__main__':
    start()
