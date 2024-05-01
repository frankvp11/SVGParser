from nicegui import ui
import random

class RandomValue:
    def __init__(self, value):
        print(value)

def handle_change(e):
    if e.value == 'Mails':
        with mail_panel:
                RandomValue(random.randint(0, 100))
                ui.label('Mails').classes('text-h4')
                ui.label('Content of mails')
    elif e.value == 'Alarms':
      with alarm_panel:
                RandomValue(random.randint(0, 100))
                ui.label('Alarms').classes('text-h4')
                ui.label('Content of alarms')
    elif e.value == 'Movies':
      with movie_panel:
                RandomValue(random.randint(0, 100))
                ui.label('Movies').classes('text-h4')
                ui.label('Content of movies')



with ui.splitter(value=30).classes('w-full h-56') as splitter:
    with splitter.before:
        with ui.tabs().props('vertical').classes('w-full') as tabs:
            mail = ui.tab('Mails', icon='mail')
            alarm = ui.tab('Alarms', icon='alarm')
            movie = ui.tab('Movies', icon='movie')
    with splitter.after:
        with ui.tab_panels(tabs, value=mail, on_change=handle_change) \
                .props('vertical').classes('w-full h-full'):
            with ui.tab_panel(mail) as mail_panel:
                 print("Hello")
            with ui.tab_panel(alarm) as alarm_panel:
                 print("Hello")

            with ui.tab_panel(movie) as movie_panel:
                  print("Hello")
ui.run()