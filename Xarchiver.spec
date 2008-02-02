#
%define		xfce_version	4.4.0
#
Summary:	Xarchiver - a GTK+2 frontend to popular compression formats
Summary(pl.UTF-8):	Xarchiver - nakładka GTK+2 na popularne formaty kompresji
Name:		Xarchiver
Version:	0.4.6
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xarchiver/xarchiver-%{version}.tar.bz2
# Source0-md5:	9700305deef4e2b6878697bd18bd2dd9
URL:		http://xarchiver.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.8.20
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xarchiver is a GTK+2 frontend to 7z, zip, rar, tar, bzip2, gzip, arj
and rpm (open and extract only). Xarchiver allows to create, add,
extract and delete files in the above formats. 7z, zip, rar and arj
password protected archives are supported.

%description -l pl.UTF-8
Xarchiver to nakładka GTK+2 na 7z, zip, rar, tar, bzip2, gzip, arj i
rpm (tylko otwieranie i rozpakowywanie). Xarchiver umożliwia
tworzenie, dodawanie, rozpakowywanie oraz usuwanie plików w powyższych
formatach. Obsługuje również archiwa 7z, zip, rar i arj zabezpieczone
hasłem.

%prep
%setup -q -n xarchiver-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_docdir}/xarchiver/{AUTHORS,ChangeLog,COPYING,NEWS,README,TODO}

%find_lang xarchiver

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f xarchiver.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xarchiver
%attr(755,root,root) %{_libdir}/thunar-archive-plugin/*.tap
%dir %{_docdir}/xarchiver
%docdir %{_docdir}/xarchiver
%{_docdir}/xarchiver/html
%{_iconsdir}/hicolor/*/apps/*.png
%{_pixmapsdir}/xarchiver
%{_desktopdir}/*.desktop
