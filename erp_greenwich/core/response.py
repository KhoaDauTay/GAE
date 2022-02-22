from rest_framework.response import Response


class APIResponse(Response):
    """API Response format for create, update, delete API (exclude get)"""

    def __init__(
        self,
        status: int,
        data: dict = None,
        messages: list = "",
        error_code: int = 0,
        success: bool = False,
    ):
        self.data = {
            "success": success or False,
            "messages": messages,
            "error_code": error_code,
            "data": data,
        }
        super().__init__(data=self.data, status=status)
