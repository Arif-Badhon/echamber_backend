from services import BaseService
from models import PharmacyInvoice
from schemas import PharmacyInvoiceIn, PharmacyInvoiceUpdate
from repositories import pharmacy_invoice_repo


pharmacy_invoice_service = BaseService[PharmacyInvoice, PharmacyInvoiceIn, PharmacyInvoiceUpdate](PharmacyInvoice, pharmacy_invoice_repo)