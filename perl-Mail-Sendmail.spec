%define	upstream_name 	 Mail-Sendmail
%define	upstream_version 0.79_16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Simple platform-independent mailer
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/M/MI/MIVKOVIC/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Mail-Sendmail is a Perl module for sending mail through a sendmail SMTP
server.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc Changes README Todo
%{_mandir}/*/*
%{perl_vendorlib}/Mail


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.791_600-4mdv2012.0
+ Revision: 765442
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.791_600-3
+ Revision: 763954
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.791_600-2
+ Revision: 667255
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.791_600-1mdv2011.0
+ Revision: 403844
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.79.16-5mdv2009.1
+ Revision: 351897
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.79.16-4mdv2009.0
+ Revision: 223811
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.79.16-3mdv2008.1
+ Revision: 180473
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 0.79.16-2mdv2008.0
+ Revision: 64787
- rebuild


* Mon Feb 12 2007 Stew Benedict <sbenedict@mandriva.com> 0.79.16-1mdv2007.0
+ Revision: 120105
- 0.79.16

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Mail-Sendmail

* Sat Jan 21 2006 Michael Scherer <misc@mandriva.org> 0.79-4mdk
- Rebuild to fix 20764 
- use mkrel
- fix rpmlint warning about distribution, and apply perl policy

