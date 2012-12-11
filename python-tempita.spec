%define tarname	Tempita

Summary:	A very small text templating language
Name:		python-tempita
Version:	0.5.1
Release:	2
Source0:	http://pypi.python.org/packages/source/T/%{tarname}/%{tarname}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/tempita/
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
string.Template or % substitution. It's small, it embeds Python in
strings, and it doesn't do much else.

%prep
%setup -q -n %{tarname}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST

%files -f FILE_LIST

%changelog
* Mon Jun 13 2011 Lev Givon <lev@mandriva.org> 0.5.1-1mdv2011.0
+ Revision: 684945
- Update to 0.5.1.

* Thu Mar 31 2011 Lev Givon <lev@mandriva.org> 0.5-0.dev.0
+ Revision: 649453
- import python-tempita


