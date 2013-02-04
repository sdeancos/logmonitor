logmonitor
==========

A very simple log monitor without dependencies in python. (alpha)

Usage
-----

$ python logmonitor.py logmonitor.config

Example logmonitor.config:

* name=MyExample_Task_EmptyFileTask
* path=/var/log/your_app/your_example.log
* maxsize=1024
* task=EmptyFileTask
