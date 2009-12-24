# -*- coding: utf-8 -*-
# -*- Mode: Python; py-indent-offset: 4 -*-
# * Author: Nikolay Kim <fafhrd91@gmail.com>

import logging, sys
from dumper import dump_threads

class DeadlockDumper(object):

    def __call__(self):
        dump = dump_threads()

        response = self.request.response
        response.setHeader('Expires', 'Sat, 1 Jan 2000 00:00:00 GMT')
        response.setHeader('Content-type', 'text/html; charset=utf-8')

        log = logging.getLogger('zojax.deadlock')
        log.log(logging.DEBUG, dump)

        dump = dump.replace('\n', '<br />')
        return '<html><body>%s</body></html>'%dump
