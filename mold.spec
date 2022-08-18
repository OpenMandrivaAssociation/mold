%define _empty_manifest_terminate_build 0

Summary: Modern and fast linker
Name: mold
Version: 1.4.1
Release: 1
Group:   Development
License: AGPLv3
URL:     https://github.com/rui314/mold
Source0: https://github.com/rui314/mold/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(tbb)
 
%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than LLVM lld linker, the second-fastest
open-source linker.
mold is created for increasing developer productivity by reducing
build time especially in rapid debug-edit-rebuild cycles.

%prep
%autosetup -p1

%build
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} LTO=1 SYSTEM_TBB=1

%install
export MANDIR=%{_mandir}
export LIBDIR=%{_libdir}
export LIBEXECDIR=%{_libexecdir}
export BINDIR=%{_bindir}
%make_install PREFIX=%{_prefix} BINDIR=%{_bindir} MANDIR=%{_mandir} LIBDIR=%{_libdir} LIBEXECDIR=%{_libexecdir} LTO=1 SYSTEM_TBB=1

%files
%{_bindir}/mold
%{_bindir}/l*
%{_libexecdir}/mold/ld
%{_libdir}/mold/mold-wrapper.so
%{_mandir}/man1/mold.1*
