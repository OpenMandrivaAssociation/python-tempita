%define tarname	Tempita
%define name	python-tempita
%define version 0.5
%define release %mkrel 0.dev.0

Summary:	A very small text templating language
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/T/%{tarname}/%{tarname}-%{version}dev.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://pythonpaste.org/tempita/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
string.Template or % substitution. It's small, it embeds Python in
strings, and it doesn't do much else.

%prep
%setup -q -n %{tarname}-%{version}dev

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
