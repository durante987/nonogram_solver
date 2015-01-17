"""
Class incorporating the information that we know of a row.
"""

import line

class Row(line.Line):

    def __init__(self, *args):
        super(Row, self).__init__(*args)
        self.is_row = True

    def __str__(self):
        str_ = "row: {!s}, ".format(self.is_row)

        return str_ + super(Row, self).__str__()
