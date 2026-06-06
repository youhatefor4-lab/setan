from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextImput
from kivy.uix.button import Button

data = []

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(). __init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.nama_input = TextImput(hint_text="Nama Pengeluaran", multiline=False)
        self.jumlah_input = TextImput(hint_text="Jumlah", multiline=False)
        self.add_button = Button(text= "Tambah", size_hint_y=None, height=50)
        self.add_button.bind(on_PressPush ke GitHubg)