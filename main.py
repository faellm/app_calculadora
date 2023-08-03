from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.expression = ""
        layout = BoxLayout(orientation='vertical')

        self.result = Button(text="0", font_size=40, size_hint_y=None, height=100)
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, font_size=40, on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        label = instance.text
        if label == '=':
            try:
                self.result.text = str(eval(self.expression))
            except Exception as e:
                self.result.text = "Error"
        elif label == 'C':
            self.expression = ""
            self.result.text = "0"
        else:
            self.expression += label
            self.result.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
