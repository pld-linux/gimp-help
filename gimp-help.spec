Summary:	Help files for the GIMP
Summary(pl):	Pliki pomocy dla GIMP
Name:		gimp-help
Version:	0.7
Release:	1
License:	FDL
Group:		Documentation
Source0:	ftp://ftp.gimp.org/pub/gimp/help/testing/%{name}-2-%{version}.tar.gz
# Source0-md5:	aee429af1f99e3d1f9e23d5d4a6d3622
URL:		http://wiki.gimp.org/gimp/GimpDocs
Requires:	gimp >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIMP-Help is a help system designed for use with the internal GIMP 2
help browser, external web browser and HTML renderers, and human
eyeballs.

%description -l pl
GIMP-Help jest systemem pomocy zaprojektowanym do użytku z wewnętrzną
przeglądarką GIMP-a 2, zewnętrznymi przeglądarkami stron WWW, oraz
ludzkimi gałkami ocznymi.

%prep
%setup -q -n %{name}-2-%{version}

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
%lang(cs) %{_datadir}/gimp/2.0/help/cs
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
%lang(fr) %{_datadir}/gimp/2.0/help/images/using/fr
