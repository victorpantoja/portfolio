# coding: utf-8
from tornado.web import URLSpec

from portfolio.handlers.page import PageHandler

urls = (
    URLSpec(r'/', PageHandler, name='home'),
    URLSpec(r'/(?P<context>.[\w-]+)', PageHandler, name='about'),
    URLSpec(r'/publications', PageHandler, name='publications'),
    URLSpec(r'/work', PageHandler, name='work'),
)
