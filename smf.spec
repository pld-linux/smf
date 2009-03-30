Summary:	Simple Machines Forum
Name:		smf
Version:	1.1.8
Release:	0.1
License:	BSD
Group:		Applications/WWW
Source0:	http://download.simplemachines.org/index.php/%{name}_1-1-8_install.tar.bz2
# Source0-md5:	59dbc27b2f6db056dd68c6af4c6d7bca
URL:		http://www.simplemachines.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	webapps
Requires:	webserver(php) >= 4.3.0
Requires:	php-mysql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
Simple Machines Forum — SMF in short — is a free, professional
grade software package that allows you to set up your own online
community within minutes.

Its powerful custom made template engine puts you in full control of
the lay-out of your message board and with our unique SSI - or Server
Side Includes
- function you can let your forum and your website interact with each
  other.

SMF is written in the popular language PHP and uses a MySQL database.
It is designed to provide you with all the features you need from a
bulletin board while having an absolute minimal impact on the
resources of the server. SMF is the next generation of forum software.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a . $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php
