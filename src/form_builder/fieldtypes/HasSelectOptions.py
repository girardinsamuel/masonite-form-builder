from typing import Iterable, List, Union, Type
from typing_extensions import Self
from masonite.utils.collections import collect, Collection


class HasSelectOptions:

    fieldtype_config = {"multiple": False}
    _options = {}

    # Public API
    def multiple(self) -> Self:
        self.fieldtype_config.multiple = True
        return self

    def options(self, raw_options: Iterable) -> Self:
        if isinstance(raw_options, (list, tuple)):
            for key_value in raw_options:
                self._options.append({"value": key_value, "label": key_value})
        else:
            for key, value in raw_options.items():
                self._options.append({"value": value, "label": key})
        return self

    # Private API
    def is_multiple(self) -> bool:
        return self.fieldtype_config.multiple

    def pre_process_index(self) -> Collection:
        value = super().pre_process_index()
        values = self.pre_process(value)

        if not isinstance(values, (tuple, list)):
            values = [values]
        values = collect(values)
        return values.map(lambda val: self.get_label(val)).all()

    def pre_process(self) -> Union[List, Collection, Type]:
        value = super().pre_process()
        multiple = self.is_multiple()
        if not value and multiple:
            return []

        if not isinstance(value, (tuple, list)):
            value = [value]

        values = collect(value)
        return values.all() if multiple else values.first()

    def process(self) -> Union[Collection, Type]:
        value = super().process()
        if not isinstance(value, (tuple, list)):
            value = [value]
        values = collect(value)
        return values.all() if self.is_multiple() else values.first()

    def get_label(self, value):
        self._options
