from django.utils.html import strip_spaces_between_tags

class CleanWhiteSpaceMiddleware(object):
    def process_response(self, request, response):
        if 'text/html' in response['Content-Type']:
            response.content = strip_spaces_between_tags(response.content)
        return response
