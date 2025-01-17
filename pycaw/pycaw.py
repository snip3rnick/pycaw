"""
Python wrapper around the Core Audio Windows API.
"""
# import here all newly split up modules,
# to keep backwards compatibility

# flake8: noqa
# yes, the imports are unused

from pycaw.api.audioclient import IAudioClient, ISimpleAudioVolume
from pycaw.api.audioclient.depend import WAVEFORMATEX
from pycaw.api.audiopolicy import (
    IAudioSessionControl,
    IAudioSessionControl2,
    IAudioSessionEnumerator,
    IAudioSessionEvents,
    IAudioSessionManager,
    IAudioSessionManager2,
)
from pycaw.api.endpointvolume import (
    IAudioEndpointVolume,
    IAudioEndpointVolumeCallback,
    IAudioMeterInformation,
)
from pycaw.api.endpointvolume.depend import (
    AUDIO_VOLUME_NOTIFICATION_DATA,
    PAUDIO_VOLUME_NOTIFICATION_DATA,
)
from pycaw.api.mmdeviceapi import IMMDevice, IMMDeviceCollection, IMMDeviceEnumerator
from pycaw.api.mmdeviceapi.depend import IPropertyStore
from pycaw.api.mmdeviceapi.depend.structures import (
    PROPERTYKEY,
    PROPVARIANT,
    PROPVARIANT_UNION,
)
from pycaw.api.policyconfig import (
    IPolicyConfig,
    IPolicyConfigVista,
)
from pycaw.constants import (
    CLSID_MMDeviceEnumerator,
    CLSID_PolicyConfigClient,
    CLSID_PolicyConfigVistaClient,
    AUDCLNT_SHAREMODE,
    DEVICE_STATE,
    STGM,
    AudioDeviceState,
    EDataFlow,
    ERole,
)
from pycaw.utils import AudioDevice, AudioDeviceEnumerator, AudioSession, AudioUtilities
