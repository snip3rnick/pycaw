from ctypes import HRESULT, POINTER, Structure, c_int
from ctypes.wintypes import DWORD, LPCWSTR, WORD, INT, LARGE_INTEGER, BOOL

from comtypes import COMMETHOD, GUID, IUnknown

from ..mmdeviceapi.depend import PROPVARIANT, PROPERTYKEY


INT64 = LARGE_INTEGER
PINT64 = POINTER(INT64)


class WAVEFORMATEX(Structure):
    _fields_ = [
        ("wFormatTag",      WORD),
        ("nChannels",       WORD),
        ("nSamplesPerSec",  DWORD),
        ("nAvgBytesPerSec", DWORD),
        ("nBlockAlign",     WORD),
        ("wBitsPerSample",  WORD),
        ("cbSize",          WORD),
    ]


# public enum DeviceShareMode
# {
#     Shared,
#     Exclusive
# }
DeviceShareMode = c_int


class IPolicyConfig(IUnknown):
    _iid_ = GUID("{F8679F50-850A-41CF-9C72-430F290290C8}")
    _methods_ = (
        # HRESULT GetMixFormat(
        # [in] PCWSTR wszDeviceId,
        # [out] WAVEFORMATEX **ppFormat);
        COMMETHOD(
            [],
            HRESULT,
            "GetMixFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["out"], POINTER(POINTER(WAVEFORMATEX)), "ppFormat"),
        ),
        # HRESULT STDMETHODCALLTYPE GetDeviceFormat(
        # [in] PCWSTR wszDeviceId,
        # [in] BOOL bDefault,
        # [out] WAVEFORMATEX **ppFormat);
        COMMETHOD(
            [],
            HRESULT,
            "GetDeviceFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], BOOL, "bDefault"),
            (["out"], POINTER(POINTER(WAVEFORMATEX)), "ppFormat"),
        ),
        # HRESULT STDMETHODCALLTYPE ResetDeviceFormat(
        # [in] PCWSTR wszDeviceId);
        COMMETHOD(
            [],
            HRESULT,
            "ResetDeviceFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
        ),
        # HRESULT STDMETHODCALLTYPE SetDeviceFormat(
        # [in] PCWSTR wszDeviceId,
        # [in] WAVEFORMATEX *pEndpointFormat,
        # [in] WAVEFORMATEX *pMixFormat);
        COMMETHOD(
            [],
            HRESULT,
            "SetDeviceFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], POINTER(WAVEFORMATEX), "pEndpointFormat"),
            (["in"], POINTER(WAVEFORMATEX), "pMixFormat"),
        ),
        # HRESULT STDMETHODCALLTYPE GetProcessingPeriod(
        # [in] PCWSTR wszDeviceId,
        # [in] BOOL bDefault,
        # [out] PINT64 pmftDefaultPeriod,
        # [out] PINT64 pmftMinimumPeriod);
        COMMETHOD(
            [],
            HRESULT,
            "GetProcessingPeriod",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], BOOL, "bDefault"),
            (["out"], PINT64, "pmftDefaultPeriod"),
            (["out"], PINT64, "pmftMinimumPeriod"),
        ),
        # HRESULT STDMETHODCALLTYPE SetProcessingPeriod(
        # [in] PCWSTR wszDeviceId,
        # [in] INT64 pmftPeriod);
        COMMETHOD(
            [],
            HRESULT,
            "SetProcessingPeriod",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], INT64, "pmftPeriod"),
        ),
        # HRESULT STDMETHODCALLTYPE GetShareMode(
        # [in] PCWSTR wszDeviceId,
        # [out] DeviceShareMode *);
        COMMETHOD(
            [],
            HRESULT,
            "GetShareMode",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["out"], POINTER(DeviceShareMode), "pMode"),
        ),
        # HRESULT STDMETHODCALLTYPE SetShareMode(
        # [in] PCWSTR wszDeviceId,
        # [in] DeviceShareMode);
        COMMETHOD(
            [],
            HRESULT,
            "SetShareMode",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], DeviceShareMode, "mode"),
        ),
        # HRESULT STDMETHODCALLTYPE GetPropertyValue(
        # [in] PCWSTR wszDeviceId,
        # [in] const PROPERTYKEY &pKey,
        # [out] PROPVARIANT *pv);
        COMMETHOD(
            [],
            HRESULT,
            "GetPropertyValue",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], POINTER(PROPERTYKEY), "pKey"),
            (["out"], POINTER(PROPVARIANT), "pv"),
        ),
        # HRESULT STDMETHODCALLTYPE SetPropertyValue(
        # [in] PCWSTR wszDeviceId,
        # [in] const PROPERTYKEY &pKey,
        # [in] PROPVARIANT &pv);
        COMMETHOD(
            [],
            HRESULT,
            "SetPropertyValue",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], POINTER(PROPERTYKEY), "pKey"),
            (["in"], POINTER(PROPVARIANT), "pv"),
        ),
        # HRESULT STDMETHODCALLTYPE SetDefaultEndpoint(
        # [in] PCWSTR wszDeviceId,
        # [in] ERole eRole);
        COMMETHOD(
            [],
            HRESULT,
            "SetDefaultEndpoint",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], DWORD, "role"),
        ),
        # HRESULT STDMETHODCALLTYPE SetEndpointVisibility(
        # [in] PCWSTR wszDeviceId,
        # [in] INT);
        COMMETHOD(
            [],
            HRESULT,
            "SetEndpointVisibility",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], BOOL, "bVisible"),
        ),
    )


class IPolicyConfigVista(IUnknown):
    _iid_ = GUID("{568b9108-44bf-40b4-9006-86afe5b5a620}")
    _methods_ = (
        # HRESULT GetMixFormat(
        # [in] PCWSTR wszDeviceId,
        # [out] WAVEFORMATEX **ppFormat);  // not available on Windows 7, use method from IPolicyConfig
        COMMETHOD(
            [],
            HRESULT,
            "GetMixFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["out"], POINTER(POINTER(WAVEFORMATEX)), "ppFormat"),
        ),
        # HRESULT STDMETHODCALLTYPE GetDeviceFormat(
        # [in] PCWSTR wszDeviceId,
        # [in] BOOL bDefault,
        # [out] WAVEFORMATEX **ppFormat);
        COMMETHOD(
            [],
            HRESULT,
            "GetDeviceFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], BOOL, "bDefault"),
            (["out"], POINTER(POINTER(WAVEFORMATEX)), "ppFormat"),
        ),
        # HRESULT STDMETHODCALLTYPE ResetDeviceFormat(
        # [in] PCWSTR wszDeviceId);
        COMMETHOD(
            [],
            HRESULT,
            "ResetDeviceFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
        ),
        # HRESULT STDMETHODCALLTYPE SetDeviceFormat(
        # [in] PCWSTR wszDeviceId,
        # [in] WAVEFORMATEX *pEndpointFormat,
        # [in] WAVEFORMATEX *pMixFormat);
        COMMETHOD(
            [],
            HRESULT,
            "SetDeviceFormat",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], POINTER(WAVEFORMATEX), "pEndpointFormat"),
            (["in"], POINTER(WAVEFORMATEX), "pMixFormat"),
        ),
        # HRESULT STDMETHODCALLTYPE GetProcessingPeriod(
        # [in] PCWSTR wszDeviceId,
        # [in] BOOL bDefault,
        # [out] PINT64 pmftDefaultPeriod,
        # [out] PINT64 pmftMinimumPeriod);  // not available on Windows 7, use method from IPolicyConfig
        COMMETHOD(
            [],
            HRESULT,
            "GetProcessingPeriod",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], BOOL, "bDefault"),
            (["out"], PINT64, "pmftDefaultPeriod"),
            (["out"], PINT64, "pmftMinimumPeriod"),
        ),
        # HRESULT STDMETHODCALLTYPE SetProcessingPeriod(
        # [in] PCWSTR wszDeviceId,
        # [in] INT64 pmftPeriod);  // not available on Windows 7, use method from IPolicyConfig
        COMMETHOD(
            [],
            HRESULT,
            "SetProcessingPeriod",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], INT64, "pmftPeriod"),
        ),
        # HRESULT STDMETHODCALLTYPE GetShareMode(
        # [in] PCWSTR wszDeviceId,
        # [out] DeviceShareMode *);  // not available on Windows 7, use method from IPolicyConfig
        COMMETHOD(
            [],
            HRESULT,
            "GetShareMode",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["out"], POINTER(DeviceShareMode), "pMode"),
        ),
        # HRESULT STDMETHODCALLTYPE SetShareMode(
        # [in] PCWSTR wszDeviceId,
        # [in] DeviceShareMode);  // not available on Windows 7, use method from IPolicyConfig
        COMMETHOD(
            [],
            HRESULT,
            "SetShareMode",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], DeviceShareMode, "mode"),
        ),
        # HRESULT STDMETHODCALLTYPE GetPropertyValue(
        # [in] PCWSTR wszDeviceId,
        # [in] const PROPERTYKEY &pKey,
        # [out] PROPVARIANT *pv);
        COMMETHOD(
            [],
            HRESULT,
            "GetPropertyValue",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], POINTER(PROPERTYKEY), "pKey"),
            (["out"], POINTER(PROPVARIANT), "pv"),
        ),
        # HRESULT STDMETHODCALLTYPE SetPropertyValue(
        # [in] PCWSTR wszDeviceId,
        # [in] const PROPERTYKEY &pKey,
        # [in] PROPVARIANT &pv);
        COMMETHOD(
            [],
            HRESULT,
            "SetPropertyValue",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], POINTER(PROPERTYKEY), "pKey"),
            (["in"], POINTER(PROPVARIANT), "pv"),
        ),
        # HRESULT STDMETHODCALLTYPE SetDefaultEndpoint(
        # [in] PCWSTR wszDeviceId,
        # [in] ERole eRole);
        COMMETHOD(
            [],
            HRESULT,
            "SetDefaultEndpoint",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], DWORD, "role"),
        ),
        # HRESULT STDMETHODCALLTYPE SetEndpointVisibility(
        # [in] PCWSTR wszDeviceId,
        # [in] BOOL bVisible);  // not available on Windows 7, use method from IPolicyConfig
        COMMETHOD(
            [],
            HRESULT,
            "SetEndpointVisibility",
            (["in"], LPCWSTR, "wszDeviceId"),
            (["in"], BOOL, "bVisible"),
        ),
    )
