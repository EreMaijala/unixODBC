How to Build unixODBC RPM Packages for RHEL 6.x
=================================================

Note that packages created with this method may not contain the drivers, so you will need to install them (such as mysql-connector-odbc) separately. Note that the separate packages may use a different names for the drivers (check /etc/odbcinst.ini). 

Prerequisites
-------------

You'll probably need to do everything on an RHEL 6.x server to be sure the results are correct. These instructions assume you have terminal open in a suitable working directory.

Execute the following commands to install the rpmbuild command and to create the initial directories:

    yum install rpm-build
    mkdir -p rpmbuild/SOURCES
    
Building the RPMs
-----------------

1. Download unixODBC.spec from this repository
2. Download unixODBC source package from http://www.unixodbc.org/, e.g.

        wget ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.3.tar.gz

3. Put the package into rpmbuild/SOURCES:

        mv unixODBC-*.tar.gz rpmbuild/SOURCES/
    
4. Build the RPMs:

        rpmbuild -bb ./unixODBC.spec
        
5. The finished RPMs can be found in rpmbuild/RPMS/x86_64 directory. Enjoy!

Ready-made RPMs
---------------

Precompiled RPMs are available in the RPMS directory. As usual, use at your own risk!