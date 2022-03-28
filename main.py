from kivy.app import App
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

# Defining our diffrent windows

class StartScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass

class FinalScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

# This is an replacment for an kivy file becuse i coulden't get it to work.
kv = Builder.load_string('''
Manager:
    StartScreen:
    LoginScreen:
    SignUpScreen:
    FinalScreen:

<StartScreen>:
    name: "start"
    BoxLayout:
        cols: 1

        BoxLayout:
            cols: 2
            orientation: 'vertical'

            Label:
                text: 'Hello welcome!'
            
            BoxLayout:
                cols: 2
                orientation: 'horizontal'

                Button:
                    text: 'Login'
                    on_press:
                        root.manager.transition.direction = 'right'
                        root.manager.transition.duration = 0.3
                        root.manager.current = 'login'
                Button:
                    text: 'SignUp'
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.3
                        root.manager.current = 'signup'

<LoginScreen>:
    name: "login"

    BoxLayout:
        orientation: 'vertical'
        cols: 1
        Label:
            text: "Login"
        
        BoxLayout:
            orientation: 'vertical'
            cols: 2

            BoxLayout:
                orientation: 'horizontal'
                cols: 2

                Button:
                    text: 'Continue'
                    on_press:
                        root.manager.transition.direction = 'down'
                        root.manager.transition.duration = 0.3
                        root.manager.current = 'final'

                Button:
                    text: 'Back'
                    on_press:
                        root.manager.transition.direction = 'left'
                        root.manager.transition.duration = 0.3
                        root.manager.current = 'start'

<SignUpScreen>:
    name: "signup"

    Label:
        text: "Hello"

<FinalScreen>:
    name: "final"
    Label:
        text: 'You got through!'
    Button:
        text: 'Log Out'
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.transition.duration = 0.3
            root.manager.current = 'start'
''')

# This is the app
class PuppyAlert(App):
    def build(self):
        return kv
    
PuppyAlert().run()
