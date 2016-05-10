%define major 0
%define libname %mklibname c++-gtk-utils %{major}
%define develname %mklibname c++-gtk-utils -d

Summary:	A library for programming GTK+ programs using C++
Name:		c++-gtk-utils
Version:	2.2.11
Release:	1
License:	GPLv2
Group:		System/Libraries
URL:		http://cxx-gtk-utils.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/cxx-gtk-utils/cxx-gtk-utils/2.2.6/%{name}-%{version}.tar.gz
Source100:      %{name}.rpmlintrc

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)

%description
c++-gtk-utils is a lightweight library containing a number of classes
and functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper such
as gtkmm or wxWidgets, or is concerned about exception safety or thread
safety of the wrapper and their documentation. It is parallel installable
for both GTK+2 and GTK+3.

%package -n	%{libname}
Summary:	A library for programming GTK+ programs using C++
Group:		System/Libraries

%description -n %{libname}
c++-gtk-utils is a lightweight library containing a number of classes
and functions for programming GTK+ programs using C++ in POSIX (unix-like)
environments, where the user does not want to use a full-on wrapper such
as gtkmm or wxWidgets, or is concerned about exception safety or thread
safety of the wrapper and their documentation. It is parallel installable
for both GTK+2 and GTK+3.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static

%make LIBS="-lpthread"

%install
%makeinstall_std

%files -n %{libname}
%doc ABOUT-NLS AUTHORS ChangeLog COPYING
%{_libdir}/libcxx-gtk-utils-3-2.2.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}-3-2.2/%{name}/*.h
%{_includedir}/%{name}-3-2.2/%{name}/*.tpp
%{_libdir}/pkgconfig/*.pc
%{_docdir}/%{name}/2.2/html/*
%{_docdir}/%{name}/2.2/README
%{_docdir}/%{name}/2.2/NEWS
%{_docdir}/%{name}/2.2/BUGS
%{_docdir}/%{name}/2.2/COPYING
%{_docdir}/%{name}/2.2/PORTING*
%{_libdir}/libcxx-gtk-utils-3-2.2.so

