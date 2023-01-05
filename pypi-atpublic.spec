#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-atpublic
Version  : 3.1.1
Release  : 14
URL      : https://files.pythonhosted.org/packages/8e/9a/ff8783e9e181ead59ae612a5df5bcd4f4bb3cc4147ef6aaa96f90020347b/atpublic-3.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/9a/ff8783e9e181ead59ae612a5df5bcd4f4bb3cc4147ef6aaa96f90020347b/atpublic-3.1.1.tar.gz
Summary  : Keep all y'all's __all__'s in sync
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-atpublic-license = %{version}-%{release}
Requires: pypi-atpublic-python = %{version}-%{release}
Requires: pypi-atpublic-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pdm_pep517)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
======================
@public and @private
======================
This library provides two very simple decorators that document the
*publicness* of the names in your module.  They keep your module's ``__all__``
in sync so you don't have to.

%package license
Summary: license components for the pypi-atpublic package.
Group: Default

%description license
license components for the pypi-atpublic package.


%package python
Summary: python components for the pypi-atpublic package.
Group: Default
Requires: pypi-atpublic-python3 = %{version}-%{release}

%description python
python components for the pypi-atpublic package.


%package python3
Summary: python3 components for the pypi-atpublic package.
Group: Default
Requires: python3-core
Provides: pypi(atpublic)

%description python3
python3 components for the pypi-atpublic package.


%prep
%setup -q -n atpublic-3.1.1
cd %{_builddir}/atpublic-3.1.1
pushd ..
cp -a atpublic-3.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672256790
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-atpublic
cp %{_builddir}/atpublic-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-atpublic/fb13b374a3ad37a4359fcdefcdbc99afb0aee68b || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-atpublic/fb13b374a3ad37a4359fcdefcdbc99afb0aee68b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
