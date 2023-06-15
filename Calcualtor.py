from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
class CalculatorApp(App):
    def build(self):
        self.userInput = True
        self.lbOperation = Label(text='')
        btn_1 = Button(text='1',on_press=lambda b: self.operation('1'),pos_hint={'center_y':0.5})
        btn_2 = Button(text='2',on_press=lambda b: self.operation('2'),pos_hint={'center_y':0.5})
        btn_3 = Button(text='3',on_press=lambda b: self.operation('3'),pos_hint={'center_y':0.5})
        btn_4 = Button(text='4',on_press=lambda b: self.operation('4'),pos_hint={'center_y':0.5})
        btn_5 = Button(text='5',on_press=lambda b: self.operation('5'),pos_hint={'center_y':0.5})
        btn_6 = Button(text='6',on_press=lambda b: self.operation('6'),pos_hint={'center_y':0.5})
        btn_7 = Button(text='7',on_press=lambda b: self.operation('7'),pos_hint={'center_y':0.5})
        btn_8 = Button(text='8',on_press=lambda b: self.operation('8'),pos_hint={'center_y':0.5})
        btn_9 = Button(text='9',on_press=lambda b: self.operation('9'),pos_hint={'center_y':0.5})
        btn_0 = Button(text='0',on_press=lambda b: self.operation('0'),pos_hint={'center_y':0.5})
        btn_plus = Button(text='+',on_press=lambda b: self.operation('+'),pos_hint={'center_y':0.5})
        btn_minus = Button(text='-',on_press=lambda b: self.operation('-'),pos_hint={'center_y':0.5})
        btn_multiplication = Button(text='*',on_press=lambda b: self.operation('*'),pos_hint={'center_y':0.5})
        btn_division = Button(text='/',on_press=lambda b: self.operation('/'),pos_hint={'center_y':0.5,'center_x':0.5},size_hint=(0.325,None))
        btn_done = Button(text='=',on_press=lambda b: self.operation('='))
        btn_backspace = Button(text='<----',on_press=lambda b: self.operation('<----'))
        vl = BoxLayout(orientation='vertical',spacing=8)
        hl1 = BoxLayout(padding=4,spacing=8)
        hl2 = BoxLayout(padding=4,spacing=8)
        hl3 = BoxLayout(padding=4,spacing=8)
        hl4 = BoxLayout(padding=4,spacing=8)
        vl.add_widget(self.lbOperation)
        hl1.add_widget(btn_plus)
        hl1.add_widget(btn_1)
        hl1.add_widget(btn_2)
        hl1.add_widget(btn_3)
        hl2.add_widget(btn_minus)
        hl2.add_widget(btn_4)
        hl2.add_widget(btn_5)
        hl2.add_widget(btn_6)
        hl3.add_widget(btn_multiplication)
        hl3.add_widget(btn_7)
        hl3.add_widget(btn_8)
        hl3.add_widget(btn_9)
        hl4.add_widget(btn_division)
        hl4.add_widget(btn_0)
        vl.add_widget(hl1)
        vl.add_widget(hl2)
        vl.add_widget(hl3)
        vl.add_widget(hl4)
        vl.add_widget(btn_done)
        vl.add_widget(btn_backspace)
        return vl
    def operation(self,text):
        if text != '=' and text != '<----':
            if self.userInput:
                self.lbOperation.text = self.lbOperation.text + text
            else:
                self.lbOperation.text = text
            self.userInput = True
        elif text == '<----':
            if self.userInput:
                if len(self.lbOperation.text) > 0:
                    self.lbOperation.text = self.lbOperation.text[:-1]
            else:
                self.lbOperation.text = ''
        else:
            if len([i for i in self.lbOperation.text if not(i in ['+','-','*','/'])]) < len(self.lbOperation.text):
                try:
                    self.lbOperation.text = str(eval(self.lbOperation.text))
                except:
                    print('Еrror')
                    self.lbOperation.text = 'Error'
                self.userInput = False
CalculatorApp().run()