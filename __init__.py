from mycroft import MycroftSkill, intent_file_handler


class Linguamystica(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('linguamystica.intent')
    def handle_linguamystica(self, message):
        self.speak_dialog('linguamystica')


def create_skill():
    return Linguamystica()

