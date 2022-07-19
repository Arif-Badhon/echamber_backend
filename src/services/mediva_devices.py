from services import BaseService
from repositories import mediva_device_repo
from models import MedivaDevice
from schemas import MedivaDeviceIn, MedivaDeviceUpdate

mediva_device_service = BaseService[MedivaDevice, MedivaDeviceIn, MedivaDeviceUpdate](MedivaDevice, mediva_device_repo)
