Summary:	GGI version of SVGA Library
Summary(pl):	Wersja GGI biblioteki SVGA
Name:		svgalib4ggi
Version:	0.6
Release:	3
License:	distributable
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.gz
URL:		http://www.ggi-project.org/
BuildRequires:	autoconf
BuildRequires:	libggi-devel
BuildRequires:	libgii-devel
Provides:	svgalib
Obsoletes:	svgalib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is LibGGI wrapper for SVGAlib. It makes SVGAlib programs work
with LibGGI making them much more portable.

%description -l pl
To jest wrapper GGI do SVGAlib. Pozwala uruchamiaÊ programy pisane dla
SVGAlib pod GGI, robi±c je bardziej przeno∂nymi.

%package devel
Summary:	Include files for [S]VGA graphics
Summary(pl):	Pliki nag≥Ûwkowe do grafiki [S]VGA
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}
Provides:	svgalib-devel
Obsoletes:	svgalib-devel

%description devel
These are header files that are needed to build programs which use
SVGAlib/svgalib4ggi.

%description devel -l pl
To s± pliki nag≥Ûwkowe potrzebne do kompilowania programÛw uøywaj±cych
SVGAlib/svgalib4ggi.

%prep
%setup -q

%build
autoconf
%configure \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf README NEWS

%clean
rm -rf $RPM_BUILD_ROOT

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
