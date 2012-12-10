%define version 1.2.7
%define release 4

%define pkgname libsigc++

%define api_version 1.2
%define major 5
%define libname %mklibname sigc++ %api_version %major

Name:		%{pkgname}%{api_version}
Summary:	The Typesafe Signal Framework for C++
Version:	%{version}
Release:	%{release}
License:	LGPL
Source:		http://ftp.gnome.org/pub/GNOME/sources/libsigc++/%{pkgname}-%{version}.tar.bz2
Url:		http://libsigc.sourceforge.net/
Group:		System/Libraries
BuildRequires:	autoconf2.5

%description
Callback system for use in widget libraries, abstract interfaces, and
general programming.

This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally part
of the Gtk-- widget set, %{pkgname} is now a separate library to provide for
more general use. It is the most complete library of its kind with the
ablity to connect an abstract callback to a class method, function, or
function object. It contains adaptor classes for connection of dissimilar
callbacks and has an ease of use unmatched by other C++ callback
libraries.

Package gtkmm, which is a c++ binding to the famous gtk+ library, uses
%{pkgname}.


%package -n	%{libname}
Summary:	The Typesafe Signal Framework for C++
Group:		System/Libraries
Provides:	%{pkgname}%{api_version} = %{version}-%{release}

%description -n	%{libname}
Callback system for use in widget libraries, abstract interfaces, and
general programming.

This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally part
of the Gtk-- widget set, %{pkgname} is now a separate library to provide for
more general use. It is the most complete library of its kind with the
ablity to connect an abstract callback to a class method, function, or
function object. It contains adaptor classes for connection of dissimilar
callbacks and has an ease of use unmatched by other C++ callback
libraries.

Package gtkmm, which is a c++ binding to the famous gtk+ library, uses
%{pkgname}.


%package -n	%{libname}-devel
Summary:	Development tools for the Typesafe Signal Framework for C++ 
Group:		Development/C++
Provides:	libsigc++1.2-examples
Obsoletes:	libsigc++1.2-examples
Provides:	%{pkgname}%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
This package contains the headers and static libraries of %{pkgname},
which are needed when developing or compiling applications which use
%{pkgname}.


%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x
%make

%check
make check

%makeinstall_std

rm -rf doc/tests
mkdir doc/tests
cp tests/*.cc tests/README tests/Makefile doc/tests/

rm -rf doc/examples
mkdir doc/examples
cp examples/*.cc examples/Makefile doc/examples/

# remove files not bundled
rm -f doc/manual/README
find $RPM_BUILD_ROOT/%{_libdir} -name '*.la' -exec rm {} \;

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files -n %{libname}
%doc AUTHORS COPYING.LIB FEATURES NEWS README
%{_libdir}/lib*.so.%{major}*

%files -n %{libname}-devel
%doc ChangeLog TODO IDEAS doc/[[:lower:]]*
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++-%{api_version}




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-4mdv2011.0
+ Revision: 620224
- the mass rebuild of 2010.0 packages

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 1.2.7-3mdv2009.0
+ Revision: 250520
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.7-1mdv2008.1
+ Revision: 140928
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Dec 21 2006 GГ¶tz Waschk <waschk@mandriva.org> 1.2.7-1mdv2007.0
+ Revision: 100980
- Import libsigc++1.2

* Thu Dec 21 2006 Gцtz Waschk <waschk@mandriva.org> 1.2.7-1mdv2007.1
- add check section
- spec fix
- mkrel

* Fri Apr 22 2005 GГ¶tz Waschk <waschk@mandriva.org> 1.2.7-1mdk
- New release 1.2.7
- drop patches
- source URL

* Tue Sep 21 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2.5-11mdk
- fix broken built-in libtool 1.5

* Sat Jun 05 2004 <lmontel@n2.mandrakesoft.com> 1.2.5-10mdk
- Rebuild

* Sat May 22 2004 Abel Cheung <deaddog@deaddog.org> 1.2.5-9mdk
- I will convert the encoding of this spec file everytime.
- Revert last change, not needed
- Drop patch0 and __libtoolize, new libtool is used

* Sat May 22 2004 Per Г�yvind Karlsen <peroyvind@linux-mandrake.com> 1.2.5-8mdk
- fix buildrequires

* Fri May 14 2004 Abel Cheung <deaddog@deaddog.org> 1.2.5-7mdk
- (gb) P0: fix built-in libtool
- (gb) P1: lib64 fixes

* Wed Apr 28 2004 Abel Cheung <deaddog@deaddog.org> 1.2.5-6mdk
- Rebuild

