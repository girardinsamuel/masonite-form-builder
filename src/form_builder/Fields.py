from typing_extensions import Self
from masonite.utils.collections import Collection, collect
from masonite.validation import Validator
from .Field import Field


class Fields:

    _items: Collection = []
    _fields: Collection = []

    def __init__(self, items=[]) -> None:
        self.set_items(items)

    def set_items(self, items) -> Self:
        if isinstance(items, Collection):
            items = items.all()
        self._items = collect(items)
        # TODO
        self._fields = self.resolve_fields()
        return self

    def set_fields(self, fields) -> Self:
        self._fields = fields
        return self

    def resolve_fields(self):
        # TODO: if need to convert array of items into Field() do it here
        # but for now it assumed that we will provided directly Field objects !
        return self._items

    def items(self):
        return self._items

    def all(self) -> Collection:
        return self._fields

    def all_except(self, *keys) -> Self:
        filtered_fields = self._fields.filter(lambda field: field.handle() not in keys)
        return Fields().set_fields(filtered_fields)

    def only(self, *keys) -> Self:
        filtered_fields = self._fields.filter(lambda field: field.handle() in keys)
        return Fields().set_fields(filtered_fields)

    def new(self) -> Self:
        return Fields().set_items(self._items).set_fields(self._fields)

    def has(self, field) -> bool:
        return self._fields.has(field)

    def get(self, field) -> Field:
        return self._fields.get(field)

    def serialize(self):
        # TODO map each of them to serialize
        return self._fields.values()

    def add_values(self, values) -> Self:
        fields = self._fields.map(lambda field: field.new().set_value(values.get(field.handle())))
        return self.new().set_fields(fields)

    def values(self) -> Collection:
        return self._fields.map(lambda field: {field.handle(): field.value()})

    def process(self) -> Self:
        return self.new().set_fields(self._fields.map(lambda field: field.process()))

    def pre_process(self) -> Self:
        return self.new().set_fields(self._fields.map(lambda field: field.pre_process()))

    def augment(self) -> Self:
        return self.new().set_fields(self._fields.map(lambda field: field.augment()))

    def meta(self) -> Collection:
        return self._fields.map(lambda field: field.meta()).all()

    # validation stuff section
    def validator(self) -> Validator:
        validator = Validator()
        return validator

    def validate(self):
        return self.validator().validate(self._fields.values().all(), self.rules())

    def rules(self) -> Collection:
        return (
            self.field_rules()
            .map(lambda rules: collect(rules).map(lambda rule: self.parse(rule)).all())
            .all()
        )

    def field_rules(self) -> Collection:
        if not self._fields:
            return collect()
        return self._fields.all().reduce(lambda arr, field: arr + field.rules(), collect())

    def parse(self, rule):
        if not isinstance(rule, str) or "{" not in rule:
            return rule
        # TODO: use regex to convert string rule in somehting
        pass
