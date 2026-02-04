# NOTE: xsltproc consumes lots of memory
Summary:	Help files for the GIMP
Summary(pl.UTF-8):	Pliki pomocy dla GIMP-a
Name:		gimp-help
Version:	3.0.2
Release:	1
License:	FDL
Group:		Documentation
Source0:	https://download.gimp.org/pub/gimp/help/%{name}-%{version}.tar.bz2
# Source0-md5:	a9afbeea7d55bb8655f91e2b0ca1d7a8
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
Requires:	gimp >= 3.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GIMP-Help is a help system designed for use with the internal GIMP 3
help browser, external web browser and HTML renderers, and human
eyeballs.

%description -l pl.UTF-8
GIMP-Help jest systemem pomocy zaprojektowanym do użytku z wewnętrzną
przeglądarką GIMP-a 3, zewnętrznymi przeglądarkami stron WWW, oraz
ludzkimi gałkami ocznymi.

%package bg
Summary:	GIMP help in Bulgarian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku bułgarskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description bg
This package provides GIMP help files in Bulgarian language.

%description bg -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku bułgarskim.

%package ca
Summary:	GIMP help in Catalan language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku katalońskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description ca
This package provides GIMP help files in Catalan language.

%description ca -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku katalońskim.

%package cs
Summary:	GIMP help in Czech language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku czeskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description cs
This package provides GIMP help files in Czech language.

%description cs -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku czeskim.

%package da
Summary:	GIMP help in Danish language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku duńskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description da
This package provides GIMP help files in Danish language.

%description da -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku duńskim.

%package de
Summary:	GIMP help in German language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku niemieckim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description de
This package provides GIMP help files in German language.

%description de -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku niemieckim.

%package el
Summary:	GIMP help in Greek language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku greckim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description el
This package provides GIMP help files in Greek language.

%description el -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku greckim.

%package en_GB
Summary:	GIMP help in British English language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku angielskim brytyjskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description en_GB
This package provides GIMP help files in British English language.

%description en_GB -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku angielskim
brytyjskim.

%package eo
Summary:	GIMP help in Esperanto language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku Esperanto
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description eo
This package provides GIMP help files in Esperanto language.

%description eo -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku Esperanto.

%package es
Summary:	GIMP help in Spanish language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku hiszpańskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description es
This package provides GIMP help files in Spanish language.

%description es -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku hiszpańskim.

%package fa
Summary:	GIMP help in Persian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku perskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description fa
This package provides GIMP help files in Persian language.

%description fa -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku perskim.

%package fi
Summary:	GIMP help in Finnish language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku fińskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description fi
This package provides GIMP help files in Finnish language.

%description fi -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku fińskim.

%package fr
Summary:	GIMP help in French language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku francuskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description fr
This package provides GIMP help files in French language.

%description fr -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku francuskim.

%package hr
Summary:	GIMP help in Croatian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku horwackim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description hr
This package provides GIMP help files in Croatian language.

%description hr -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku horwackim.

%package hu
Summary:	GIMP help in Hungarian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku węgierskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description hu
This package provides GIMP help files in Hungarian language.

%description hu -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku węgierskim.

%package it
Summary:	GIMP help in Italian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku włoskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description it
This package provides GIMP help files in Italian language.

%description it -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku włoskim.

%package ja
Summary:	GIMP help in Japanese language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku japońskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description ja
This package provides GIMP help files in Japanese language.

%description ja -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku japońskim.

%package ko
Summary:	GIMP help in Korean language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku koreańskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description ko
This package provides GIMP help files in Korean language.

%description ko -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku koreańskim.

%package lt
Summary:	GIMP help in Lithuanian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku litewskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description lt
This package provides GIMP help files in Lithuanian language.

%description lt -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku litewskim.

%package nl
Summary:	GIMP help in Dutch language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku niderlandzkim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description nl
This package provides GIMP help files in Dutch language.

%description nl -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku niderlandzkim.

%package nn
Summary:	GIMP help in Norwegian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku norweskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description nn
This package provides GIMP help files in Norwegian language.

%description nn -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku norweskim.

%package pl
Summary:	GIMP help in Polish language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku polskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description pl
This package provides GIMP help files in Polish language.

%description pl -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku polskim.

%package pt
Summary:	GIMP help in Portuguese language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku portugalskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description pt
This package provides GIMP help files in Portuguese language.

%description pt -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku portugalskim.

%package pt_BR
Summary:	GIMP help in Brazilian Portuguese language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku portugalskim brazylijskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description pt_BR
This package provides GIMP help files in Brazilian Portuguese
language.

%description pt_BR -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku portugalskim
brazylijskim.

%package ro
Summary:	GIMP help in Romanian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku rumuńskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description ro
This package provides GIMP help files in Romanian language.

%description ro -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku rumuńskim.

%package ru
Summary:	GIMP help in Russian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku rosyjskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description ru
This package provides GIMP help files in Russian language.

%description ru -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku rosyjskim.

%package sk
Summary:	GIMP help in Slovak language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku słowackim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sk
This package provides GIMP help files in Slovak language.

%description sk -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku słowackim.

%package sl
Summary:	GIMP help in Slovenian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku słoweńskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sl
This package provides GIMP help files in Slovenian language.

%description sl -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku słoweńskim.

%package sv
Summary:	GIMP help in Swedish language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku szwedzkim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description sv
This package provides GIMP help files in Swedish language.

%description sv -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku szwedzkim.

%package tr
Summary:	GIMP help in Turkish language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku tureckim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description tr
This package provides GIMP help files in Turkish language.

%description tr -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku tureckim.

%package uk
Summary:	GIMP help in Ukrainian language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku ukraińskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description uk
This package provides GIMP help files in Ukrainian language.

%description uk -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku ukraińskim.

%package zh_CN
Summary:	GIMP help in Chinese language
Summary(pl.UTF-8):	Podręcznik GIMP-a w języku chińskim
Group:		I18n
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description zh_CN
This package provides GIMP help files in Chinese language.

%description zh_CN -l pl.UTF-8
Ten pakiet dostarcza pliki podręcznika GIMP-a w języku chińskim.

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
%if "%{_host_cpu}" != "x32"
	--host=%{_host} \
	--build=%{_host} \
%endif
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
%doc AUTHORS ChangeLog MAINTAINERS NEWS TERMINOLOGY
%dir %{_datadir}/gimp/3.0/help
%dir %{_datadir}/gimp/3.0/help/pdf
# always include as fallback
%{_datadir}/gimp/3.0/help/en
%{_datadir}/gimp/3.0/help/pdf/gimp-keys-en.pdf

%files bg
%defattr(644,root,root,755)
%lang(bg) %{_datadir}/gimp/3.0/help/bg
%lang(bg) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-bg.pdf

%files ca
%defattr(644,root,root,755)
%lang(ca) %{_datadir}/gimp/3.0/help/ca
%lang(ca) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-ca.pdf

%files cs
%defattr(644,root,root,755)
%lang(cs) %{_datadir}/gimp/3.0/help/cs
%lang(cs) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-cs.pdf

%files da
%defattr(644,root,root,755)
%lang(da) %{_datadir}/gimp/3.0/help/da
%lang(da) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-da.pdf

%files de
%defattr(644,root,root,755)
%lang(de) %{_datadir}/gimp/3.0/help/de
%lang(de) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-de.pdf

%files el
%defattr(644,root,root,755)
%lang(el) %{_datadir}/gimp/3.0/help/el
%lang(el) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-el.pdf

%files en_GB
%defattr(644,root,root,755)
%lang(en_GB) %{_datadir}/gimp/3.0/help/en_GB
%lang(en_GB) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-en_GB.pdf

%files eo
%defattr(644,root,root,755)
%lang(eo) %{_datadir}/gimp/3.0/help/eo
%lang(eo) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-eo.pdf

%files es
%defattr(644,root,root,755)
%lang(es) %{_datadir}/gimp/3.0/help/es
%lang(es) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-es.pdf

%files fa
%defattr(644,root,root,755)
%lang(fa) %{_datadir}/gimp/3.0/help/fa
%lang(fa) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-fa.pdf

%files fi
%defattr(644,root,root,755)
%lang(fi) %{_datadir}/gimp/3.0/help/fi
%lang(fi) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-fi.pdf

%files fr
%defattr(644,root,root,755)
%lang(fr) %{_datadir}/gimp/3.0/help/fr
%lang(fr) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-fr.pdf

%files hr
%defattr(644,root,root,755)
%lang(hr) %{_datadir}/gimp/3.0/help/hr
%lang(hr) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-hr.pdf

%files hu
%defattr(644,root,root,755)
%lang(hu) %{_datadir}/gimp/3.0/help/hu
%lang(hu) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-hu.pdf

%files it
%defattr(644,root,root,755)
%lang(it) %{_datadir}/gimp/3.0/help/it
%lang(it) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-it.pdf

%files ja
%defattr(644,root,root,755)
%lang(ja) %{_datadir}/gimp/3.0/help/ja
%lang(ja) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-ja.pdf

%files ko
%defattr(644,root,root,755)
%lang(ko) %{_datadir}/gimp/3.0/help/ko
%lang(ko) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-ko.pdf

%files lt
%defattr(644,root,root,755)
%lang(lt) %{_datadir}/gimp/3.0/help/lt
%lang(lt) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-lt.pdf

%files nl
%defattr(644,root,root,755)
%lang(nl) %{_datadir}/gimp/3.0/help/nl
%lang(nl) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-nl.pdf

%files nn
%defattr(644,root,root,755)
%lang(nn) %{_datadir}/gimp/3.0/help/nn
%lang(nn) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-nn.pdf

%files pl
%defattr(644,root,root,755)
%lang(pl) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-pl.pdf
%lang(pl) %{_datadir}/gimp/3.0/help/pl

%files pt
%defattr(644,root,root,755)
%lang(pt) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-pt.pdf
%lang(pt) %{_datadir}/gimp/3.0/help/pt

%files pt_BR
%defattr(644,root,root,755)
%lang(pt_BR) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-pt_BR.pdf
%lang(pt_BR) %{_datadir}/gimp/3.0/help/pt_BR

%files ro
%defattr(644,root,root,755)
%lang(ro) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-ro.pdf
%lang(ro) %{_datadir}/gimp/3.0/help/ro

%files ru
%defattr(644,root,root,755)
%lang(ru) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-ru.pdf
%lang(ru) %{_datadir}/gimp/3.0/help/ru

%files sk
%defattr(644,root,root,755)
%lang(sk) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-sk.pdf
%lang(sk) %{_datadir}/gimp/3.0/help/sk

%files sl
%defattr(644,root,root,755)
%lang(sl) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-sl.pdf
%lang(sl) %{_datadir}/gimp/3.0/help/sl

%files sv
%defattr(644,root,root,755)
%lang(sv) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-sv.pdf
%lang(sv) %{_datadir}/gimp/3.0/help/sv

%files tr
%defattr(644,root,root,755)
%lang(tr) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-tr.pdf
%lang(tr) %{_datadir}/gimp/3.0/help/tr

%files uk
%defattr(644,root,root,755)
%lang(uk) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-uk.pdf
%lang(uk) %{_datadir}/gimp/3.0/help/uk

%files zh_CN
%defattr(644,root,root,755)
%lang(zh_CN) %{_datadir}/gimp/3.0/help/pdf/gimp-keys-zh_CN.pdf
%lang(zh_CN) %{_datadir}/gimp/3.0/help/zh_CN
