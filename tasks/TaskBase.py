# -*- coding: utf-8 -*-
# copyright (c) 2012 by Samuel de Ancos.
from abc import ABCMeta, abstractmethod
 
class TaskBase:
    __metaclass__ = ABCMeta
 
    @abstractmethod
    def run(self, path, max_size, size):pass