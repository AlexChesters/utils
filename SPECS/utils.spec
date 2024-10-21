%define name alexchesters-utils
%{!?version: %{error: Version is not defined}}
%define release 1
%define buildroot %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Name: %{name}
Version: %{version}
Release: %{release}
Summary: A collection of various utilities packaged as an RPM

Group: Installation Script
License: MIT
Source: %{name}.tar.gz
BuildRoot: %{buildroot}
AutoReqProv: no

%description
A collection of various utilities packaged as an RPM

%prep
%setup -q -c -n %{name}

%install
mkdir -p %{buildroot}/usr/lib/alexchesters-utils
cp -R ./src/. %{buildroot}/usr/lib/alexchesters-utils
mkdir -p %{buildroot}/var/log/alexchesters-utils

%post
ln -s /usr/lib/alexchesters-utils/* /usr/bin

%clean
rm -rf %{buildroot}

%files
%defattr(755, root, root, 755)
/usr/lib/alexchesters-utils
/var/log/alexchesters-utils
