
class AuthenticationLogic:
    @staticmethod
    def check_credentials(entered_username, entered_password):
        return entered_username == "vt" and entered_password == "password"
