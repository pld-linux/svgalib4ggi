Summary:	GGI version of SVGA Library 
Name:		svgalib4ggi
Version:	0.6
Release:	1
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.gz
URL:		http://www.ggi-project.org
Provides:	svgalib
Obsoletes:	svgalib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is LibGGI wrapper for SVGAlib.
It makes SVGAlib programs work with LibGGI making them much more portable 

%package devel
Summary:	development libraries and include files for [S]VGA graphics
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
These are the libraries and header files that are needed to build programs
which use SVGAlib/svgalib4ggi.

%prep
%setup -q

gzip README NEWS

%build
LDFLAGS="-s" ; export LDFLAGS
%configure \
	--disable-debug
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR="$RPM_BUILD_ROOT"
	
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz NEWS.gz
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/*.so
