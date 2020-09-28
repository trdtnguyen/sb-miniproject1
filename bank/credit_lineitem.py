"""
LoanLineItem class represents loan transaction entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError

from bank.lineitem import LineItem


class CreditLineItem(LineItem):
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
        self.credit_id = 0

    def __init__(self, in_id, in_processing_date, in_effective_date,
                 in_type, in_status, in_amount, in_description, in_pos, in_credit_id):
        """ Constructor
        Args:
            self (obj): self obj
            in_processing_date (str): processing date from database
            in_type (str): type of transaction. It is either "deposit" or "withdraw".
            in_status (str): status of the transaction. It is either "Pending" or "Completed".
            in_amount (float): amount value of transaction
            in_description (str): description of the transaction
            in_pos (str): location of the pos that the transaction is occured
            in_credit_id (int): credit id
        Returns:
            None
        """
        LineItem.__init__(self, in_id, in_processing_date, in_effective_date,
                          in_type, in_status, in_amount, in_description, in_pos)
        self.credit_id = in_credit_id

    def insert_lineitem(self, db):
        """ Insert a new row to corresponding table in database. The row are fetched from current instance properties.
        Args:
            db (DB): DB instance
        Returns:
            None
        """
        table = db.get_table('credit_line_items')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            stmt = table.insert(). \
                values(
                credit_id=self.credit_id,
                cli_processing_date=self.processing_date,
                cli_effective_date=self.effective_date,
                cli_type=self.type,
                cli_status=self.status,
                cli_amount=self.amount,
                cli_description=self.description,
                cli_pos=self.pos
            )
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1