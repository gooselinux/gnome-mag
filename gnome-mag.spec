%define po_package gnome-mag

Summary: Screen magnifier for GNOME
Name: gnome-mag
Version: 0.15.9
Release: 2%{?dist}
License: LGPLv2+
Group: Desktop/Accessibility
URL: http://www.gnome.org/
Source0: http://download.gnome.org/sources/gnome-mag/0.15/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: intltool
BuildRequires: libX11-devel, libXtst-devel, libXdamage-devel
BuildRequires: libXfixes-devel, libXt-devel
BuildRequires: libXcomposite-devel, libXrender-devel
BuildRequires: libbonobo-devel
BuildRequires: gtk2-devel
BuildRequires: at-spi-devel
BuildRequires: gettext
BuildRequires: autoconf, automake, libtool

# updated translations
# https://bugzilla.redhat.com/show_bug.cgi?id=589204
Patch0: gnome-mag-translations.patch

%description
This package includes a screen magnifier, which allows you to zoom in on
portions of the desktop. The magnifier is provided as a service for use
by other applicaitons and assistive technologies.

%package devel
Summary:	Development files for gnome-mag
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbonobo-devel
Requires:	gtk2-devel
Requires:	pkgconfig

%description devel
This package contains files needed for developing applications
that are using gnome-mag.

%prep
%setup -q
%patch0 -p1 -b .translations

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' |xargs /bin/rm

%find_lang %{po_package}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{po_package}.lang
%defattr(-,root,root,-)
%doc AUTHORS README NEWS COPYING
%{_bindir}/magnifier
%{_libdir}/*.so.*
%{_libdir}/bonobo/servers/*
%{_libdir}/orbit-2.0/GNOME_Magnifier_module.so
%{_datadir}/gnome-mag
%{_mandir}/man1/magnifier.1.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/gnome-mag-1.0
%{_libdir}/pkgconfig/*pc
%{_libdir}/*.so
%{_datadir}/idl/gnome-mag-1.0
%{_datadir}/doc/gnome-mag*

%changelog
* Mon Jun 21 2010 Matthias Clasen <mclasen@redhat.com> - 0.15.9-2
- Update translations
Resolves: #589204

* Tue Sep 22 2009 Matthias Clasen <mclasen@redhat.com> - 0.15.9-1
- Update to 0.15.9

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 0.15.8-1
- Update to 0.15.8

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Matthias Clasen <mclasen@redhat.com> - 0.15.6-1
- Update to 0.15.6
- See http://download.gnome.org/sources/gnome-mag/0.15/gnome-mag-0.15.6.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 0.15.5-1
- Update to 0.15.5

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Matthias Clasen <mclasen@redhat.com> - 0.15.4-4
- Remove an unnecessary dependency

* Sun Nov 23 2008 Matthias Clasen <mclasen@redhat.com> - 0.15.4-2
- Tweak description

* Tue Sep 23 2008 Matthias Clasen <mclasen@redhat.com> - 0.15.4-1
- Update to 0.15.4

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 0.15.3-1
- Update to 0.15.3

* Sun Aug  3 2008 Matthias Clasen <mclasen@redhat.com> - 0.15.2-1
- Update to 0.15.2

* Tue Jul 15 2008 Matthias Clasen <mclasen@redhat.com> - 0.15.1-1
- Update to 0.15.1

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.15.0-2
- Autorebuild for GCC 4.3

* Fri Dec 28 2007 Matthias Clasen <mclasen@redhat.com> - 0.15.0-1
- Update to 0.15.0

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.10-1
- Update to 0.14.10

* Fri Sep 14 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.9-1
- Update to 0.14.9

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.8-1
- Update to 0.14.8

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.14.6-2
- Rebuild for selinux ppc32 issue.

* Sat Aug  4 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.6-2
- Update the license field

* Mon Jun 18 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.6-1
- Update to 0.14.6
- Drop upstreamed patch

* Mon Jun  4 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.5-1
- Update to 0.14.5

* Mon May 28 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.4-1
- Update to 0.14.4

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.3-1
- Update to 0.14.3

* Wed Jan 10 2007 Matthias Clasen <mclasen@redhat.com> - 0.14.1-1
- Update to 0.14.1

* Mon Dec 18 2006 Matthias Clasen <mclasen@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Wed Aug  2 2006 Matthias Clasen <mclasen@redhat.com> - 0.13.1-1.fc6
- Update to 0.13.1

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> 0.13.0-1
- Update to 0.13.0

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.12.6-1.1
- rebuild

* Wed Jul 12 2006 Matthias Clasen <mclasen@redhat.com> 0.12.6-1
- Update to 0.12.6

* Mon Jun 12 2006 Bill Nottingham  <notting@redhat.com> 0.12.5-2
- we don't call automake, don't buildreq it

* Thu May 18 2006 Matthias Clasen  <mclasen@redhat.com> 0.12.5-1
- Update to 0.12.5

* Mon May 15 2006 John (J5) Palmieri <johnp@redhat.com> - 0.12.4-1.1
- bump and rebuild

* Mon Mar 13 2006 Matthias Clasen  <mclasen@redhat.com> 0.12.4-1
- Update to 0.12.4

* Tue Feb 28 2006 Karsten Hopp <karsten@redhat.de> 0.12.3-3
- BuildRequires: libXt-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.12.3-2.1
- bump again for double-long bug on ppc(64)

* Thu Feb  9 2006 Matthias Clasen <mclasen@redhat.com> - 0.12.3-2
- Make it build

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.12.3-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Jan 19 2006 Matthias Clasen <mclasen@redhat.com>
- Update to 0.12.3

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Nov  1 2005 Matthias Clasen <mclasen@redhat.com> 0.12.2-2
- Switch requires to modular X

* Wed Oct  5 2005 Matthias Clasen <mclasen@redhat.com> 0.12.2-1
- Update to 0.12.2

* Tue Aug 16 2005 Matthias Clasen <mclasen@redhat.com> 
- Rebuilt

* Tue Jun 28 2005 Matthias Clasen <mclasen@redhat.com> 0.12.1-1
- Update to 0.12.1

* Wed Mar 30 2005 Matthias Clasen <mclasen@redhat.com> 0.12-2
- Add a missing Requires (#152493)

* Mon Mar 14 2005 Matthias Clasen <mclasen@redhat.com> 0.12-1
- Update to 0.12.0

* Wed Mar  2 2005 Matthias Clasen <mclasen@redhat.com> 0.11.14-2
- Rebuild with gcc4

* Wed Feb  9 2005 Matthias Clasen <mclasen@redhat.com> 0.11.14-1
- Update to 0.11.14

* Fri Jan 28 2005 Matthias Clasen <mclasen@redhat.com> 0.11.13-1
- Update to 0.11.13

* Mon Sep 20 2004 Colin Walters <walters@redhat.com> 0.11.7-1
- Update to 0.11.7

* Tue Aug 31 2004 Colin Walters <walters@redhat.com> 0.11.5-1
- Update to 0.11.5
- Add missing ldconfig calls (bz #131273)

* Wed Aug 18 2004 Colin Walters <walters@redhat.com> 0.11.4-1
- Update to 0.11.4

* Tue Aug 04 2004 Colin Walters <walters@redhat.com> 0.11.3-1
- Update to 0.11.3

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 18 2004 Colin Walters <walters@redhat.com> 0.11.2-1
- Update to 0.11.2

* Sat Apr 10 2004 Warren Togami <wtogami@redhat.com> 0.10.10-2
- BR automake14 intltool xorg-x11-devel libbonobo-devel gtk2-devel at-spi-devel gettext

* Wed Mar 31 2004 Mark McLoughlin <markmc@redhat.com> 0.10.10-1
- Update to 0.10.10

* Wed Mar 10 2004 Mark McLoughlin <markmc@redhat.com> 0.10.8-1
- Update to 0.10.8
- Fixup the lib64 patch

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 26 2004 Alexander Larsson <alexl@redhat.com> 0.10.7-1
- update to 0.10.7

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Oct  2 2003 Jonathan Blandford <jrb@redhat.com> 0.10.3-1
- new version

* Wed Sep 24 2003 Mike McLean <mikem@redhat.com> 0.10.2-4
- release bump and rebuild

* Mon Jul 28 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add defattr to -devel rpm

* Fri Jul 18 2003 Jonathan Blandford <jrb@redhat.com>
- fix lib64ism

* Fri May  9 2003 Jonathan Blandford <jrb@redhat.com> mag-1
- Initial build.


