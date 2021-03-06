"""Base RFC functionality"""


import sap
import sap.errors


SAPRFC_MODULE = None


def mod_log():
    """rfc.core module logger"""

    return sap.get_logger()


def _try_import_pyrfc():

    # pylint: disable=global-statement
    global SAPRFC_MODULE

    try:
        import pyrfc
    except ImportError as ex:
        mod_log().info('Failed to import the module pyrfc')
        mod_log().debug(str(ex))
    else:
        SAPRFC_MODULE = pyrfc


def _unimport_pyrfc():
    """For the sake of testing"""

    # pylint: disable=global-statement
    global SAPRFC_MODULE

    SAPRFC_MODULE = None


def rfc_is_available():
    """Returns true if RFC can be used"""

    if SAPRFC_MODULE is None:
        _try_import_pyrfc()

    return SAPRFC_MODULE is not None


def connect(host, sysnr, client, user, password):
    """ADT Connection for HTTP communication built on top Python requests.
    """

    if not rfc_is_available():
        raise sap.errors.SAPCliError('RFC functionality is not available(enabled)')

    mod_log().info('Connecting to HOST=%s SYSNR=%s CLIENT=%s as %s', host, sysnr, client, user)
    return SAPRFC_MODULE.Connection(ashost=host,
                                    sysnr=sysnr,
                                    client=client,
                                    user=user,
                                    passwd=password)
