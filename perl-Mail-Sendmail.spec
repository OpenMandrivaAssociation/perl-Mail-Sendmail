%define	modname	Mail-Sendmail
%define	modver	0.80

Summary:	Simple platform-independent mailer
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/authors/id/N/NE/NEILB/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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

