import copy

from cs_qualif_step2.core.domain.device.device_repository import DeviceRepository
from cs_qualif_step2.core.domain.device.device import Device


class InMemoryDeviceRepository(DeviceRepository):
    def __init__(self):
        self.devices = {}

    def find_by_mac_address(self, mac_address: str):
        for device in self.devices.values():
            if device.get_mac_address() == mac_address:
                return copy.copy(device)
        return None

    def find_by_id(self, device_id: str):
        return copy.copy(self.devices.get(device_id))

    def save(self, device: Device):
        self.devices[str(device.get_device_id())] = device

    def find_by_timezone(self, timezone: str):
        pass
