from fastapi import HTTPException, status

class AnalyticError(HTTPException):
    def __init__(self, detail: str = "Analytic processing failed"):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
