%define	name		perl-Mail-Sendmail
%define	realname 	Mail-Sendmail
%define	majorver	0.79
%define minorver	16
%define	release 	%mkrel 5

Name:		%{name}
Summary:	Simple platform-independent mailer
Version:	%{majorver}.%{minorver}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source:		http://www.cpan.org/authors/id/M/MI/MIVKOVIC/%{realname}-%{majorver}_%{minorver}.tar.bz2
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch


%description
Mail-Sendmail is a Perl module for sending mail through a sendmail SMTP
server.


%prep
%setup -q -n %{realname}-%{majorver}_%{minorver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README Todo
%{_mandir}/*/*
%{perl_vendorlib}/Mail


