#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Curses
%define	pnam	UI
Summary:	Curses::UI - a UI framework based on the curses library
Summary(pl):	Curses::UI - interfejs u¿ytkownika oparty na bibliotece curses
Name:		perl-Curses-UI
Version:	0.73
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	perl-Curses
BuildRequires:	perl-Term-ReadKey
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Curses::UI Perl module is a UI framework based on the curses library.
It can be used for the development of curses based user interfaces.

%description -l pl
Modu³ Perla Curses::UI stanowi szkielet oparty na bibliotece curses.
Mo¿e s³u¿yæ do konstruowania interfejsów u¿ytkownika w oparciu o
bibliotekê curses.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Curses/UI.pm
%{perl_vendorlib}/Curses/UI
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
