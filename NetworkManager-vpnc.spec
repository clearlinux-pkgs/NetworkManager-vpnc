#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : NetworkManager-vpnc
Version  : 1.2.6
Release  : 3
URL      : https://download.gnome.org/sources/NetworkManager-vpnc/1.2/NetworkManager-vpnc-1.2.6.tar.xz
Source0  : https://download.gnome.org/sources/NetworkManager-vpnc/1.2/NetworkManager-vpnc-1.2.6.tar.xz
Summary  : NetworkManager VPN plugin for VPNC
Group    : Development/Tools
License  : GPL-2.0
Requires: NetworkManager-vpnc-data = %{version}-%{release}
Requires: NetworkManager-vpnc-lib = %{version}-%{release}
Requires: NetworkManager-vpnc-libexec = %{version}-%{release}
Requires: NetworkManager-vpnc-license = %{version}-%{release}
Requires: NetworkManager-vpnc-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(NetworkManager)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libnm)
BuildRequires : pkgconfig(libnm-glib)
BuildRequires : pkgconfig(libnm-glib-vpn)
BuildRequires : pkgconfig(libnm-gtk)
BuildRequires : pkgconfig(libnm-util)
BuildRequires : pkgconfig(libnma)
BuildRequires : pkgconfig(libsecret-1)

%description
Client for Cisco IPsec virtual private networks
Support for configuring virtual private networks based on VPNC.
Compatible with Cisco VPN concentrators configured to use IPsec.

%package data
Summary: data components for the NetworkManager-vpnc package.
Group: Data

%description data
data components for the NetworkManager-vpnc package.


%package lib
Summary: lib components for the NetworkManager-vpnc package.
Group: Libraries
Requires: NetworkManager-vpnc-data = %{version}-%{release}
Requires: NetworkManager-vpnc-libexec = %{version}-%{release}
Requires: NetworkManager-vpnc-license = %{version}-%{release}

%description lib
lib components for the NetworkManager-vpnc package.


%package libexec
Summary: libexec components for the NetworkManager-vpnc package.
Group: Default
Requires: NetworkManager-vpnc-license = %{version}-%{release}

%description libexec
libexec components for the NetworkManager-vpnc package.


%package license
Summary: license components for the NetworkManager-vpnc package.
Group: Default

%description license
license components for the NetworkManager-vpnc package.


%package locales
Summary: locales components for the NetworkManager-vpnc package.
Group: Default

%description locales
locales components for the NetworkManager-vpnc package.


%prep
%setup -q -n NetworkManager-vpnc-1.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557021517
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1557021517
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/NetworkManager-vpnc
cp COPYING %{buildroot}/usr/share/package-licenses/NetworkManager-vpnc/COPYING
%make_install
%find_lang NetworkManager-vpnc

%files
%defattr(-,root,root,-)
/usr/lib/NetworkManager/VPN/nm-vpnc-service.name

%files data
%defattr(-,root,root,-)
/usr/share/appdata/network-manager-vpnc.metainfo.xml
/usr/share/dbus-1/system.d/nm-vpnc-service.conf
/usr/share/gnome-vpn-properties/vpnc/nm-vpnc-dialog.ui

%files lib
%defattr(-,root,root,-)
/usr/lib64/NetworkManager/libnm-vpn-plugin-vpnc-editor.so
/usr/lib64/NetworkManager/libnm-vpn-plugin-vpnc.so
/usr/lib64/NetworkManager/libnm-vpnc-properties.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/nm-vpnc-auth-dialog
/usr/libexec/nm-vpnc-service
/usr/libexec/nm-vpnc-service-vpnc-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/NetworkManager-vpnc/COPYING

%files locales -f NetworkManager-vpnc.lang
%defattr(-,root,root,-)

