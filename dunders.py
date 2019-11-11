# __dict__,
""" amapping of all the attributes in an object to their value."""


class AsDictionaryMixin:
    def to_dict(self):
        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop)
        }

    def _represent(self, value):
        if isinstance(value, object):
            if hasattr(value, "to_dict"):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith("_")


# __mro__
"""The MRO shows the order in which Python is going to look for a matching attribute or method."""
Instance.__mro__

# __str__
"""provide a pretty representation"""


def __str__(self):
    lines = [self.street]
    if self.street2:
        lines.append(self.street2)
    lines.append(f"{self.city}, {self.state} {self.zipcode}")
    return "\n".join(lines)
