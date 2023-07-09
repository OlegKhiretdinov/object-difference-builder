from collections import namedtuple

STATUS = namedtuple('PROPERTY_STATUS',
                    ["DELETED", "PRISTINE", "ADDED", "CHANGED"])
PROPERTY_STATUS = STATUS(
    DELETED="deleted",
    PRISTINE="pristine",
    ADDED="added",
    CHANGED="changed"
)

PREFIX = namedtuple("PREFIX", ["ADD", "DELETE", "PRISTINE"])
JSON_DIFF_PREFIX = PREFIX(ADD="+ ", DELETE="- ", PRISTINE="  ")

INDENT = "  "
