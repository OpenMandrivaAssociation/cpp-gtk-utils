%define major 0
%define minor 2
%define libname %mklibname c++-gtk-utils %{major}
%define develname %mklibname c++-gtk-utils -d

Summary:	GTK+-based ISO image editor
Name:		c++-gtk-utils
Version:	2.0.4
Release:	1
Source0:	http://downloads.sourceforge.net/project/cxx-gtk-utils/cxx-gtk-utils/2.0.4/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		System/Libraries
URL:		http://cxx-gtk-utils.sourceforge.net
BuildRequires:	gtk+3.0-devel	

%description
c++-gtk-utils is a lightweight library containing 
a number of classes and functions for programming 
GTK+ programs using C++ in POSIX (unix-like) environments, 
where the user does not want to use a full-on wrapper such
as gtkmm or wxWidgets, or is concerned about exception safety 
or thread safety of the wrapper and their documentation.
It is parallel installable for both GTK+2 and GTK+3. 



%package -n	%{libname}
Summary:	A library containing a number of classes and functions for programming GTK+ programs using C++
Group:		System/Libraries
Provides:	%{name} = %{version}

%description -n %{libname}
c++-gtk-utils is a lightweight library containing
a number of classes and functions for programming
GTK+ programs using C++ in POSIX (unix-like) environments,
where the user does not want to use a full-on wrapper such
as gtkmm or wxWidgets, or is concerned about exception safety
or thread safety of the wrapper and their documentation.
It is parallel installable for both GTK+2 and GTK+3.


%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name}


%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} --exec-prefix=%{_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir}  --mandir=%{_mandir}


%make

%install
%makeinstall_std
rm -rf %{buildroot}/%{_libdir}/libcxx-gtk-utils-3-2.0.a


%files -n %{libname}
%{_libdir}/libcxx-gtk-utils-3-2.0.so.0.0.%{minor}

%files -n %{develname}
%{_includedir}/%{name}-3-2.0/%{name}/*.h
%{_includedir}/%{name}-3-2.0/%{name}/*.tpp
%{_libdir}/pkgconfig/*.pc
%{_docdir}/%{name}/2.0/html/*
%{_docdir}/%{name}/2.0/README
%{_docdir}/%{name}/2.0/NEWS
%{_docdir}/%{name}/2.0/BUGS
%{_docdir}/%{name}/2.0/COPYING
%{_docdir}/%{name}/2.0/PORTING*
%{_libdir}/libcxx-gtk-utils-3-2.0.so
%{_libdir}/libcxx-gtk-utils-3-2.0.so.0
