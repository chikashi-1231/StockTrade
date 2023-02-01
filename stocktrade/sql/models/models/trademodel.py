class SellingStock:
    """
    株を売却する際に情報を持たせるモデル
    """
    def __init__(self, symbolID, amount, price):
        self.symbolID = symbolID
        self.amount = amount
        self.price = price
