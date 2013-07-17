# coding: utf-8
from tornado.web import URLSpec

from portfolio.handlers.page import PageHandler

urls = (
    URLSpec(r'/(?P<page>index.html)?', PageHandler, name='home'),
    URLSpec(r'/(?P<context>.[\w-]+)(?P<page>/index.html)?', PageHandler, name='context'),
)
