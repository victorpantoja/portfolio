# coding: utf-8
import portfolio
from portfolio import settings
from tornado.web import RequestHandler


class PageHandler(RequestHandler):
    selectors = ['headline', 'first-name', 'last-name', 'location', 'skills',
                 'languages', 'projects', 'summary']

    def get(self, **kwargs):
        profile = portfolio.get_application().get_profile(selectors=self.selectors)

        if kwargs.get('context'):
            self.render("%s.html" % kwargs['context'], SERVER_NAME=settings.SERVER_NAME,
                                                        profile=profile)
        else:
            self.render("index.html", SERVER_NAME=settings.SERVER_NAME)
