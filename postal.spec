Summary:	SMTP and POP benchmark program
Name:		postal
Version:	0.62
Release:	%mkrel 6
Group:		Networking/Mail
License:	GPL
URL:		http://www.coker.com.au/postal/
Source0:	http://www.coker.com.au/postal/%{name}-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRequires:	libstdc++-devel

%description
This program starts a specified number of processes to send as much random data
to random accounts as possible. Adds the X-Postal header to email it sends, so
if someone uses it unethically then it will be easy to filter via procmail.

%prep

%setup -q

%build

%configure2_5x \
    --disable-stripping

%make 

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -m755 postal %{buildroot}%{_sbindir}/
install -m755 postal-list %{buildroot}%{_sbindir}/
install -m755 rabid %{buildroot}%{_sbindir}/
install -m644 *.8 %{buildroot}%{_mandir}/man8/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc debian/changelog credits.txt
%{_sbindir}/*
%{_mandir}/man*/*


