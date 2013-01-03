# -*- coding: utf-8 -*-
# copyright (c) 2012 by Samuel de Ancos.
from tasks.TaskBase import TaskBase

class Task(TaskBase):
    def run(self, path, max_size, size):
        open(path, "w").close()