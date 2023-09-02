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
Source1:	%{name}-lang-files.rb
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

%{__ruby} %{SOURCE1} -p %{_datadir}/gimp/2.0 -p %{_defaultdocdir} -s %{_defaultdocdir}/\.+ > %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TERMINOLOGY
