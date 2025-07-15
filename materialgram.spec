Name:           materialgram
Version:        5.16.4.1
Release:        2%{?dist}
Summary:        Telegram Desktop fork with material icons and some improvements
Vendor:         burhancodes
Group:          Applications/Internet
Packager:       Burhanverse  <contact@burhanverse.eu.org>
License:        GPLv3
URL:            https://github.com/kukuruzka165/materialgram
Source0:        https://github.com/kukuruzka165/materialgram/releases/download/v%{version}/materialgram-v%{version}.tar.gz

%description
Telegram Desktop fork with Material Design and other improvements, which is based on the Telegram API and the MTProto secure protocol.

Author: kukuruzka  <kukuruzka165@github.com>

BuildRequires: tar
BuildRequires: sed
BuildRequires: desktop-file-utils

Requires: hicolor-icon-theme
Requires: desktop-file-utils
Requires: shared-mime-info

%prep
tar -xvf %{_sourcedir}/materialgram-v%{version}.tar.gz -C %{_sourcedir}
cd %{_sourcedir}/

%build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/dbus-1
mkdir -p %{buildroot}/usr/share/icons
mkdir -p %{buildroot}/usr/share/metainfo

cp -a %{_sourcedir}/usr/bin/materialgram %{buildroot}/usr/bin/

cp -a %{_sourcedir}/usr/share/* %{buildroot}/usr/share/

chmod +x %{buildroot}/usr/bin/materialgram

desktop-file-validate %{buildroot}/usr/share/applications/io.github.kukuruzka165.materialgram.desktop

%files
/usr/bin/materialgram
%dir /usr/share/applications
/usr/share/applications/*
%dir /usr/share/dbus-1
/usr/share/dbus-1/*
%dir /usr/share/icons
/usr/share/icons/*
%dir /usr/share/metainfo
/usr/share/metainfo/*

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

if [ "$1" -eq 0 ]; then
  USER_HOME="/home/${SUDO_USER:-$USER}"

  if [ -d "$USER_HOME/.local/share/materialgram" ]; then
    rm -rf "$USER_HOME/.local/share/materialgram"
  fi
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Tue Jul 15 2025 Burhanverse <contact@burhanverse.eu.org> - 5.16.4.1-2
- Updated to version 5.16.4.1