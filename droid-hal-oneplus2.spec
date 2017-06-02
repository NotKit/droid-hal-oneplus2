# These and other macros are documented in dhd/droid-hal-device.inc
%define device oneplus2
%define vendor oneplus
%define vendor_pretty OnePlus
%define device_pretty OnePlus 2
%define installable_zip 1
%define droid_target_aarch64 1
%define straggler_files \
/init.qcom.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
%{nil}
%include rpm/dhd/droid-hal-device.inc
