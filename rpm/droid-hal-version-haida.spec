# Device specific configs

# rpm_device is the name of the ported device
%define rpm_device haida
# rpm_vendor is used in the rpm space (the vendor doing the port)
%define rpm_vendor semc

# Manufacturer and device name to be shown in UI
%define vendor_pretty Sony Ericsson
%define device_pretty Xperia Neo V

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc
