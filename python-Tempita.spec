%define 	module	Tempita
Summary:	A very small text templating language
Summary(pl.UTF-8):	-
Name:		python-%{module}
Version:	0.4
Release:	0.2
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/T/Tempita/%{module}-%{version}.tar.gz
# Source0-md5:	0abe015a72e748d0c6284679a497426c
URL:		http://pythonpaste.org/tempita/
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
#Requires:		python-libs
Requires:	python-modules
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A very small text templating language.

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
# CFLAGS is only for arch packages - remove on noarch packages
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs
%dir %{py_sitescriptdir}/tempita
%{py_sitescriptdir}/tempita/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
