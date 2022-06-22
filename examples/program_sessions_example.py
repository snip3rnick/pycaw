"""
Get a list of all devices with the device enumerator.
"""
from pycaw.pycaw import AudioDeviceEnumerator, AudioDeviceState


def main():
    devices  = AudioDeviceEnumerator()
    sessions_by_pid = {}
    for device in devices.GetDevices(state=AudioDeviceState.Active):
        device_sessions = device.GetAllSessions()
        for session in device_sessions:
            spid = sessions_by_pid.get(session.ProcessId, [])
            spid.append(session)
            sessions_by_pid[session.ProcessId] = spid

    for pid, sessions in sessions_by_pid.items():
        session = sessions[0]
        name = session.DisplayName or session.Process.name().rsplit(".exe", 1)[0].title()
        print(f"[{pid}]".ljust(10), name.ljust(20),
              f"({len(sessions)} session{len(sessions) != 1 and 's' or ''})")


if __name__ == "__main__":
    main()
