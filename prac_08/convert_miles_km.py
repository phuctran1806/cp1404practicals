from kivy.app import App
from kivy.app import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILES_TO_KM_RATIO = 1.60934

class MilesToKmConverter(App):
    """An app that converts miles to km."""
    km_message = StringProperty()
    miles_message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        Window.size = (700, 400)
        return self.root

    def convert_miles_to_km(self, input_miles):
        """Converts miles to km when user hit the convert button."""
        try:
            km_value = float(input_miles) * MILES_TO_KM_RATIO
        except ValueError:
            self.km_message = "0.0"
        else:
            integer_part, decimal_part = str(km_value).split(".")
            self.km_message = f"{integer_part}.{decimal_part[:3]}"  # Only display with 3 decimals

    def handle_increment(self, input_miles, value):
        """Increase or decrease the miles number by 1."""
        try:
            new_miles = float(input_miles) + value
        except ValueError:
            self.miles_message = f"{value}.0"
        else:
            self.miles_message = f"{new_miles}"


MilesToKmConverter().run()
