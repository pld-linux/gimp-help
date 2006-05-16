Summary:	Help files for the GIMP
Summary(pl):	Pliki pomocy dla GIMP
Name:		gimp-help
Version:	0.10
Release:	1
License:	FDL
Group:		Documentation
Source0:	ftp://ftp.gimp.org/pub/gimp/help/%{name}-2-%{version}.tar.gz
# Source0-md5:	22a1e10c314c5547fe8721c4f6f0b30a
URL:		http://wiki.gimp.org/gimp/GimpDocs
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xhtml-dtd10-xml
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
%doc AUTHORS ChangeLog HACKING NEWS README TERMINOLOGY TODO
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
%lang(zh_CN) %{_datadir}/gimp/2.0/help/images/preferences/zh_CN
%{_datadir}/gimp/2.0/help/images/tool-options
%dir %{_datadir}/gimp/2.0/help/images/toolbox
%{_datadir}/gimp/2.0/help/images/toolbox/*.png
%dir %{_datadir}/gimp/2.0/help/images/using
%{_datadir}/gimp/2.0/help/images/using/*.png
%{_datadir}/gimp/2.0/help/images/math
%{_datadir}/gimp/2.0/help/en
%lang(cs) %{_datadir}/gimp/2.0/help/cs
%lang(de) %{_datadir}/gimp/2.0/help/de
%lang(fr) %{_datadir}/gimp/2.0/help/fr
%lang(hr) %{_datadir}/gimp/2.0/help/hr
%lang(it) %{_datadir}/gimp/2.0/help/it
%lang(nl) %{_datadir}/gimp/2.0/help/nl
%lang(sv) %{_datadir}/gimp/2.0/help/sv
%lang(zh_CN) %{_datadir}/gimp/2.0/help/zh_CN
%lang(cs) %{_datadir}/gimp/2.0/help/images/toolbox/cs
%lang(de) %{_datadir}/gimp/2.0/help/images/toolbox/de
%lang(fr) %{_datadir}/gimp/2.0/help/images/toolbox/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/toolbox/it
%lang(zh_CN) %{_datadir}/gimp/2.0/help/images/toolbox/zh_CN
%lang(cs) %{_datadir}/gimp/2.0/help/images/filters/cs
%lang(de) %{_datadir}/gimp/2.0/help/images/filters/de
%lang(fr) %{_datadir}/gimp/2.0/help/images/filters/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/filters/it
%lang(zh_CN) %{_datadir}/gimp/2.0/help/images/filters/zh_CN
%lang(cs) %{_datadir}/gimp/2.0/help/images/dialogs/cs
%lang(de) %{_datadir}/gimp/2.0/help/images/dialogs/de
%lang(fr) %{_datadir}/gimp/2.0/help/images/dialogs/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/dialogs/it
%lang(zh_CN) %{_datadir}/gimp/2.0/help/images/dialogs/zh_CN
%lang(nl) %{_datadir}/gimp/2.0/help/images/preferences/nl
%lang(cs) %{_datadir}/gimp/2.0/help/images/using/cs
%lang(de) %{_datadir}/gimp/2.0/help/images/using/de
%lang(fr) %{_datadir}/gimp/2.0/help/images/using/fr
%lang(hr) %{_datadir}/gimp/2.0/help/images/using/hr
%lang(nl) %{_datadir}/gimp/2.0/help/images/using/nl
%lang(zh_CN) %{_datadir}/gimp/2.0/help/images/using/zh_CN
