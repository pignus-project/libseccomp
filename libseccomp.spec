Summary: Enhanced seccomp library
Name: libseccomp
Version: 0.1.0
Release: 2%{?dist}
ExclusiveArch: %{ix86} x86_64
License: LGPLv2
Group: System Environment/Libraries
Source: http://downloads.sf.net/project/libseccomp/%{name}-%{version}.tar.gz
URL: http://libseccomp.sourceforge.net
Requires: kernel >= 3.5

# force the build process to be as verbose as possible, nothing is hidden
Patch1: libseccomp-0.1.0-build_verbose.patch

%description
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%package devel
Summary: Development files used to build applications with libseccomp support
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release} pkgconfig

%description devel
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%prep
%setup -q
%patch1 -p1

%build
./configure --prefix="%{_prefix}" --libdir="%{_libdir}"
CFLAGS="%{optflags}" make

%install
rm -rf "%{buildroot}"
mkdir -p "%{buildroot}/%{_libdir}"
mkdir -p "%{buildroot}/%{_includedir}"
mkdir -p "%{buildroot}/%{_mandir}"
make DESTDIR="%{buildroot}" install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE
%doc CREDITS
%doc README
%{_libdir}/libseccomp.so.*

%files devel
%{_includedir}/seccomp.h
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%{_mandir}/man3/*

%changelog
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Paul Moore <pmoore@redhat.com> - 0.1.0-1
- Limit package to x86/x86_64 platforms (RHBZ #837888)
* Tue Jun 12 2012 Paul Moore <pmoore@redhat.com> - 0.1.0-0
- Initial version

