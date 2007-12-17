%define name edos-mandriva-manual-tests
%define version 1.0.0
%define release %mkrel 2

Name:		%{name}
Summary:	EDOS XML specification files for Mandriva manual test procedures
Version:	%{version}
Release:	%{release}
URL:		http://www.edos-project.org
License:	GPL
Group:		Development/Other
Source0:	http://www.edos-project.org/releases/%{name}-%{version}.tar.bz2
Buildarch:      noarch
Packager:       Francois Dechelle <fdechelle@mandriva.com>

%description
EDOS XML specification files for Mandriva manual test procedures

%package drakconf
Summary: EDOS XML specification files for Mandriva manual test procedures (DrakConf)
Group:		Development/Other
%description drakconf
The EDOS XML specification files for Mandriva manual test procedures, for the DrakConf suite

%package drakxnet
Summary: EDOS XML specification files for Mandriva manual test procedures (DrakxNet)
Group:		Development/Other
%description drakxnet
The EDOS XML specification files for Mandriva manual test procedures, for the DrakxNet suite

%package drakxtools
Summary: EDOS XML specification files for Mandriva manual test procedures (DrakxTools)
Group:		Development/Other
%description drakxtools
The EDOS XML specification files for Mandriva manual test procedures, for the DrakxTools suite

%package evolution
Summary: EDOS XML specification files for Mandriva manual test procedures (Evolution)
Group:		Development/Other
%description evolution
The EDOS XML specification files for Mandriva manual test procedures, for the Evolution suite

%package flash
Summary: EDOS XML specification files for Mandriva manual test procedures (Flash)
Group:		Development/Other
%description flash
The EDOS XML specification files for Mandriva manual test procedures, for the Flash suite

%package gaim
Summary: EDOS XML specification files for Mandriva manual test procedures (Gaim)
Group:		Development/Other
%description gaim
The EDOS XML specification files for Mandriva manual test procedures, for the Gaim suite

%package gnome
Summary: EDOS XML specification files for Mandriva manual test procedures (Gnome)
Group:		Development/Other
%description gnome
The EDOS XML specification files for Mandriva manual test procedures, for the Gnome suite

%package installation
Summary: EDOS XML specification files for Mandriva manual test procedures (Installation)
Group:		Development/Other
%description installation
The EDOS XML specification files for Mandriva manual test procedures, for the Installation suite

%package isv
Summary: EDOS XML specification files for Mandriva manual test procedures (ISV)
Group:		Development/Other
%description isv
The EDOS XML specification files for Mandriva manual test procedures, for the ISV suite

%package kde
Summary: EDOS XML specification files for Mandriva manual test procedures (KDE)
Group:		Development/Other
%description kde
The EDOS XML specification files for Mandriva manual test procedures, for the KDE suite

%package mandrivaservice
Summary: EDOS XML specification files for Mandriva manual test procedures (MandrivaService)
Group:		Development/Other
%description mandrivaservice
The EDOS XML specification files for Mandriva manual test procedures, for the MandrivaService suite

%package openoffice
Summary: EDOS XML specification files for Mandriva manual test procedures (OpenOffice)
Group:		Development/Other
%description openoffice
The EDOS XML specification files for Mandriva manual test procedures, for the OpenOffice suite

%package themes
Summary: EDOS XML specification files for Mandriva manual test procedures (Themes)
Group:		Development/Other
%description themes
The EDOS XML specification files for Mandriva manual test procedures, for the Themes suite

%package upgrade
Summary: EDOS XML specification files for Mandriva manual test procedures (Upgrade)
Group:		Development/Other
%description upgrade
The EDOS XML specification files for Mandriva manual test procedures, for the Upgrade suite

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 
%makeinstall

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

%files drakconf
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/DrakConf

%files drakxnet
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/DrakxNet

%files drakxtools
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/DrakxTools

%files evolution
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/Evolution

%files flash
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/Flash

%files gaim
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/Gaim

%files gnome
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/Gnome

%files installation
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/Installation

%files isv
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/ISV

%files kde
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/KDE

%files mandrivaservice
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/MandrivaService

%files openoffice
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/OpenOffice

%files themes
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/Themes

%files upgrade
%defattr(-,root,root)
%_datadir/edos/tests/mandriva-manual-tests/Upgrade

%changelog
* Tue Oct 31 2006 Francois Dechelle <fdechelle@mandriva.com>
- initial package

