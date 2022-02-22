from typing import Any

from rest_framework import status
from rest_framework.exceptions import APIException


class APIValidationError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid input."
    default_code = "invalid"

    def __init__(self, errors: Any = None):
        """

        :param errors: [{"error_field_name": "error message"}, ]
        """
        if isinstance(errors, list):
            self.errors = errors
        else:
            self.errors = [errors]
        self.error_details = []
        for error in self.errors:
            if isinstance(error, dict):
                # Get error field name
                key = next(iter(error))
                self.error_details.append({"field": key, "message": error[key]})
        self.detail = {"errors": self.error_details}
