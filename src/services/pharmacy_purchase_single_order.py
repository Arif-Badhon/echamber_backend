from services import BaseService
from models import PharmacyPurchaseSingleOrder
from schemas import PharmacyPurchaseSingleOrderIn, PharmacyPurchaseSingleOrderUpdate
from repositories import pharmacy_purchase_single_order_repo

pharmacy_purchase_single_order_service = BaseService[PharmacyPurchaseSingleOrder, PharmacyPurchaseSingleOrderIn, PharmacyPurchaseSingleOrderUpdate](PharmacyPurchaseSingleOrder, pharmacy_purchase_single_order_repo)
