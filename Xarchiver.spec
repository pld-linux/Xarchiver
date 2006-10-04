# $Revision: 1.3 $Date: 2006-10-04 21:51:04 $
#
%define		xfce_version 4.3.99.1
#
Summary:	Xarchiver - a GTK+2 frontend to popular compression formats
Summary(pl):	Xarchiver - nak³adka GTK+2 na popularne formaty kompresji
Name:		Xarchiver
Version:	0.4.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{xfce_version}/src/xarchiver-%{version}.tar.bz2
# Source0-md5:	b74d61fd0998fa36c14ccb24e91e8ded
URL:		http://xarchiver.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	pkgconfig
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
Requires(post,postun):	desktop-file-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xarchiver is a GTK+2 frontend to 7z, zip, rar, tar, bzip2, gzip, arj
and rpm (open and extract only). Xarchiver allows to create, add,
extract and delete files in the above formats. 7z, zip, rar and arj
password protected archives are supported.

%description -l pl
Xarchiver to nak³adka GTK+2 na 7z, zip, rar, tar, bzip2, gzip, arj i
rpm (tylko otwieranie i rozpakowywanie). Xarchiver umo¿liwia
tworzenie, dodawanie, rozpakowywanie oraz usuwanie plików w powy¿szych
formatach. Obs³uguje równie¿ archiwa 7z, zip, rar i arj zabezpieczone
has³em.

%prep
%setup -q -n xarchiver-%{version}

%build
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

%find_lang xarchiver

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f xarchiver.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README TODO
%attr(755,root,root) %{_bindir}/xarchiver
%attr(755,root,root) %{_libdir}/thunar-archive-plugin/*.tap
%{_datadir}/xarchiver
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
