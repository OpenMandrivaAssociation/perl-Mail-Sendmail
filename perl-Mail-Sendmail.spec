%define	modname	Mail-Sendmail
%define	modver	0.83

Summary:	Simple platform-independent mailer
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://github.com/neilb/Mail-Sendmail
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Mail-Sendmail-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
Mail-Sendmail is a Perl module for sending mail through a sendmail SMTP
server.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README Todo
%{perl_vendorlib}/Mail
%{_mandir}/man3/*

