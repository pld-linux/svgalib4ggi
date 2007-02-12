# NOTE: not compatible with svgalib (does not provide vgagl.h)
Summary:	GGI version of SVGA Library
Summary(pl.UTF-8):   Wersja GGI biblioteki SVGA
Name:		svgalib4ggi
Version:	0.6
Release:	6
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.gz
# Source0-md5:	f8515480c6935b2081135e71e7bc4a5c
URL:		http://www.ggi-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libggi-devel
BuildRequires:	libgii-devel
#Provides:	svgalib
#Obsoletes:	svgalib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is LibGGI wrapper for SVGAlib. It makes SVGAlib programs work
with LibGGI making them much more portable.

%description -l pl.UTF-8
To jest wrapper GGI do SVGAlib. Pozwala uruchamiać programy pisane dla
SVGAlib pod GGI, robiąc je bardziej przenośnymi.

%package devel
Summary:	Include files for [S]VGA graphics
Summary(pl.UTF-8):   Pliki nagłówkowe do grafiki [S]VGA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Provides:	svgalib-devel
#Obsoletes:	svgalib-devel

%description devel
These are header files that are needed to build programs which use
SVGAlib/svgalib4ggi.

%description devel -l pl.UTF-8
To są pliki nagłówkowe potrzebne do kompilowania programów używających
SVGAlib/svgalib4ggi.

%prep
%setup -q

%build
# libtool cannot be rebuilt (new version doesn't like "ggi" as library revision)
%{__aclocal} -I .
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

# unwanted - svgalib doesn't have it, so it cannot be here too
# if we want packages linked with svgalib4ggi be compatible with svgalib
rm -f $RPM_BUILD_ROOT%{_libdir}/libvga.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*.h
