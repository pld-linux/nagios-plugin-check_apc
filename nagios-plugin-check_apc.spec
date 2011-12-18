#
# another version of this plugin is here:
# http://www.opennet.ru/base/sys/apc_ups_nagios.txt.html

%define		plugin	check_apc
Summary:	Nagios Plugin for apcupsd APC Smart-UPS
Summary(pl.UTF-8):	Wtyczka Nagiosa do sprawdzania apcupsd APC Smart-UPS
Name:		nagios-plugin-check_apc
Version:	0.0.2
Release:	0.3
License:	GPL
Group:		Networking
Source0:	http://www.negative1.org/check_apc/check_apc
# Source0-md5:	8d3770144e00a4ab41879c7a8b876065
Patch0:		%{name}-path.patch
URL:		http://www.negative1.org/
Requires:	apcupsd
Requires:	nagios-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_libdir}/nagios/plugins

%description
check_apc is a Nagios plugin that can be used with apcupsd or apcsnmp
to monitor an APC UPS.

%description -l pl.UTF-8
check_apc to wtyczka Nagiosa do monitorowania UPS-ów APC przy użyciu
apcupsd lub apcsnmp.

%prep
%setup -qcT
install -p %{SOURCE0} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/%{plugin}
