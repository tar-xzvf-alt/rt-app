%define _unpackaged_files_terminate_build 1
Name: rt-app
Version: 1.0
Release: alt2.gitd6f8be4
Summary: Synthetic real-time periodic workload generator
License: GPLv2
Group: System/Kernel and hardware 
Url: https://github.com/scheduler-tools/rt-app
Vcs: https://github.com/scheduler-tools/rt-app

BuildRequires(pre): rpm-build-python3
BuildRequires: autoconf automake libtool
BuildRequires: libjson-c-devel
BuildRequires: libnuma-devel

Source0: %name-%version.tar
Patch0: rt-app-alt-configure-ac-version.patch
Patch1: rt-app-alt-workgen-python3.patch

%description
rt-app is a test application that starts multiple periodic threads
in order to simulate a real-time periodic load. It is capable of
emulating configurable real-time workloads with various scheduling
policies (SCHED_FIFO, SCHED_RR, SCHED_DEADLINE) and measuring
wakeup latency, slack, and other timing metrics.

%prep
%setup
%autopatch -p1
%python3_fix_shebang doc/workgen

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

install -d %buildroot%_datadir/%name/examples
cp -r doc/examples/* %buildroot%_datadir/%name/examples/
install -pDm644 doc/tutorial.txt %buildroot%_datadir/%name/tutorial.txt

%files

%doc README COPYING
%_bindir/rt-app
%_bindir/workgen
%_datadir/%name/

%changelog
* Wed Jul 15 2026 Taran Evgeniy <taranev@basealt.ru> 1.0-alt2.gitd6f8be4
- Fixed version generation when building without Git metadata.
- Ported the workgen helper to Python 3.

* Mon Jul 14 2026 Taran Evgeniy <taranev@basealt.ru> 1.0-alt1.gitd6f8be4
- Init packaging
