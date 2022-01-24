from masonite.tests import TestCase

from src.form_builder.fieldtypes import Text


class TestTextField(TestCase):
    def test_component_and_index_component(self):
        field = Text.make("my_field")
        assert field.component() == "text-fieldtype"
        assert field.index_component() == "text-index-fieldtype"
        assert field.fieldtype_config.html_type == "text"
