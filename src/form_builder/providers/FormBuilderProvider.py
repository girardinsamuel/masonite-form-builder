"""A FormBuilderProvider Service Provider."""

from masonite.packages import PackageProvider


class FormBuilderProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("form_builder")
            .name("form-builder")
            .config("config/form_builder.py", publish=True)
        )

    def boot(self):
        """Boots services required by the container."""
        pass
