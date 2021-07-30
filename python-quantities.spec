%global module_name     quantities

Name:       python-%{module_name}
Version:    0.12.3
Release:    2
Summary:    Support for physical quantities with units, based on numpy

License:    BSD
URL:        https://pypi.org/project/quantities/

Source0:    https://files.pythonhosted.org/packages/89/44/a875b723f70935b022d6b7a02c12a020e3b1777aa7bfc6fc243a908bc650/%{module_name}-%{version}.tar.gz

Source1:    license.rst


BuildArch:      noarch


%global _description\
Quantities is designed to handle arithmetic and conversions of physical\
quantities, which have a magnitude, dimensionality specified by various units,\
and possibly an uncertainty. See the tutorial for examples. Quantities builds\
on the popular numpy library and is designed to work with numpy ufuncs, many of\
which are already supported. Quantities is actively developed, and while the\
current features and API are stable, test coverage is incomplete so the package\
is not suggested for mission-critical applications.

%description %_description

%package -n python3-%{module_name}
Summary:    Support for physical quantities with units, based on numpy
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
Requires:       python3-numpy
%{?python_provide:%python_provide python3-%{module_name}}

%description -n python3-%{module_name} %_description

%prep
%autosetup -n %{module_name}-%{version} -p1
cp %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{module_name}
%doc CHANGES.txt license.rst
%{python3_sitelib}/%{module_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{module_name}/


%changelog
* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 0.12.3-2
- DESC: delete -S git from %autosetup, and delete BuildRequires git-core


* Tue July 06 2021 duyiwei<duyiwei@kylinos.cn> 0.12.3-1
- Init package
