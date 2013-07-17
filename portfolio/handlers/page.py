# coding: utf-8
from tornado.web import RequestHandler
import settings


class PageHandler(RequestHandler):

    def get(self, **kwargs):
        
        if kwargs.get('context'):
            self.render("%s.html" % kwargs['context'], SERVER_NAME=settings.SERVER_NAME)
        else:
            self.render("index.html", SERVER_NAME=settings.SERVER_NAME)
