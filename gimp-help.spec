# NOTE: xsltproc consumes lots of memory
Summary:	Help files for the GIMP
Summary(pl.UTF-8):	Pliki pomocy dla GIMP-a
Name:		gimp-help
Version:	2.10.34
Release:	1
License:	FDL
Group:		Documentation
Source0:	https://download.gimp.org/pub/gimp/help/%{name}-%{version}.tar.bz2
# Source0-md5:	5e393d61c802e73ffe6c550759ed0853
URL:		https://docs.gimp.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.10
BuildRequires:	dblatex
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	librsvg
BuildRequires:	libxml2-progs >= 2
BuildRequires:	libxslt-progs
BuildRequires:	python3 >= 1:3.6.0
BuildRequires:	python3-libxml2
BuildRequires:	ruby
BuildRequires:	sed >= 4.0
BuildRequires:	xhtml-dtd10-xml
Requires:	gimp >= 2.8.0
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
%{__aclocal}
%{__autoconf}
%{__automake}
# see autogen.sh
%{__sed} -i -e 's/# HIDE FROM AUTOMAKE #//' -e '/^all\(-local\)\?:/i\
\
\
' Makefile.in
%configure \
	--host=%{_host} \
	--build=%{_host} \
	--without-gimp
%{__make} -j1 all

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TERMINOLOGY
%dir %{_datadir}/gimp/2.0/help
%lang(ca) %{_datadir}/gimp/2.0/help/ca
%lang(cs) %{_datadir}/gimp/2.0/help/cs
%lang(da) %{_datadir}/gimp/2.0/help/da
%lang(de) %{_datadir}/gimp/2.0/help/de
%lang(el) %{_datadir}/gimp/2.0/help/el
# always include as fallback
%{_datadir}/gimp/2.0/help/en
%lang(en_GB) %{_datadir}/gimp/2.0/help/en_GB
%lang(es) %{_datadir}/gimp/2.0/help/es
%lang(fa) %{_datadir}/gimp/2.0/help/fa
%lang(fi) %{_datadir}/gimp/2.0/help/fi
%lang(fr) %{_datadir}/gimp/2.0/help/fr
%lang(hr) %{_datadir}/gimp/2.0/help/hr
%lang(hu) %{_datadir}/gimp/2.0/help/hu
%lang(it) %{_datadir}/gimp/2.0/help/it
%lang(ja) %{_datadir}/gimp/2.0/help/ja
%lang(ko) %{_datadir}/gimp/2.0/help/ko
%lang(lt) %{_datadir}/gimp/2.0/help/lt
%lang(nl) %{_datadir}/gimp/2.0/help/nl
%lang(nn) %{_datadir}/gimp/2.0/help/nn
%lang(pt) %{_datadir}/gimp/2.0/help/pt
%lang(pt_BR) %{_datadir}/gimp/2.0/help/pt_BR
%lang(ro) %{_datadir}/gimp/2.0/help/ro
%lang(ru) %{_datadir}/gimp/2.0/help/ru
%lang(sl) %{_datadir}/gimp/2.0/help/sl
%lang(sv) %{_datadir}/gimp/2.0/help/sv
%lang(uk) %{_datadir}/gimp/2.0/help/uk
%lang(zh_CN) %{_datadir}/gimp/2.0/help/zh_CN

%dir %{_datadir}/gimp/2.0/help/pdf
%lang(ca) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-ca.pdf
%lang(cs) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-cs.pdf
%lang(da) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-da.pdf
%lang(de) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-de.pdf
%lang(el) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-el.pdf
%{_datadir}/gimp/2.0/help/pdf/gimp-keys-en.pdf
%lang(en_GB) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-en_GB.pdf
%lang(es) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-es.pdf
%lang(fa) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-fa.pdf
%lang(fi) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-fi.pdf
%lang(fr) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-fr.pdf
%lang(hr) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-hr.pdf
%lang(hu) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-hu.pdf
%lang(it) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-it.pdf
%lang(ja) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-ja.pdf
%lang(ko) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-ko.pdf
%lang(lt) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-lt.pdf
%lang(nl) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-nl.pdf
%lang(nn) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-nn.pdf
%lang(pl) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-pl.pdf
%lang(pt) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-pt.pdf
%lang(pt_BR) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-pt_BR.pdf
%lang(ro) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-ro.pdf
%lang(ru) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-ru.pdf
%lang(sl) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-sl.pdf
%lang(sv) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-sv.pdf
%lang(uk) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-uk.pdf
%lang(zh_CN) %{_datadir}/gimp/2.0/help/pdf/gimp-keys-zh_CN.pdf
