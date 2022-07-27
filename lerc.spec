Summary:	LERC - Limited Error Raster Compression
Summary(pl.UTF-8):	LERC (Limited Error Raster Compression) - kompresja rastrowa o ograniczonym błędzie
Name:		lerc
Version:	4.0.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/Esri/lerc/releases
Source0:	https://github.com/Esri/lerc/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f5b00e53bf507aba13ca3de02726e2ba
URL:		https://github.com/Esri/lerc
BuildRequires:	cmake >= 3.12
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpm-build >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LERC is an open-source image or raster format which supports rapid
encoding and decoding for any pixel type (not just RGB or Byte). Users
set the maximum compression error per pixel while encoding, so the
precision of the original input image is preserved (within user
defined error bounds).

%description -l pl.UTF-8
LERC to rastrowy format obrazów z otwartymi źródłami, obsługujący
szybkie kodowanie i dekodowanie dowolnego typu pikseli (nie tylko RGB
lub bajtów). Użytkownik przy kodowaniu ustawia maksymalny poziom błędu
kompresji na piksel, więc dokładność oryginalnego obrazu wejściowego
jest zachowana (w granicach błędu określonego przez użytkownika).

%package devel
Summary:	Header files for Lerc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Lerc
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for Lerc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Lerc.

%package doc
Summary:	Documentation for Lerc library
Summary(pl.UTF-8):	Dokumentacja biblioteki Lerc
Group:		Documentation
BuildArch:	noarch

%description doc
Documentation for Lerc library.

%description doc -l pl.UTF-8
Dokumentacja biblioteki Lerc.

%prep
%setup -q

%build
install -d builddir
cd builddir
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md NOTICE README.md
%attr(755,root,root) %{_libdir}/libLerc.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libLerc.so
%{_includedir}/Lerc_c_api.h
%{_includedir}/Lerc_types.h
%{_pkgconfigdir}/Lerc.pc

%files doc
%defattr(644,root,root,755)
%doc doc/{*.pdf,*.png,MORE.md}
