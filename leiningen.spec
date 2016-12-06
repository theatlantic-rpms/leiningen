Name:           leiningen
Version:        2.7.1
Release:        0
Summary:        Automating Clojure projects without setting your hair on fire
License:        EPL-1.0
Group:          Development/Tools/Building
Url:            http://leiningen.org/
Source0:        https://github.com/technomancy/leiningen/releases/download/%{version}/leiningen-%{version}-standalone.zip
Source1:        lein
Source2:        lein.1
Source3:        zsh_completion.zsh
Source4:        bash_completion.bash
Requires:       java >= 1.7.0
Requires:       clojure >= 1.5.1
BuildArch:      noarch

%description
Working on Clojure projects with tools designed for Java can be an
exercise in frustration. With Leiningen, you describe your build with
Clojure. Leiningen handles fetching dependencies, running tests,
packaging your projects and can be easily extended with a number of
plugins.

%prep
%setup -q -D -T -c

%build

%install
install -p -D -m 0755 %{SOURCE0} %{buildroot}%{_datadir}/java/leiningen-%{version}-standalone.jar
install -p -D -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/lein
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/lein.1
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/zsh_completion.d/_lein
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/bash_completion.d/lein.sh

%files
%defattr(-,root,root)
%{_bindir}/lein
%{_datadir}/java/leiningen-%{version}-standalone.jar
%doc %{_mandir}/man1/lein*
%config %{_sysconfdir}/bash_completion.d/*.sh
%config %{_sysconfdir}/zsh_completion.d

%changelog