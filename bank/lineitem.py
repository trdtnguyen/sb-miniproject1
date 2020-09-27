"""
LineItem class represents an abstract line item log for transaction-like entity such as
BankAccount transactions, credit transaction, loan transaction
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'


class LineItem:
    def __init__(self, id, processing_date, effective_date, type, status, amount, description, pos):
        """ Constructor
        Args:
            self (obj): self obj
            processing_date (str): processing date from database
            type (str): type of line item. Depend on the subclass, type would be various.
            status (str): status of the line item. Depend on the subclass, type would be various.
            amount (float): amount value of line item
            description (str): description of the line item
            pos (str): location of the pos that the line item is occured
        Returns:
            None
        """
        self.id = id
        self.processing_date = processing_date
        self.effective_date = effective_date
        self.type = type
        self.status = status
        self.amount = amount
        self.description = description
        self.pos = pos

    def write(self):
        pass
