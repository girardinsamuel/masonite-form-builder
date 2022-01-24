from typing import Callable, Dict, Union, Type
from typing_extensions import Self
from dotted_dict import DottedDict
from masonite.utils.collections import collect
from inflection import titleize


class Field:

    config = {
        "label": "",
        "placeholder": "",
        "instructions": "",
        "initial": None,
        "validatable": True,
        "defaultable": True,
        "selectable": True,
        "sortable": False,
        "rules": [],
    }
    fieldtype_config = {
        "handle": "",
        "component": "",
        "index_component": "",
        "html_type": "text",
    }
    _handle: str = None
    _value = None
    _rules = []

    def __init__(self):
        self.config = DottedDict(self.config)
        self.fieldtype_config = DottedDict(self.fieldtype_config)

    def __init_subclass__(cls):
        cls.config = DottedDict({**Field.config, **cls.config})
        cls.fieldtype_config = DottedDict({**Field.fieldtype_config, **cls.fieldtype_config})

    def __str__(self):
        return f"{self.__class__.__name__} <{self.handle()}>"

    def __repr__(self):
        return f"{self.__class__.__name__} <{self.handle()}>"

    # Public Fluent API
    @classmethod
    def make(cls, handle) -> Self:
        return cls()._set_handle(handle)

    def label(self, label: str = "") -> Self:
        self.config.label = label
        return self

    def placeholder(self, placeholder: str = "") -> Self:
        self.config.placeholder = placeholder
        return self

    def instructions(self, instructions: str = "") -> Self:
        self.config.instructions = instructions
        return self

    def validatable(self) -> Self:
        self.config.validatable = True
        return self

    def defaultable(self) -> Self:
        self.config.defaultable = True
        return self

    def selectable(self) -> Self:
        self.config.selectable = True
        return self

    def sortable(self) -> Self:
        self.config.sortable = True
        return self

    def rules(self, *rules) -> Self:
        self._rules = rules
        return self

    def initial(self, initial: Union[Type, Callable]) -> Self:
        self.config.initial = initial
        return self

    def extra(self, data: Dict) -> Self:
        self.config.extra = data
        return self

    def handle(self) -> str:
        return self._handle

    # Private API
    def _set_handle(self, handle) -> Self:
        self._handle = handle
        return self

    def _set_config(self, config) -> Self:
        self.config = config
        return self

    def new(self) -> Self:
        return Field()._set_config(self.config)._set_handle(self._handle)

    def display(self):
        return ""

    def rules(self):
        return []

    def component(self):
        handle = self.fieldtype_config.component or self.fieldtype_config.handle
        return f"{handle.replace('-fieldtype', '')}-fieldtype"

    def index_component(self):
        handle = self.fieldtype_config.index_component or self.fieldtype_config.handle
        return f"{handle.replace('-fieldtype', '')}-index-fieldtype"

    def is_required(self):
        return collect(self.rules()).contains("required")

    def is_sortable(self):
        return self.config.sortable

    def is_filterable(self):
        return self.config.filterable

    def serialize(self):
        return {
            "handle": self.handle(),
            "label": self.config.label or titleize(self.handle()),
            "type": self.fieldtype_config.html_type,
            "display": self.display(),
            "required": self.required(),
        }

    def set_value(self, value) -> Self:
        self._value = value
        return self

    def value(self):
        return self._value

    def initial_value(self):
        if callable(self.config.initial):
            value = self.config.initial()
        else:
            value = self.config.initial
        return value

    def augment(self, value):
        return value

    def meta(self):
        return {}

    def process(self) -> Self:
        return self.new().set_value(self.value())

    def pre_process(self) -> Self:
        value = self.value() or self.initial_value()
        return self.new().set_value(value)

    def pre_process_index(self) -> Self:
        return self.new().set_value(self.value())
