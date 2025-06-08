from enum import Enum


class RecoveryMethodEnum(Enum):
    EMAIL = "EMAIL"
    CODE = "CODE"


class VerificationCodeTypeEnum(Enum):
    VerifyEmail = "VERIFY_EMAIL"
    RecoveryMethodEmail = "RECOVERY_METHOD_EMAIL"
    RecoveryMethodCode = "RECOVERY_METHOD_CODE"
