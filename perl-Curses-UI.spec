#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Curses
%define	pnam	UI
Summary:	Curses::UI perl module
Summary(pl):	Modu³ perla Curses::UI
Name:		perl-%{pdir}-%{pnam}
Version:	0.71
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-Curses
BuildRequires:	perl-Term-ReadKey
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A UI framework based on the curses library.

%description -l pl
Modu³ ten udostêpnia UI bazuj±ce na bibliotece Curses.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
%{perl_sitelib}/Curses/UI.pm
%{perl_sitelib}/Curses/UI
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
