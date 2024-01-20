#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	Tempita
Summary:	A very small text templating language
Summary(pl.UTF-8):	Bardzo mały język szablonów tekstu
Name:		python-%{module}
Version:	0.5.2
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/T/Tempita/%{module}-%{version}.tar.gz
# Source0-md5:	4c2f17bb9d481821c41b6fbee904cea1
URL:		https://pypi.org/project/Tempita/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	sed >= 4.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A very small text templating language.

%description -l pl.UTF-8
Bardzo mały język szablonów tekstu.

%package -n python3-Tempita
Summary:	A very small text templating language
Summary(pl.UTF-8):	Bardzo mały język szablonów tekstu
Group:		Development/Languages/Python

%description -n python3-Tempita
A very small text templating language.

%description -n python3-Tempita -l pl.UTF-8
Bardzo mały język szablonów tekstu.

%prep
%setup -q -n %{module}-%{version}

%if %{with python3}
# 2to3 no longer supported by setuptools
install -d py3
cp -p setup.cfg setup.py py3
%{__sed} -i -e '/use_2to3=/d' py3/setup.py
2to3-%{py3_ver} tempita -o py3/tempita -n -W
%endif

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
cd py3
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
cd py3
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/tempita
%{py_sitescriptdir}/Tempita-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-Tempita
%defattr(644,root,root,755)
%{py3_sitescriptdir}/tempita
%{py3_sitescriptdir}/Tempita-%{version}-py*.egg-info
%endif
