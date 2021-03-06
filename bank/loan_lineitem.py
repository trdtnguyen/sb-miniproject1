"""
LoanLineItem class represents loan transaction entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError

from bank.lineitem import LineItem


class LoanLineItem(LineItem):
    """ Default Constructor

    """

    def __init__(self):
        self.id = 0
        self.processing_date = ''
        self.effective_date = ''
        self.type = ''
        self.status = ''
        self.amount = 0.0
        self.description = ''
        self.pos = ''
        self.loan_id = 0

    def __init__(self, in_id, in_processing_date, in_effective_date,
                 in_type, in_status, in_amount, in_description, in_pos, in_loan_id):
        """ Constructor
        Args:
            self (obj): self obj
            in_processing_date (str): processing date from database
            in_type (str): type of transaction. It is either "deposit" or "withdraw".
            in_status (str): status of the transaction. It is either "Pending" or "Completed".
            in_amount (float): amount value of transaction
            in_description (str): description of the transaction
            in_pos (str): location of the pos that the transaction is occured
            in_loan_id (int): loan id
        Returns:
            None
        """
        LineItem.__init__(self, in_id, in_processing_date, in_effective_date,
                          in_type, in_status, in_amount, in_description, in_pos)
        self.loan_id = in_loan_id

    def insert_lineitem(self, db):
        """ Insert a new row to corresponding table in database. The row are fetched from current instance properties.
        Args:
            db (DB): DB instance
        Returns:
            None
        """
        table = db.get_table('loan_line_items')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            stmt = table.insert(). \
                values(
                loan_id=self.loan_id,
                lli_processing_date=self.processing_date,
                lli_effective_date=self.effective_date,
                lli_type=self.type,
                lli_status=self.status,
                lli_amount=self.amount,
                lli_description=self.description,
                lli_pos=self.pos
            )
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1
