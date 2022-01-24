from masonite.tests import TestCase

from src.form_builder.Field import Field


class TestBaseField(TestCase):
    def test_field_creation(self):
        field = Field.make("my_field")
        assert field._handle == "my_field"

    def test_placeholder(self):
        field = Field.make("my_field").placeholder("Enter a value")
        assert field.config.placeholder == "Enter a value"
        field = field.placeholder()
        assert field.config.placeholder == ""

    def test_label(self):
        field = Field.make("my_field").label("First name")
        assert field.config.label == "First name"
        field = field.label()
        assert field.config.label == ""
