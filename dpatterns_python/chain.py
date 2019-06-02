"""
chain pattern in python
"""


class Handler:  # Abstract handler
    """Abstract Handler"""

    def __init__(self, successor):
        self._successor = successor  # Define who is the next handler

    def handle(self, request):
        """
        handle
        :param request:
        :return:
        """
        handled = self._handle(request)  # If handled, stop here

        # Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError("Must provide implementation in subclass!")


class ConcreteHandler1(Handler):  # Inherits from the abstract handler
    """Concrete handler 1"""

    def _handle(self, request):
        """
        Provide a condition for handling
        :param request:
        :return:
        """
        if 0 < request <= 10:
            print("Request {} handled in handler 1".format(request))
            return True  # Indicates that the request has been handled
        return False


class DefaultHandler(Handler):  # Inherits from the abstract handler
    """Default handler"""

    def _handle(self, request):
        """If there is no handler available"""
        # No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True  # Indicates that the request has been handled


class Client:
    """
    Using handlers
    """

    def __init__(self):
        """
        Create handlers and use them in a sequence you want
        Note that the default handler has no successor
        """
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests_list):
        """
        Send your requests one at a time for handlers to handle
        :param requests_list:
        :return:
        """
        for request in requests_list:
            self.handler.handle(request)


# Create a client
CLIENT = Client()

# Create requests
REQUEST = [2, 5, 30]

# Send the requests
CLIENT.delegate(REQUEST)
