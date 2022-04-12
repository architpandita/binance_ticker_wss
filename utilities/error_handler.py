from utilities.base_exception import PkgError
"""
Each error represent specific part of the code that failed.
We can decide and add code according to the requirement.
"""

class UserInputError(PkgError):
    # if User  input is not validated passed
    pass


class MarketHighAlertError(PkgError):
    pass

class StartAlertError(PkgError):
    pass