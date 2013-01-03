#!/usr/bin/env python
# -*- coding: utf-8 -*-
# copyright (c) 2012 by Samuel de Ancos.
from os import path
from sys import stderr
from time import sleep
from imp import find_module, load_module
from argparse import ArgumentParser
from ConfigParser import SafeConfigParser

class MonitorLog(object):
    
    def __init__(self, name, opts):
        self.name = name
        self.path = opts['path']
        self.max_size = opts['maxsize']
        self.task = opts['task']
    
    def load_task(self):
        info = find_module(self.task, ['tasks'])
        module = load_module(self.task, *info)
        return module

    def run(self):
        self.size = path.getsize(self.path)
        max_size = int(self.max_size)
        if self.size >= max_size:
            task_class = self.load_task()
            instance = task_class.Task()
            instance.run(self.path, max_size, self.size)
 
def main(configurations):
    while 1:
        for name, opts in configurations:
            try:
                monitor = MonitorLog(name, opts)
                monitor.run()
            except Exception, err:
                stderr.write('ERROR: %s\n' % str(err))
        sleep(1)
    return 0

if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Log Monitor')
    arg_parser.add_argument('-c', '--config', type=str, help='Config file.')

    args = arg_parser.parse_args()
    config_candidates = ['logmonitor.config']
    
    if args.config:
        config_candidates.append(args.config)

    config_parser = SafeConfigParser()
    parse_files = config_parser.read(config_candidates)

    if parse_files:
        main(config_parser._sections.iteritems())
    else:
        stderr.write('Config File not found: ' + str(args.config))
