Summary:	GGI version of SVGA Library
Summary(pl):	Wersja GGI biblioteki SVGA
Name:		svgalib4ggi
Version:	0.6
Release:	5
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.gz
# Source0-md5:	f8515480c6935b2081135e71e7bc4a5c
URL:		http://www.ggi-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libggi-devel
BuildRequires:	libgii-devel
Provides:	svgalib
Obsoletes:	svgalib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is LibGGI wrapper for SVGAlib. It makes SVGAlib programs work
with LibGGI making them much more portable.

%description -l pl
To jest wrapper GGI do SVGAlib. Pozwala uruchamiaæ programy pisane dla
SVGAlib pod GGI, robi±c je bardziej przeno¶nymi.

%package devel
Summary:	Include files for [S]VGA graphics
Summary(pl):	Pliki nag³ówkowe do grafiki [S]VGA
Group:		Development/Libraries
Requires:	%{name} = %{version}
Provides:	svgalib-devel
Obsoletes:	svgalib-devel

%description devel
These are header files that are needed to build programs which use
SVGAlib/svgalib4ggi.

%description devel -l pl
To s± pliki nag³ówkowe potrzebne do kompilowania programów u¿ywaj±cych
SVGAlib/svgalib4ggi.

%prep
%setup -q

%build
rm -f missing
rm -f acinclude.m4
%{__aclocal} -I .
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/*.so
