import datetime
import yaml

class User:

    def __init__(self):
        """
        Initialize the user object.
        """
        try:
            file = open('./config.yaml', 'r')
            self.config = yaml.safe_load(file)

        except FileNotFoundError:
            with open('./config.yaml', 'w') as file:
                self.config = self._one_time_user_setup()
                yaml.dump(self.config, file, default_flow_style=False)

        finally:
            file.close()


    def _one_time_user_setup(self) -> dict:
        """
        Perform setup if this is the first time starting the application
        """
        username = input('Enter a username: ')
        email = input('Enter an email: ')
        created_timestamp = str(datetime.datetime.today())

        return dict(username = username, email = email, created_timestamp = created_timestamp)


    def __str__(self):
        print(self.username)
