#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import ok, fail, checkParam, query2Dict

async def ls (request):
    #return ok('love')
    print(request)
    return request

async def post (request):
    print(request)
    return request

async def get (request):
    #return ok('love')
    return request