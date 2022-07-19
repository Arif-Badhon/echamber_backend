from repositories import BaseRepo
from schemas import MedivaDeviceIn, MedivaDeviceUpdate
from models import MedivaDevice


mediva_device_repo = BaseRepo[MedivaDevice, MedivaDeviceIn, MedivaDeviceUpdate](MedivaDevice)
