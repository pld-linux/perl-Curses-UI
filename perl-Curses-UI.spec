#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Curses
%define		pnam	UI
Summary:	Curses::UI - a UI framework based on the curses library
Summary(pl.UTF-8):   Curses::UI - interfejs użytkownika oparty na bibliotece curses
Name:		perl-Curses-UI
Version:	0.95
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f1ee30de6cbba611acca785fa668d8b8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Curses
BuildRequires:	perl-Term-ReadKey
%if %{with tests}
BuildRequires:	perl-Test-Pod
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Curses::UI Perl module is a UI framework based on the curses library.
It can be used for the development of curses based user interfaces.

%description -l pl.UTF-8
Moduł Perla Curses::UI stanowi szkielet oparty na bibliotece curses.
Może służyć do konstruowania interfejsów użytkownika w oparciu o
bibliotekę curses.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

# fails with:
# Unable to get Terminal Size. The TIOCGWINSZ ioctl didn't work. The
# COLUMNS and LINES environment variables didn't work. The resize
# program didn't work.
# Alternatively we could add BR: X11 (which sounds a bit crazy for me)
mv t/13notebook.t{,.blah}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# get rid of pod documentation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Curses/UI/Tutorial.pod

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
