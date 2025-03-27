from kivy.app import App
from kivy.app import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """A simple app that has a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Eve", "Bob"]

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels of names."""
        for name in self.names:
            label = Label(
                text=name,
                font_size="20sp",
                bold=True,
            )
            self.root.ids.names_box.add_widget(label)


DynamicLabels().run()
