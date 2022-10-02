from repositories import BaseRepo
from models import PharmacyInvoice
from schemas import PharmacyInvoiceIn, PharmacyInvoiceUpdate

pharmacy_invoice_repo = BaseRepo[PharmacyInvoice, PharmacyInvoiceIn, PharmacyInvoiceUpdate](PharmacyInvoice)