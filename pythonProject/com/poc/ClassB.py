from com.poc import Constants
from com.poc.ClassA import JSONAdvisories as NotusJsonAdvisories


class JSONAdvisories(NotusJsonAdvisories):

    def __init__(self):
        self.constant = Constants.family1

    def print_constant(self):
        super().print_constant()


