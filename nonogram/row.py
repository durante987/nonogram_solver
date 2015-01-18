"""
Class incorporating the information that we know of a row.
"""

from .line import Line


class Row(Line):
    def __init__(self, *args):
        super(Row, self).__init__(*args)

    def __str__(self):
        return "row: " + super(Row, self).__str__()
