logmonitor
==========

A very simple log monitor without dependencies. (alpha)

Usage
-----

$ python logmonitor.py logmonitor.config

Example logmonitor.config:

* name=MyExample_Task_EmptyFileTask
* path=/var/home/your_app/your_example.log
* maxsize=1024
* task=EmptyFileTask
