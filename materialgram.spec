Name:           materialgram
Version:        5.15.2.1
Release:        1%{?dist}
Summary:        Telegram Desktop fork with material icons and some improvements
Vendor:         burhancodes
Group:          Applications/Internet
Packager:       Burhanverse  <contact@burhanverse.eu.org>
License:        GPLv3
URL:            https://github.com/kukuruzka165/materialgram
Source0:        https://github.com/kukuruzka165/materialgram/releases/download/v%{version}/materialgram-v%{version}.tar.gz

BuildRequires:  tar
BuildRequires:  sed
Requires:       python3

%description
Telegram Desktop fork with Material Design and other improvements, which is based on the Telegram API and the MTProto secure protocol.

Author: kukuruzka  <kukuruzka165@github.com>

%prep
tar -xvf %{_sourcedir}/materialgram-v%{version}.tar.gz -C %{_sourcedir}
cd %{_sourcedir}/
# Fix for Mageia 8
%if 0%{?mageia_version} == 8
    sed -i 's/^SingleMainWindow=/X-SingleMainWindow=/' \
        %{buildroot}/usr/share/applications/io.github.kukuruzka165.materialgram.desktop
%endif

%build

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/dbus-1
mkdir -p %{buildroot}/usr/share/icons
mkdir -p %{buildroot}/usr/share/metainfo

cp -a %{_sourcedir}/usr/bin/materialgram %{buildroot}/usr/bin/

cp -a %{_sourcedir}/usr/share/* %{buildroot}/usr/share/

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

%preun
  pkill -f '/usr/bin/materialgram' || true

%postun
if [ "$1" -eq 0 ]; then
  USER_HOME="/home/${SUDO_USER:-$USER}"

  if [ -d "$USER_HOME/.local/share/materialgram" ]; then
    rm -rf "$USER_HOME/.local/share/materialgram"
  fi
fi
