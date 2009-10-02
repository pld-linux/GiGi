# TODO:
# - Checking for C header file IL/ilut.h... no
#   Note: since SDL support is disabled, the SDL headers are not be in the
#   compiler's search path during tests.  If DevIL was built with SDL support,
#   this may cause the seach for ilut.h to fail.

Summary:	GUI Library for OpenGL
Name:		GiGi
Version:	0.6.0
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gigi/GG-%{version}.tgz
# Source0-md5:	e100bad1c0713b3167a4fdc1cb8898c9
Patch0:		gg-boots-include-location-fix.patch
URL:		http://gigi.sourceforge.net/
BuildRequires:	scons
BuildRequires:	boost-devel >= 1.32
BuildRequires:	boost-signals >= 1.32
BuildRequires:	boost-filesystem >= 1.32
BuildRequires:	freetype-devel
BuildRequires:	DevIL-devel >= 1.6.1
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GiGi (aka GG) is a GUI library for OpenGL. It is platform-independent (it runs
at least on Linux and Windows, and probably more), compiler-independent (it
compiles under at GCC 3.4 or higher and MSVC++ 8.0 SP1 or higher, and probably
more), and driver-independent.

%package libs
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries

%description libs

%description libs -l pl.UTF-8

%package devel
Summary:	Header files for ... library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ...
Group:		Development/Libraries
# if base package contains shared library for which these headers are
#Requires:	%{name} = %{version}-%{release}
# if -libs package contains shared library for which these headers are
#Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for ... library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl.UTF-8):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl.UTF-8
Statyczna biblioteka ....

%prep
%setup -q -n GG
%patch0

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
