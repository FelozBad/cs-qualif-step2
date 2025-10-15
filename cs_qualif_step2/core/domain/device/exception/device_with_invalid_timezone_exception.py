from cs_qualif_step2.core.domain.exception.ConflictException import ConflictException


class DeviceWithInvalidTimeZoneException(ConflictException):
    def __init__(self, time_zone: str):
        self.mac_address = mac_address
        super().__init__(f"The timezone: {time_zone} does not exist.")