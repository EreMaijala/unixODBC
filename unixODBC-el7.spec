%define name unixODBC
%define ver 2.3.4
%define prefix /usr
%define sysconfdir /etc

Summary: ODBC driver manager and drivers for PostgreSQL, MySQL, etc.
Name: %{name}
Version: %ver
Release: 1.el7
License: LGPL and GPL
Group: Applications/Databases
Source: %{name}-%{ver}.tar.gz
BuildRoot: /var/tmp/%{name}-%{ver}-root
URL: http://www.unixodbc.org/
Docdir: %{prefix}/doc
Prefix: %prefix

%description
unixODBC aims to provide a complete ODBC solution for the Linux platform.
All programs are GPL.
All libs are LGPL (except nn which is GPL?).

%package devel
Summary: Includes and static libraries for ODBC development
Group: Development/Libraries
Requires: %{name} = %{ver}

%description devel
unixODBC aims to provide a complete ODBC solution for the Linux platform.
All programs are GPL.
All libs are LGPL (except nn which is GPL?).
This package contains the include files and static libraries
for development.

%package gui-qt
Summary: ODBC configurator, Data Source browser and ODBC test tool based on Qt
Group: Applications/Databases
Requires: %{name} = %{ver}

%description gui-qt
unixODBC aims to provide a complete ODBC solution for the Linux platform.
All programs are GPL.
All libs are LGPL (except nn which is GPL?).
This package contains two Qt based GUI programs for unixODBC:
ODBCConfig and DataManager

%prep
%setup

%ifarch alpha
ARCH_FLAGS="--host=alpha-redhat-linux"
%endif

export -n LANG LINGUAS LC_ALL
if [ ! -f configure ]; then
CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir} 
else
CFLAGS="$RPM_OPT_FLAGS" ./configure $ARCH_FLAGS --prefix=%{prefix} --sysconfdir=%{sysconfdir} --enable-gui=no
fi

%build
export -n LANG LINGUAS LC_ALL
if [ "$SMP" != "" ]; then
(make "MAKE=make -k -j $SMP"; exit 0)
make
else
make
fi

%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT%{sysconfdir} install-strip
mv $RPM_BUILD_ROOT%{prefix}/lib $RPM_BUILD_ROOT%{prefix}/lib64

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)


%doc AUTHORS COPYING ChangeLog NEWS README doc

%config(noreplace) %{sysconfdir}/odbc.ini
%config(noreplace) %{sysconfdir}/odbcinst.ini
%{prefix}/bin/dltest
%{prefix}/bin/slencheck
%{prefix}/bin/isql
%{prefix}/bin/iusql
%{prefix}/bin/odbcinst
%{prefix}/bin/odbc_config
%{_libdir}/libodbc.so*
%{_libdir}/libodbccr.so*
%{_libdir}/libodbcinst.so*
%{prefix}/share/man/man1/dltest.1.gz
%{prefix}/share/man/man1/isql.1.gz
%{prefix}/share/man/man1/iusql.1.gz
%{prefix}/share/man/man1/odbc_config.1.gz
%{prefix}/share/man/man1/odbcinst.1.gz
%{prefix}/share/man/man5/odbc.ini.5.gz
%{prefix}/share/man/man5/odbcinst.ini.5.gz
%{prefix}/share/man/man7/unixODBC.7.gz

%files devel
%defattr(-, root, root)

%{prefix}/include/*
%{prefix}/lib64/*.la

%files gui-qt
%defattr(-, root, root)

