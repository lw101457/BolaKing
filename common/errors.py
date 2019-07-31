from starlette.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN


def raise_400(code):
    raise HTTPException(
        status_code=HTTP_400_BAD_REQUEST,
        detail={
            "code": code,
            "detail": ""
        }
    )


def raise_401(code):
    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={
            "code": code,
            "detail": ""
        }
    )


def raise_403(code):
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN,
        detail={
            "code": code,
            "detail": ""
        }
    )
