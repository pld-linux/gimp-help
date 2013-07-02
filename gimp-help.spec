# NOTE: python xml2po crashes with memory fault inside libxml2mod on two files from Greek (el) translation
Summary:	Help files for the GIMP
Summary(pl.UTF-8):	Pliki pomocy dla GIMP-a
Name:		gimp-help
Version:	2.8.0
Release:	1
License:	FDL
Group:		Documentation
Source0:	ftp://ftp.gimp.org/pub/gimp/help/%{name}-%{version}.tar.bz2
# Source0-md5:	d6e07a569fe4b3bb11aaf5630da2693b
Source1:	%{name}-lang-files.rb
Patch0:		%{name}-am.patch
Patch1:		%{name}-langs.patch
Patch2:		%{name}-xml2po.patch
URL:		http://wiki.gimp.org/gimp/GimpDocs
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1.6
BuildRequires:	docbook-dtd43-xml
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
%doc AUTHORS ChangeLog HACKING NEWS README TERMINOLOGY
