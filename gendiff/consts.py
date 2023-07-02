from collections import namedtuple

STATUS = namedtuple('PROPERTY_STATUS', ["DELETED", "PRISTINE", "ADDED", "CHANGED"])
PROPERTY_STATUS = STATUS(DELETED="deleted", PRISTINE="pristine", ADDED="added", CHANGED="changed")
