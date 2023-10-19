%define _empty_manifest_terminate_build 0
%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration

Summary: Modern and fast linker
Name: mold
Version: 2.3.0
Release: 1
Group:   Development
License: MIT
URL:     https://github.com/rui314/mold
Source0: https://github.com/rui314/mold/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Patch0:  mold-2.3.0-static-helpers.patch
BuildRequires: cmake
BuildRequires: ninja
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
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc %{_datadir}/doc/mold/LICENSE
%doc %{_datadir}/doc/mold/LICENSE.third-party
%{_bindir}/mold
%{_bindir}/l*
%{_libexecdir}/mold/ld
%{_libdir}/mold/mold-wrapper.so
%{_mandir}/man1/mold.1*
%{_mandir}/man1/ld.mold.1*
