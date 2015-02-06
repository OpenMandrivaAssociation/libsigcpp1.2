%define pkgname libsigc++

%define api 1.2
%define major 5
%define libname %mklibname sigc++ %{api} %{major}
%define devname %mklibname sigc++ %{api} -d

Summary:	The Typesafe Signal Framework for C++
Name:		%{pkgname}%{api}
Version:	1.2.7
Release:	6
License:	LGPLv2.1+
Group:		System/Libraries
Url:		http://libsigc.sourceforge.net/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsigc++/%{pkgname}-%{version}.tar.bz2

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

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The Typesafe Signal Framework for C++
Group:		System/Libraries

%description -n %{libname}
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

%files -n %{libname}
%doc AUTHORS COPYING.LIB FEATURES NEWS README
%{_libdir}/libsigc-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development tools for the Typesafe Signal Framework for C++
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{_lib}sigc++1.2_5-devel < 1.2.7-5
Obsoletes:	%{_lib}sigc++1.2_5-devel < 1.2.7-5

%description -n %{devname}
This package contains the headers and static libraries of %{pkgname},
which are needed when developing or compiling applications which use
%{pkgname}.

%files -n %{devname}
%doc ChangeLog TODO IDEAS doc/[[:lower:]]*
%{_includedir}/*
%{_libdir}/libsigc-%{api}.so
%{_libdir}/pkgconfig/*
%{_libdir}/sigc++-%{api}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{pkgname}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

rm -rf doc/tests
mkdir doc/tests
cp tests/*.cc tests/README tests/Makefile doc/tests/

rm -rf doc/examples
mkdir doc/examples
cp examples/*.cc examples/Makefile doc/examples/

# remove files not bundled
rm -f doc/manual/README

%check
make check

