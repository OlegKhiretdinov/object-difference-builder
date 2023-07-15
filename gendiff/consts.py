from collections import namedtuple

STATUS = namedtuple('PROPERTY_STATUS',
                    ["DELETED", "PRISTINE", "ADDED", "CHANGED"])
PROPERTY_STATUS = STATUS(
    DELETED="deleted",
    PRISTINE="pristine",
    ADDED="added",
    CHANGED="changed"
)

# PREFIX = namedtuple("PREFIX", ["ADD", "DELETE", "PRISTINE"])
# JSON_PREFIX = PREFIX(ADD="+ ", DELETE="- ", PRISTINE="  ")

# Stylish
JSON_PREFIX = {
    PROPERTY_STATUS.ADDED: "+ ",
    PROPERTY_STATUS.DELETED: "- ",
    PROPERTY_STATUS.PRISTINE: "  ",
}

INDENT = "  "

STATUS_VALUES_RELATION = {
    PROPERTY_STATUS.ADDED: "current",
    PROPERTY_STATUS.DELETED: "initial",
    PROPERTY_STATUS.PRISTINE: "initial",
}
