from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build a BoxLayout Demo App."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user when they press the 'Greet' button."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Reset both the text input field and the output label to blank when user press 'Clear' button."""
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""



BoxLayoutDemo().run()
