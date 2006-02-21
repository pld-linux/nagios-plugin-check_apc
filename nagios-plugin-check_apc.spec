#
# another version this plugin is here:
# http://www.opennet.ru/base/sys/apc_ups_nagios.txt.html
#
%define		namescript check_apc
%include	/usr/lib/rpm/macros.perl
Summary:	Nagios Plugin for apcupsd APC Smart-UPS
Summary(pl):	Wtyczka Nagiosa do sprawdzania apcupsd APC Smart-UPS
Name:		nagios-plugin-check_apc
Version:	0.0.2
Release:	0.1
License:	GPL
Group:		Networking
Source0:	http://www.negative1.org/check_apc/check_apc
# Source0-md5:	8d3770144e00a4ab41879c7a8b876065
#Patch0:	check_apc-path.patch
URL:		http://www.negative1.org
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	nagios-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/nagios/plugins
%define		_sysconfdir	/etc/nagios/plugins

#define		_noautoreq 'perl(utils)'

%description
check_apc is a Nagios plugin that can be used with apcupsd or apcsnmp to monitor an APC UPS.

%description -l pl
check_apc wtyczka Nagiosa do sprawdzania apcupsd.

%prep
%setup -q -c -T
install %{SOURCE0} .
#%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp %{namescript}  $RPM_BUILD_ROOT%{_plugindir}/%{namescript}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/*
