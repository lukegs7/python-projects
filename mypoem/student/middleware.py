#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 8:55 下午
# @Author  : lukegs7
# @File    : middleware.py.py
# @Software: PyCharm

import time
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class TimeItMiddleware(MiddlewareMixin):

    def process_request(self, request):
        self.start_time = time.time()
        return

    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('index'):
            return None
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view: {:.2f}s'.format(costed))
        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response

    def process_response(self, request, response):
        costed = time.time() - self.start_time
        print('request to response cost {:.2f}s'.format(costed))
        return response
