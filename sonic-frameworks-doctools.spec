%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname SonicFrameworksDocTools
%define devname %mklibname SonicFrameworksDocTools -d
#define git 20240217

Name: sonic-frameworks-doctools
Version: 6.26.0
Release: %{?git:0.%{git}.}1
URL: https://github.com/Sonic-DE/sonic-frameworks-doctools
Source0: %url/archive/%version/%name-%version.tar.gz
Summary: Create documentation from DocBook
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6I18n)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: libxml2-utils
BuildRequires: docbook-dtds
BuildRequires: perl(URI::Escape)
Requires: %{libname} = %{EVRD}
Requires: docbook-dtd45-xml
Requires: docbook-style-xsl

Conflicts:  kf6-kdoctools

%description
Create documentation from DocBook

%package -n %{libname}
Summary: Create documentation from DocBook
Group: System/Libraries
Requires: %{name} = %{EVRD}
Conflicts:  %{_lib}KF6DocTools

%description -n %{libname}
Create documentation from DocBook

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Conflicts: %{_lib}KF6DocTools-devel

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Create documentation from DocBook

%install -a
%find_lang %{name} --all-name --with-qt --with-html --with-man
rm -rf %{buildroot}/%{_libdir}/cmake

%files -f %{name}.lang
%{_bindir}/checkXML6
%{_bindir}/meinproc6
%{_datadir}/kf6/kdoctools
%{_mandir}/man1/checkXML6.1*
%{_mandir}/man1/meinproc6.1*
%{_mandir}/man7/kf6options.7*
%{_mandir}/man7/qt6options.7*

%files -n %{devname}
%{_includedir}/KF6/KDocTools

# pending rename
# %{_libdir}/cmake/KF6DocTools

%files -n %{libname}
%{_libdir}/libKF6DocTools.so*
