Summary:	pportman - parallel port manager
Summary(pl.UTF-8):	pportman - menadżer portu równoległego
Name:		pportman
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://autko.net/~jackass/pportman/%{name}-%{version}.tar.gz
# Source0-md5:	93d4dc561ac1f8da185e2e671436c014
URL:		http://autko.net/~jackass/pportman
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pportman is a simple and nice parallel port manager. Writed in ncurses.

%description -l pl.UTF-8
pportman to prosty i przyjemny w obsłudzę menadżer portu równoległego. 
Został napisany w ncurses.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CFlAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
