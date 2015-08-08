%define name smeserver-phpvirtualbox-5.0
%define version 5.0.0
%define release 1
%define rpmver   5.0.0
Summary: smserver rpm to install phpvirtualbox
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
URL: http://mirror.de-labrusse.fr
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
#Patch0: smeserver-phpvirtualbox-force-https.patch
#Patch1: smeserver-phpvirtualbox-unix-group.patch
#Patch2: smeserver-phpvirtualbox-4.3.0-remove-webauth.patch
#Patch3: smeserver-phpvirtualbox-4.3.0-add_webauth_migrate_fragment.patch
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 8.0
Requires: php-soap
Requires: phpvirtualbox-5.0

AutoReqProv: no
%description
smserver rpm to install phpvirtualbox : An open source, AJAX implementation of the VirtualBox user interface written in PHP. As a 
modern web interface, it allows you to access and control remote VirtualBox instances. phpVirtualBox is designed to allow users to 
administer VirtualBox in a headless environment - mirroring the VirtualBox GUI through its web interface.

%changelog
* Thu Aug 06 2015 stephane de labrusse <stephdl@de-labrusse.fr> 5.0.0-1
- require to phpvirtualbox-5.0

* Sun May 18 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.1-3
- first release to sme9
- unixgroup removed from the contribs
- fix ssl redirection

* Wed Mar 19 2014 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.1-1
- due to the bug correction of phpvirtualbox, this version give back the web authentication with migrate fragment update
* Wed Jan 08 2014 JP Pialasse <tests@pialasse.com> 4.3.0-10.sme
- changing requires to phpvirtualbox = 4.3
* Mon Dec 30 2013 JP Pialasse <tests@pialasse.com> 4.3.0-9.sme
- renaming to import into buildsys
* Fri Dec 13 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-8
- remove the web authentication for the buildin phpvirtualbox authentication 
* Sun Nov 10 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-7
- removing dependance to smeserver-virtualbox-4.3
* Tue Nov 05 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-6
- change name to match the phpvirtualbox version
* Wed Oct 23 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-5
- Clean 92phpvirtualbox to force only the localnetwork
- Add the plugin unixgroup (from pwauth) to allow unix groups to reach the apache server.
- you can see http://code.google.com/p/pwauth/ for more informations
* Sun Oct 20 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-4
- Force https protocol for phpvirtualbox
* Sat Oct 19 2013 stephane de labrusse <stephdl@de-labrusse.fr> 4.3.0-3
- Initial release

%prep
%setup
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
%build
#perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre

%preun

%post

echo "=============================================================="
echo "	Please do not forget to install the extension pack "
echo "	You need it to activate the virtualbox RDP server"                         
echo "	And many features, see this page to manage it by CL"
echo "  "                                                                   
echo "	https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack"
echo " "
echo "	The download page : https://www.virtualbox.org/wiki/Downloads"
echo "=============================================================="


%postun
#uninstall
if [ $1 = 0 ] ; then
 /sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
 /usr/local/bin/svc -h /service/httpd-e-smith
fi
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

