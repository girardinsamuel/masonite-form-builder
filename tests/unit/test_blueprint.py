from masonite.tests import TestCase

from src.form_builder.Blueprint import Blueprint
from src.form_builder.fieldtypes import Text


class MyCustomForm(Blueprint):
    pass


class TestBlueprint(TestCase):
    def test_blueprint_creation(self):
        blueprint = Blueprint().make("my_form").title("My First Form")
        assert blueprint._handle == "my_form"
        assert blueprint.config.title == "My First Form"

    def test_custom_blueprint_creation(self):
        blueprint = MyCustomForm().make()
        assert blueprint._handle == "my_custom_form"
        assert blueprint.config.title == "My Custom Form"

    def test_building_blueprint(self):
        blueprint = (
            Blueprint()
            .make("my_form")
            .title("My First Form")
            .add_fields(Text.make("first_name"), Text.make("last_name"), Text.make("email"))
        )
        # GET
        # fields = blueprint.fields().pre_process()
        # values = fields.values().all()
        # meta = fields.meta()

        # POST
        fields = (
            blueprint.fields()
            .all_except("email")
            .add_values({"first_name": "Sam", "last_name": "Gamji"})
        )
        values = fields.process().values()
        import pdb

        pdb.set_trace()
