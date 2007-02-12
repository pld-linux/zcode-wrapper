Summary:	Wrapper for running old Infocom text games
Summary(pl.UTF-8):   Wrapper do uruchamiania starych tekstówek Infocomu
Name:		zcode-wrapper
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	zcode-wrapper.sh
Requires:	zcode-interpreter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper for running old Infocom text games.

%description -l pl.UTF-8
Wrapper do uruchamiania starych tekstówek Infocomu.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/zcode

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/games/zcode/wrapper.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/games/zcode
%attr(755,root,root) %{_datadir}/games/zcode/wrapper.sh
