%define		_class		Contact
%define		_subclass	Vcard_Parse
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.32.0
Release:	6
Summary:	Parse vCard 2.1 and 3.0 files
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Contact_Vcard_Parse/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Allows you to parse vCard files and text blocks, and get back an array
of the elements of each vCard in the file or text.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{upstream_name}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.32.0-5mdv2012.0
+ Revision: 741831
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.32.0-4
+ Revision: 679270
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.32.0-3mdv2011.0
+ Revision: 613619
- the mass rebuild of 2010.1 packages

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.32.0-2mdv2010.1
+ Revision: 478297
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.32.0-1mdv2010.0
+ Revision: 450265
- new version
- use pear installer
- use fedora %%post/%%postun

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.31.0-8mdv2010.0
+ Revision: 440950
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-7mdv2009.1
+ Revision: 321934
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-6mdv2009.0
+ Revision: 236812
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-5mdv2007.0
+ Revision: 81418
- Import php-pear-Contact_Vcard_Parse

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.31.0-1mdk
- 1.31.0

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.30-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.30-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.30-1mdk
- initial Mandriva package (PLD import)

