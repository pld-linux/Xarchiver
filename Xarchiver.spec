
%define		xfce_version	4.4.0
Summary:	Xarchiver - a GTK+2 frontend to popular compression formats
Summary(pl.UTF-8):	Xarchiver - nakładka GTK+2 na popularne formaty kompresji
Name:		Xarchiver
Version:	0.5.4.14
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	https://github.com/ib/xarchiver/archive/%{version}/xarchiver-%{version}.tar.gz
# Source0-md5:	70e60118c59fe647f620b07f83907fc9
Patch0:		%{name}-desktop.patch
URL:		https://github.com/ib/xarchiver/wiki
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.8.20
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
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
%patch0 -p1
mv -f po/pt{_PT,}.po
sed -e 's/pt_PT/pt/' -i po/LINGUAS

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

%{__rm} $RPM_BUILD_ROOT%{_docdir}/xarchiver/{ChangeLog,COPYING,README}

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
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/xarchiver
%attr(755,root,root) %{_libexecdir}/thunar-archive-plugin/*.tap
%docdir %{_docdir}/xarchiver
%{_docdir}/xarchiver
%{_iconsdir}/hicolor/*/apps/xarchiver.png
%{_iconsdir}/hicolor/scalable/apps/xarchiver.svg
%{_pixmapsdir}/xarchiver
%{_desktopdir}/*.desktop
%{_mandir}/man1/xarchiver.1*
