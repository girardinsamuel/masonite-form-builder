from typing_extensions import Self
from typing import List
from dotted_dict import DottedDict
from inflection import underscore, titleize

from .Fields import Fields
from .Field import Field


class Blueprint:

    _fields = []
    config = DottedDict(
        {
            "title": "",
        }
    )
    _handle: str = ""

    def make(self, handle: str = "") -> Self:
        if not handle:
            handle = underscore(self.__class__.__name__)
        self._handle = handle

        self.config.title = titleize(self.__class__.__name__)
        return self

    def title(self, title="") -> Self:
        self.config.title = title
        return self

    def add_fields(self, *fields: Field) -> Self:
        self._fields = fields
        return self

    def fields(self) -> Fields:
        # TODO: validate unique handles
        # TODO: run custom external check
        fields = Fields(self._fields)
        return fields

    def field(self, field: Field) -> Field:
        self.fields().get(field)

    def serialize(self):
        pass
