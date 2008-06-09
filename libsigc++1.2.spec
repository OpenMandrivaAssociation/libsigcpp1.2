%define version 1.2.7
%define release %mkrel 1

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -rf doc/tests
mkdir doc/tests
cp tests/*.cc tests/README tests/Makefile doc/tests/

rm -rf doc/examples
mkdir doc/examples
cp examples/*.cc examples/Makefile doc/examples/

# remove files not bundled
rm -f doc/manual/README

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING.LIB FEATURES NEWS README
%{_libdir}/lib*.so.%{major}*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc ChangeLog TODO IDEAS doc/[[:lower:]]*
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++-%{api_version}


