from .characteristic import Real
from .concept import AbstractElement


class BaseRecord(AbstractElement, Real):
    """Base class for records."""


class MutableRecord(BaseRecord):
    """Mutable record class."""


class ImmutableRecord(BaseRecord):
    """Immutable record class."""


__all__ = [
    "BaseRecord",
    "MutableRecord",
    "ImmutableRecord",
]
