%define _debugsource_template %{nil}
%define debug_package %{nil}

Name:           protonupd
Version:        3.0.1
Release:        2%{?dist}
Summary:        Download and install Proton releases with centralized storage
License:        GPL-3.0-or-later
URL:            https://github.com/sachesi/protonupd
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)

%generate_buildrequires
%pyproject_buildrequires

%description
protonupd is a CLI tool to download and install Proton builds into one
central store, then symlink them into Steam, Bottles, and Lutris paths.

%prep
%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files protonupd

install -Dm644 assets/usr/share/bash-completion/completions/%{name} \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 assets/usr/share/zsh/site-functions/_%{name} \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 assets/usr/share/fish/completions/%{name}.fish \
    %{buildroot}%{_datadir}/fish/completions/%{name}.fish

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/completions/%{name}.fish

%changelog
* Thu Apr 23 2026 protonupd packager <packager@protonupd> - 3.0.1-1
- Bump version to 3.0.1

* Thu Apr 23 2026 protonupd packager <packager@protonupd> - 3.0.0-2
- Include /usr/bin/protonupd in %%files to fix unpackaged file error
- Switch pyproject license to SPDX string and drop deprecated classifier
- Fix License

* Thu Apr 23 2026 protonupd packager <packager@protonupd> - 3.0.0-1
- Add Fedora RPM spec and COPR SRPM workflow
- Install shell completions from assets/usr/share
