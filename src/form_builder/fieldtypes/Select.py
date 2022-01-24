from src.form_builder.fieldtypes.HasSelectOptions import HasSelectOptions
from ..Field import Field


class Select(Field, HasSelectOptions):

    fieldtype_config = {
        "handle": "select",
        "index_component": "tags",
    }
