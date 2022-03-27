import subprocess

from google.oauth2.credentials import UserAccessTokenCredentials


def main():
    subprocess.check_call(["expressvpn", "connect", "gr"], stderr=subprocess.STDOUT)
    try:
        import google.cloud.logging
        import google.auth.credentials

        client = google.cloud.logging.Client(credentials=UserAccessTokenCredentials(
        ))
        logger: google.cloud.logging.Logger = client.logger(name="test_logging")
        logger.log("Zhaba bumba")
    finally:
        subprocess.check_call(["expressvpn", "disconnect"], stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main()


# git config --global user.email "jonatan.repka@my.com"
# git config --global user.name "Jonatan Repka"
