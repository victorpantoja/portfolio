from settings import LINKEDIN_API_KEY, LINKEDIN_API_SECRET, LINKEDIN_USER_TOKEN, LINKEDIN_USER_SECRET
from linkedin.linkedin import LinkedInDeveloperAuthentication, PERMISSIONS, LinkedInApplication

RETURN_URL = "http://victorpantoja.com"

authentication = LinkedInDeveloperAuthentication(LINKEDIN_API_KEY, LINKEDIN_API_SECRET, 
                                                          LINKEDIN_USER_TOKEN, LINKEDIN_USER_SECRET, 
                                                          RETURN_URL, PERMISSIONS.enums.values())

application = LinkedInApplication(authentication)


def get_application():
    return application
