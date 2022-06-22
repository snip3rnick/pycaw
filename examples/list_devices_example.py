"""
Get a list of all devices with the device enumerator.
"""
from pycaw.pycaw import AudioDeviceEnumerator, AudioDeviceState


def main():
    devices = AudioDeviceEnumerator()
    device_by_state  = dict((state, []) for state in AudioDeviceState)
    for device in devices.GetDevices():
        device_by_state[device.state].append(device)
    for state in AudioDeviceState:
        print(state.name)
        for device in device_by_state[state]:
            print("  ", device.FriendlyName)


if __name__ == "__main__":
    main()
