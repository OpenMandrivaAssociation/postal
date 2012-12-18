Summary:	SMTP and POP benchmark program
Name:		postal
Version:	0.72
Release:	1
Group:		Networking/Mail
License:	GPLv3
URL:		http://doc.coker.com.au/projects/postal/
Source0:	http://www.coker.com.au/postal/%{name}-%{version}.tgz
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libgcrypt)

%description
This program starts a specified number of processes to send as much random data
to random accounts as possible. Adds the X-Postal header to email it sends, so
if someone uses it unethically then it will be easy to filter via procmail.

%prep
%setup -q

%build

%configure2_5x \
	--disable-openssl \
	--disable-static \
	--disable-stripping

%make 

%install
%makeinstall_std

%files
%doc debian/changelog credits.txt
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man*/*

