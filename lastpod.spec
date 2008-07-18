%define name lastpod
%define version 1.1
%define svn r103
%define release %mkrel 1

Summary: Submits the songs played on an iPod to last.fm
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{svn}.tar.bz2
License: GPLv2+
Group: Sound
Url: http://www.lastpod.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: java-devel
BuildRequires: ant-junit
Requires: java

%description
LastPod is a graphical tool that submits the music played on the iPod to the
last.fm web site.


%prep
%setup -q -n %name

%build
cd bin
ant dist

%install
rm -rf $RPM_BUILD_ROOT
install -D dist/lastPod.jar %buildroot%_datadir/%name/lastPod.jar
install -d %buildroot{%_bindir,%_datadir/applications}
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
java -jar %_datadir/%name/lastPod.jar
EOF
cat > %buildroot%_datadir/applications/mandriva-%name.desktop << EOF
[Desktop Entry]
Name=LastPod
Comment=Submit songs played on the iPod to last.fm
Exec=%{_bindir}/%{name}
Icon=multimedia-player
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;Audio;Java;
MimeType=x-content/audio-player;
EOF


%check
cd bin
ant test

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%clean_desktop_database

%files
%defattr(-,root,root)
%attr(755,root,root) %_bindir/%name
%_datadir/%name
%_datadir/applications/mandriva-%name.desktop
