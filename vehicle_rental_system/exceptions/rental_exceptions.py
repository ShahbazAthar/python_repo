"""
Custom exception hierarchy for the Vehicle Rental Management System.

Everything the system can go wrong in gets its own exception type,
so calling code can catch precisely what it cares about instead of
a bare `except Exception`.
"""


class RentalException(Exception):
    """Base class for every exception raised by this system."""
    pass


class ValidationError(RentalException):
    """Raised when a Customer or Vehicle field fails validation
    (e.g. empty name, empty registration number)."""
    pass


class VehicleUnavailableError(RentalException):
    """Raised when a rental is attempted on a vehicle that's already rented."""
    pass


class InvalidRentalDurationError(RentalException):
    """Raised when rental days is zero, negative, or not a whole number."""
    pass


class PaymentFailureError(RentalException):
    """Raised when a PaymentProcessor implementation fails to process payment."""
    pass


class VehicleUnderMaintenanceError(RentalException):
    """Raised when a rental is attempted on a vehicle flagged for
    maintenance. (bonus feature)"""
    pass


class InvalidOperationError(RentalException):
    """Raised for any other invalid operation, e.g. returning a
    vehicle that was never rented out."""
    pass