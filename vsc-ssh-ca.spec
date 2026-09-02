Summary: A list of IP addresses to whitelist for VSC logins
Name: vsc-ssh-ca
Version: 1.0
Release: 1
License: GPL
Group: Applications/System
BuildArch: noarch
Source: %{name}-%{version}.tar.gz

%description
The different certificat authorities in use by VSC for VSC users.

%prep
%setup -q

%build
cat brussel.pub leuven.pub > vsc-ca.pub

%install
%{__mkdir_p} %{buildroot}%{_sysconfdir}/certs
%{__install} -p -m444 vsc-ca.pub %{buildroot}%{_sysconfdir}/certs/vsc-ca.pub

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/certs/vsc-ca.pub

%changelog
* Wed Sep 02 2026 Ward Poelmans <ward.poelmans@vub.be>
- Initial version with CA from KULeuven and VUB
