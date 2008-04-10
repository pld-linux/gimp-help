Summary:	Help files for the GIMP
Summary(pl.UTF-8):	Pliki pomocy dla GIMP-a
Name:		gimp-help
Version:	2.4.1
Release:	1
License:	FDL
Group:		Documentation
Source0:	ftp://ftp.gimp.org/pub/gimp/help/%{name}-%{version}.tar.bz2
# Source0-md5:	da505d7532b6e14713e04b6e79a11379
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

%description -l pl.UTF-8
GIMP-Help jest systemem pomocy zaprojektowanym do użytku z wewnętrzną
przeglądarką GIMP-a 2, zewnętrznymi przeglądarkami stron WWW, oraz
ludzkimi gałkami ocznymi.

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

mv -f $RPM_BUILD_ROOT%{_datadir}/gimp/2.0/help/images/filters/{no,nb}
mv -f $RPM_BUILD_ROOT%{_datadir}/gimp/2.0/help/images/preferences/{no,nb}
mv -f $RPM_BUILD_ROOT%{_datadir}/gimp/2.0/help/images/tutorials/{no,nb}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TERMINOLOGY
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
%dir %{_datadir}/gimp/2.0/help/images/tutorials
%{_datadir}/gimp/2.0/help/images/tutorials/*.jpg
%{_datadir}/gimp/2.0/help/images/tutorials/*.png
%dir %{_datadir}/gimp/2.0/help/images/using
%{_datadir}/gimp/2.0/help/images/using/*.jpg
%{_datadir}/gimp/2.0/help/images/using/*.png
%{_datadir}/gimp/2.0/help/images/math
%{_datadir}/gimp/2.0/help/en
%lang(de) %{_datadir}/gimp/2.0/help/de
%lang(es) %{_datadir}/gimp/2.0/help/es
%lang(fr) %{_datadir}/gimp/2.0/help/fr
%lang(it) %{_datadir}/gimp/2.0/help/it
%lang(ko) %{_datadir}/gimp/2.0/help/ko
%lang(nb) %{_datadir}/gimp/2.0/help/no
%lang(nl) %{_datadir}/gimp/2.0/help/nl
%lang(pl) %{_datadir}/gimp/2.0/help/pl
%lang(ru) %{_datadir}/gimp/2.0/help/ru
%lang(sv) %{_datadir}/gimp/2.0/help/sv
%lang(de) %{_datadir}/gimp/2.0/help/images/toolbox/de
%lang(es) %{_datadir}/gimp/2.0/help/images/toolbox/es
%lang(fr) %{_datadir}/gimp/2.0/help/images/toolbox/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/toolbox/it
%lang(ko) %{_datadir}/gimp/2.0/help/images/toolbox/ko
%lang(nl) %{_datadir}/gimp/2.0/help/images/toolbox/nl
%lang(no) %{_datadir}/gimp/2.0/help/images/toolbox/no
%lang(de) %{_datadir}/gimp/2.0/help/images/filters/de
%lang(es) %{_datadir}/gimp/2.0/help/images/filters/es
%lang(fr) %{_datadir}/gimp/2.0/help/images/filters/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/filters/it
%lang(nb) %{_datadir}/gimp/2.0/help/images/filters/nb
%lang(de) %{_datadir}/gimp/2.0/help/images/dialogs/de
%lang(es) %{_datadir}/gimp/2.0/help/images/dialogs/es
%lang(fr) %{_datadir}/gimp/2.0/help/images/dialogs/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/dialogs/it
%lang(ko) %{_datadir}/gimp/2.0/help/images/dialogs/ko
%lang(nb) %{_datadir}/gimp/2.0/help/images/dialogs/no
%lang(nl) %{_datadir}/gimp/2.0/help/images/dialogs/nl
%lang(ru) %{_datadir}/gimp/2.0/help/images/dialogs/ru
%lang(es) %{_datadir}/gimp/2.0/help/images/preferences/es
%lang(it) %{_datadir}/gimp/2.0/help/images/preferences/it
%lang(nb) %{_datadir}/gimp/2.0/help/images/preferences/nb
%lang(nl) %{_datadir}/gimp/2.0/help/images/preferences/nl
%lang(ru) %{_datadir}/gimp/2.0/help/images/preferences/ru
%lang(fr) %{_datadir}/gimp/2.0/help/images/tutorials/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/tutorials/it
%lang(nb) %{_datadir}/gimp/2.0/help/images/tutorials/nb
%lang(de) %{_datadir}/gimp/2.0/help/images/using/de
%lang(es) %{_datadir}/gimp/2.0/help/images/using/es
%lang(fr) %{_datadir}/gimp/2.0/help/images/using/fr
%lang(it) %{_datadir}/gimp/2.0/help/images/using/it
%lang(ko) %{_datadir}/gimp/2.0/help/images/using/ko
%lang(nb) %{_datadir}/gimp/2.0/help/images/using/no
%lang(nl) %{_datadir}/gimp/2.0/help/images/using/nl
%lang(ru) %{_datadir}/gimp/2.0/help/images/using/ru
