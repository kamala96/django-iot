from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Controller


class MicroControllerAuthentication(BaseAuthentication):
    def authenticate(self, request):
        controller_chip_id = request.META.get('HTTP_X_CHIP_ID')
        network_address = request.META.get('HTTP_X_NETWORK_IP')

        if not controller_chip_id or not network_address:
            return None

        try:
            controller = Controller.objects.get(
                chip_id=controller_chip_id, network_address=network_address)
        except Controller.DoesNotExist:
            raise AuthenticationFailed('Invalid access key.')

        return (controller, None)
