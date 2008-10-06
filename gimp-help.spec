Summary:	Help files for the GIMP
Summary(pl.UTF-8):	Pliki pomocy dla GIMP-a
Name:		gimp-help
Version:	2.4.2
Release:	1
License:	FDL
Group:		Documentation
Source0:	ftp://ftp.gimp.org/pub/gimp/help/%{name}-%{version}.tar.bz2
# Source0-md5:	497e1212cbd1499d151b85dabaa3875c
Source1:	%{name}-lang-files.rb
URL:		http://wiki.gimp.org/gimp/GimpDocs
BuildRequires:	docbook-dtd43-xml
BuildRequires:	ruby
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

%{__ruby} %{SOURCE1} -p %{_datadir}/gimp/2.0 -p %{_defaultdocdir} > %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README TERMINOLOGY
