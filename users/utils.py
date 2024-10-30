from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone
import base64
from datetime import datetime

class ResetPasswordToken(PasswordResetTokenGenerator):
    def make_token(self, user):
        token = super().make_token(user)
        expiration_time = timezone.now() + timezone.timedelta(hours=1)
        expiration_timestamp = int(expiration_time.timestamp())
        print(f"make_token says: Token has been made: {token}, Expiration Timestamp: {expiration_timestamp}")
        return f"{token}-{base64.urlsafe_b64encode(str(expiration_timestamp).encode()).decode()}"

    def check_token(self, user, token):
        print("####################check_method########################")# test line
        try:
            base_token, expiration_b64 = token.rsplit("-", 1)
            expiration_timestamp = int(base64.urlsafe_b64decode(expiration_b64).decode())
            print(f"check_token Says: Decoded base token: {base_token}, Expiration Timestamp: {expiration_timestamp}")# test line
        except (ValueError, TypeError):
            print("Error decoding token.")# test line
            return False

        is_valid_token = super().check_token(user, base_token)
        is_valid_timestamp = self._check_token_validity(expiration_timestamp)

        print(f"Is valid token: {is_valid_token}, Is valid timestamp: {is_valid_timestamp}")  # test line

        return is_valid_token and is_valid_timestamp

    def _check_token_validity(self, timestamp):
        """Check if the token is still valid based on expiration timestamp."""
        valid_until = timezone.make_aware(datetime.fromtimestamp(timestamp))
        return timezone.now() < valid_until
