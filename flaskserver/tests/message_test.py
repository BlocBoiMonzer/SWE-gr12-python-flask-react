class SendMessageCommand:
    def execute(self):
        pass


class Test_when_sending_messages :
    def test_messages_are_stored_in_database (self):
        command = SendMessageCommand()
        command.user = "Luke Skywalker"
        command.message = "This is Red Leader. We're approaching the Ison Corridor!"
        command.execute()

        assert "Inconclusive - how do we check?" == False