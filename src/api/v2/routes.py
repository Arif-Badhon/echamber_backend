from fastapi import APIRouter
from schemas import notice
from .endpoints2 import pharmaceuticals, pharmacy, pharmacy_purchase_order, pharmacy_grn, pharmacy_stock, clinic, clinic_details, pharmacy_invoice

api_router = APIRouter()

api_router.include_router(pharmaceuticals.router, prefix='/pharmaceuticals', tags=['Pharmaceuticals'])
api_router.include_router(pharmacy.router, prefix='/pharmacy', tags=['Pharmacy'])
api_router.include_router(pharmacy_purchase_order.router, prefix='/pharmacy/purchase-order', tags=['Pharmacy Purchase Order'])
api_router.include_router(pharmacy_grn.router, prefix='/pharmacy/grn', tags=['Pharmacy GRN'])
api_router.include_router(pharmacy_stock.router, prefix='/pharmacy/stock', tags = ['PharmacyStock'])
api_router.include_router(pharmacy_invoice.router, prefix='/pharmacy-invoice', tags=['Pharmacy Invoice'])
api_router.include_router(clinic.router, prefix='/clinic', tags=['Clinic'])
api_router.include_router(clinic_details.router, prefix='/clinic-details', tags=['Clinic Details, Nav, Offers'])