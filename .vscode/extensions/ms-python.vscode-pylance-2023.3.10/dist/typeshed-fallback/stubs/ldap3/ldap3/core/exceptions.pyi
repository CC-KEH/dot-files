import socket
from _typeshed import Incomplete
from typing import Any
from typing_extensions import Self

class LDAPException(Exception): ...

class LDAPOperationResult(LDAPException):
    def __new__(
        cls,
        result: Incomplete | None = ...,
        description: Incomplete | None = ...,
        dn: Incomplete | None = ...,
        message: Incomplete | None = ...,
        response_type: Incomplete | None = ...,
        response: Incomplete | None = ...,
    ) -> Self: ...
    result: Any
    description: Any
    dn: Any
    message: Any
    type: Any
    response: Any
    def __init__(
        self,
        result: Incomplete | None = ...,
        description: Incomplete | None = ...,
        dn: Incomplete | None = ...,
        message: Incomplete | None = ...,
        response_type: Incomplete | None = ...,
        response: Incomplete | None = ...,
    ) -> None: ...

class LDAPOperationsErrorResult(LDAPOperationResult): ...
class LDAPProtocolErrorResult(LDAPOperationResult): ...
class LDAPTimeLimitExceededResult(LDAPOperationResult): ...
class LDAPSizeLimitExceededResult(LDAPOperationResult): ...
class LDAPAuthMethodNotSupportedResult(LDAPOperationResult): ...
class LDAPStrongerAuthRequiredResult(LDAPOperationResult): ...
class LDAPReferralResult(LDAPOperationResult): ...
class LDAPAdminLimitExceededResult(LDAPOperationResult): ...
class LDAPUnavailableCriticalExtensionResult(LDAPOperationResult): ...
class LDAPConfidentialityRequiredResult(LDAPOperationResult): ...
class LDAPSASLBindInProgressResult(LDAPOperationResult): ...
class LDAPNoSuchAttributeResult(LDAPOperationResult): ...
class LDAPUndefinedAttributeTypeResult(LDAPOperationResult): ...
class LDAPInappropriateMatchingResult(LDAPOperationResult): ...
class LDAPConstraintViolationResult(LDAPOperationResult): ...
class LDAPAttributeOrValueExistsResult(LDAPOperationResult): ...
class LDAPInvalidAttributeSyntaxResult(LDAPOperationResult): ...
class LDAPNoSuchObjectResult(LDAPOperationResult): ...
class LDAPAliasProblemResult(LDAPOperationResult): ...
class LDAPInvalidDNSyntaxResult(LDAPOperationResult): ...
class LDAPAliasDereferencingProblemResult(LDAPOperationResult): ...
class LDAPInappropriateAuthenticationResult(LDAPOperationResult): ...
class LDAPInvalidCredentialsResult(LDAPOperationResult): ...
class LDAPInsufficientAccessRightsResult(LDAPOperationResult): ...
class LDAPBusyResult(LDAPOperationResult): ...
class LDAPUnavailableResult(LDAPOperationResult): ...
class LDAPUnwillingToPerformResult(LDAPOperationResult): ...
class LDAPLoopDetectedResult(LDAPOperationResult): ...
class LDAPNamingViolationResult(LDAPOperationResult): ...
class LDAPObjectClassViolationResult(LDAPOperationResult): ...
class LDAPNotAllowedOnNotLeafResult(LDAPOperationResult): ...
class LDAPNotAllowedOnRDNResult(LDAPOperationResult): ...
class LDAPEntryAlreadyExistsResult(LDAPOperationResult): ...
class LDAPObjectClassModsProhibitedResult(LDAPOperationResult): ...
class LDAPAffectMultipleDSASResult(LDAPOperationResult): ...
class LDAPOtherResult(LDAPOperationResult): ...
class LDAPLCUPResourcesExhaustedResult(LDAPOperationResult): ...
class LDAPLCUPSecurityViolationResult(LDAPOperationResult): ...
class LDAPLCUPInvalidDataResult(LDAPOperationResult): ...
class LDAPLCUPUnsupportedSchemeResult(LDAPOperationResult): ...
class LDAPLCUPReloadRequiredResult(LDAPOperationResult): ...
class LDAPCanceledResult(LDAPOperationResult): ...
class LDAPNoSuchOperationResult(LDAPOperationResult): ...
class LDAPTooLateResult(LDAPOperationResult): ...
class LDAPCannotCancelResult(LDAPOperationResult): ...
class LDAPAssertionFailedResult(LDAPOperationResult): ...
class LDAPAuthorizationDeniedResult(LDAPOperationResult): ...
class LDAPESyncRefreshRequiredResult(LDAPOperationResult): ...

exception_table: Any

class LDAPExceptionError(LDAPException): ...
class LDAPConfigurationError(LDAPExceptionError): ...
class LDAPUnknownStrategyError(LDAPConfigurationError): ...
class LDAPUnknownAuthenticationMethodError(LDAPConfigurationError): ...
class LDAPSSLConfigurationError(LDAPConfigurationError): ...
class LDAPDefinitionError(LDAPConfigurationError): ...
class LDAPPackageUnavailableError(LDAPConfigurationError, ImportError): ...
class LDAPConfigurationParameterError(LDAPConfigurationError): ...
class LDAPKeyError(LDAPExceptionError, KeyError, AttributeError): ...
class LDAPObjectError(LDAPExceptionError, ValueError): ...
class LDAPAttributeError(LDAPExceptionError, ValueError, TypeError): ...
class LDAPCursorError(LDAPExceptionError): ...
class LDAPCursorAttributeError(LDAPCursorError, AttributeError): ...
class LDAPObjectDereferenceError(LDAPExceptionError): ...
class LDAPSSLNotSupportedError(LDAPExceptionError, ImportError): ...
class LDAPInvalidTlsSpecificationError(LDAPExceptionError): ...
class LDAPInvalidHashAlgorithmError(LDAPExceptionError, ValueError): ...
class LDAPSignatureVerificationFailedError(LDAPExceptionError): ...
class LDAPBindError(LDAPExceptionError): ...
class LDAPInvalidServerError(LDAPExceptionError): ...
class LDAPSASLMechanismNotSupportedError(LDAPExceptionError): ...
class LDAPConnectionIsReadOnlyError(LDAPExceptionError): ...
class LDAPChangeError(LDAPExceptionError, ValueError): ...
class LDAPServerPoolError(LDAPExceptionError): ...
class LDAPServerPoolExhaustedError(LDAPExceptionError): ...
class LDAPInvalidPortError(LDAPExceptionError): ...
class LDAPStartTLSError(LDAPExceptionError): ...
class LDAPCertificateError(LDAPExceptionError): ...
class LDAPUserNameNotAllowedError(LDAPExceptionError): ...
class LDAPUserNameIsMandatoryError(LDAPExceptionError): ...
class LDAPPasswordIsMandatoryError(LDAPExceptionError): ...
class LDAPInvalidFilterError(LDAPExceptionError): ...
class LDAPInvalidScopeError(LDAPExceptionError, ValueError): ...
class LDAPInvalidDereferenceAliasesError(LDAPExceptionError, ValueError): ...
class LDAPInvalidValueError(LDAPExceptionError, ValueError): ...
class LDAPControlError(LDAPExceptionError, ValueError): ...
class LDAPExtensionError(LDAPExceptionError, ValueError): ...
class LDAPLDIFError(LDAPExceptionError): ...
class LDAPSchemaError(LDAPExceptionError): ...
class LDAPSASLPrepError(LDAPExceptionError): ...
class LDAPSASLBindInProgressError(LDAPExceptionError): ...
class LDAPMetricsError(LDAPExceptionError): ...
class LDAPObjectClassError(LDAPExceptionError): ...
class LDAPInvalidDnError(LDAPExceptionError): ...
class LDAPResponseTimeoutError(LDAPExceptionError): ...
class LDAPTransactionError(LDAPExceptionError): ...
class LDAPInfoError(LDAPExceptionError): ...
class LDAPCommunicationError(LDAPExceptionError): ...
class LDAPSocketOpenError(LDAPCommunicationError): ...
class LDAPSocketCloseError(LDAPCommunicationError): ...
class LDAPSocketReceiveError(LDAPCommunicationError, socket.error): ...
class LDAPSocketSendError(LDAPCommunicationError, socket.error): ...
class LDAPSessionTerminatedByServerError(LDAPCommunicationError): ...
class LDAPUnknownResponseError(LDAPCommunicationError): ...
class LDAPUnknownRequestError(LDAPCommunicationError): ...
class LDAPReferralError(LDAPCommunicationError): ...
class LDAPConnectionPoolNameIsMandatoryError(LDAPExceptionError): ...
class LDAPConnectionPoolNotStartedError(LDAPExceptionError): ...
class LDAPMaximumRetriesError(LDAPExceptionError): ...

def communication_exception_factory(exc_to_raise, exc): ...
def start_tls_exception_factory(exc): ...
