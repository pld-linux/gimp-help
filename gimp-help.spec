Summary:	Help files for the GIMP
Summary(pl):	Pliki pomocy dla GIMP
Name:		gimp-help-2
Version:	0.5
Release:	0.1
License:	GPL
Group:		Documentation
Source0:	ftp://ftp.gimp.org/pub/gimp/help/testing/%{name}-%{version}.tar.gz
# Source0-md5:	4b10833a545842ee4436a75eea68fd42
URL:		http://wiki.gimp.org/gimp/GimpDocs
Requires:	gimp >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
#The GIMP User Manual is a newly written User Manual for the GIMP.

#stupid description, please don't give rel 1 without change it!

%description -l pl

%prep
%setup -q

%build
%configure \
	--without-gimp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/gimp/2.0/help
%dir %{_datadir}/gimp/2.0/help/images
%{_datadir}/gimp/2.0/help/images/*.png
%{_datadir}/gimp/2.0/help/images/callouts
%dir %{_datadir}/gimp/2.0/help/images/dialogs
%{_datadir}/gimp/2.0/help/images/dialogs/*.png
%{_datadir}/gimp/2.0/help/images/dialogs/examples
%dir %{_datadir}/gimp/2.0/help/images/filters
%{_datadir}/gimp/2.0/help/images/filters/*.png
%{_datadir}/gimp/2.0/help/images/filters/examples
%{_datadir}/gimp/2.0/help/images/glossary
%{_datadir}/gimp/2.0/help/images/menus
%dir %{_datadir}/gimp/2.0/help/images/preferences
%{_datadir}/gimp/2.0/help/images/preferences/*.png
%lang(de) %{_datadir}/gimp/2.0/help/images/preferences/de
%lang(fr) %{_datadir}/gimp/2.0/help/images/preferences/fr
%{_datadir}/gimp/2.0/help/images/tool-options
%dir %{_datadir}/gimp/2.0/help/images/toolbox
%{_datadir}/gimp/2.0/help/images/toolbox/*.png
%dir %{_datadir}/gimp/2.0/help/images/using
%{_datadir}/gimp/2.0/help/images/using/*.png
%{_datadir}/gimp/2.0/help/en
%lang(de) %{_datadir}/gimp/2.0/help/de
%lang(fr) %{_datadir}/gimp/2.0/help/fr
%lang(sv) %{_datadir}/gimp/2.0/help/sv
%lang(zh_CN) %{_datadir}/gimp/2.0/help/zh_CN
%lang(fr) %{_datadir}/gimp/2.0/help/images/toolbox/fr
%lang(de) %{_datadir}/gimp/2.0/help/images/toolbox/de
%lang(de) %{_datadir}/gimp/2.0/help/images/filters/de
%lang(fr) %{_datadir}/gimp/2.0/help/images/filters/fr
%lang(de) %{_datadir}/gimp/2.0/help/images/dialogs/de
%lang(fr) %{_datadir}/gimp/2.0/help/images/dialogs/fr
