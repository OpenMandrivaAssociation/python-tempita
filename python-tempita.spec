%define tarname	Tempita

Summary:	A very small text templating language

Name:		python-tempita
Version:	0.5.3dev
Release:	1
Source0:	http://pypi.python.org/packages/source/T/Tempita/Tempita-%{version}.tar.gz
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


