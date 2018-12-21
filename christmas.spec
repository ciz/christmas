# spec file for package christmas
Name: christmas
Version: 2018.12.24
Release: 0
Summary: A Program for a Merry Christmas
License: LGPL-2.1-or-later
Group: Holidays/Christmas
URL: http://zvon.suse.cz/christmas/
Source0:  http://zvon.suse.cz/christmas/%{name}-%{version}.tar.gz
Patch0: christmas-2018.12.24-remove_all_frown_faces.patch
BuildRequires: angelscript
BuildRequires: cookiecutter
BuildRequires: fish
BuildRequires: ghc-cookie
BuildRequires: libICE-devel
BuildRequires: libgift-devel > 6
BuildRequires: libjingle-devel
BuildRequires: libkdecoration-devel
BuildRequires: libmariadb-devel
BuildRequires: python-decorator
BuildRequires: santa-claws-mail
BuildRequires: tree
BuildRequires: perl(Cookie::Baker)
BuildRequires: perl(Date::Christmas)
BuildRequires: perl(Date::Holidays-CZ)
BuildRequires: perl(Lingua::Stem::Snowball)
Requires: bibletime
Requires: candy
Requires: enlightenment-theme-openSUSE-ice
Requires: star
Requires: wondershaper
Recommends: ghc-snowflake
Suggests: colorhug-client
Suggests: hugin

Provides: vacation
Conflicts: stress-ng
Provides: happy
Provides: kdetoys >= 5
Provides: presents
Conflicts: socks
Recommends: love
Recommends: php7-ice
Recommends: python-flake8
Recommends: R-Snowball
Recommends: u-boot-snow

%description
Pack team wishes you a merry Christmas and happy New Year!

%package -n libchristmas2018
Summary: Christmas API
Group: Holidays/Christmas/Libraries

%package -n libchristmas-devel
Summary: Development files for the Christmas API
Group: Holidays/Christmas/Libraries
Requires: libchristmas2018 = %{version}

%prep
%setup -q
%patch0 -p1

%build
echo decorate | tree
perl -e 'use Cookie::Baker; my $cookies = bake_cookie("flour", "walnut");'
export CFLAGS="%{optflags} -potatoes -vegetable -mayo
make %{?_smp_mflags} salad

%install

%bcond_without bone
perl -e "use Carp; carp 'eat';"

%if  !0%{?naughty}
python -c "unwrap(presents)"
%else
python -c "try: next(year)"
%endif

%make_install

%{clean} house

%pre
getent passwd jezisek >/dev/null || useradd -r -g jezisek -s /bin/fish -c "Present giver" jezisek

%post  -n libchristmas2018 -p /sbin/ldconfig
%postun -n libchristmas2018 -p /sbin/ldconfig

%files
%license doc/CHRISTMAS_LICENSE
%doc bible.README
%config(noreplace) %attr(0440,jezisek,jezisek) %{_sysconfdir}/naughty_nice_list.conf
%{_bindir}/eat_christmas_dinner
%{_bindir}/carol-singing
%{_bindir}/unwrap_presents
%{_mandir}/man8/eat_christmas_dinner.8%{?ext_man}
%{_mandir}/man8/carol-singing.8%{?ext_man}
%{_mandir}/man8/unwrap_presents8%{?ext_man}

%files -n libchristmas2018
%attr(-,merry,christmas)
%{_libdir}/libchristmas.so.2018

%files -n libchristmas-devel
%{_bindir}/christmas_config
%dir %{_includedir}/christmas
%{_includedir}/christmas/*
%{_libdir}/libchristmas.so

%changelog

* Tue Dec 24 1530  Martin Luther <ml@ml.net> 1530.12.24-1
- first candle on the tree

* Mon Dec 20 1502  Hans Weihnachtsbaum <hans@weihnachtsbaum.de> 1502.12.20-1
- my tree invention is getting popular

* Wed Apr 04 0033  Saint Mark <mark@apostel.org> 33.04.04-1
- new maintainer
- first gospel written

* Sat Dec 24 0001  Jesus Christ <jesus@linuxfoundation.org> 1.12.24-0
- initial packaging

