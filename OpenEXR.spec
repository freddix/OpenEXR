Summary:	High dynamic-range (HDR) image file format support libraries
Name:		OpenEXR
Version:	2.2.0
Release:	1
License:	Industrial Light & Magic
Group:		Libraries
Source0:	http://download.savannah.nongnu.org/releases/openexr/openexr-%{version}.tar.gz
# Source0-md5:	b64e931c82aa3790329c21418373db4e
URL:		http://www.openexr.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ilmbase-devel >= 2.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	zlib-devel
# broken build system
BuildConflicts:	OpenEXR
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenEXR is a high dynamic-range (HDR) image file format developed by
Industrial Light & Magic for use in computer imaging applications.
OpenEXR is used by ILM on all motion pictures currently in production.
The first movies to employ OpenEXR were Harry Potter and the Sorcerers
Stone, Men in Black II, Gangs of New York, and Signs. Since then,
OpenEXR has become ILM's main image file format.

%package devel
Summary:	Header files for OpenEXR libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OpenEXR libraries.

%package progs
Summary:	OpenEXR utilities
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
OpenEXR utilities.

%prep
%setup -qn openexr-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libIlmImf-2_2.so.22
%attr(755,root,root) %ghost %{_libdir}/libIlmImfUtil-2_2.so.22
%attr(755,root,root) %{_libdir}/libIlmImf-2_2.so.*.*.*
%attr(755,root,root) %{_libdir}/libIlmImfUtil-2_2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libIlmImf.so
%attr(755,root,root) %{_libdir}/libIlmImfUtil.so
%{_includedir}/OpenEXR/Imf*.h
%{_includedir}/OpenEXR/OpenEXRConfig.h
%{_aclocaldir}/openexr.m4
%{_pkgconfigdir}/OpenEXR.pc

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exrenvmap
%attr(755,root,root) %{_bindir}/exrheader
%attr(755,root,root) %{_bindir}/exrmakepreview
%attr(755,root,root) %{_bindir}/exrmaketiled
%attr(755,root,root) %{_bindir}/exrmultipart
%attr(755,root,root) %{_bindir}/exrmultiview
%attr(755,root,root) %{_bindir}/exrstdattr

