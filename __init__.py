from mycroft import MycroftSkill, intent_file_handler


class TeamDeathmatch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('deathmatch.team.intent')
    def handle_deathmatch_team(self, message):
        self.speak_dialog('deathmatch.team')


def create_skill():
    return TeamDeathmatch()

