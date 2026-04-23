%define _debugsource_template %{nil}
%define debug_package %{nil}

Name:           protonupd
Version:        3.0.0
Release:        1%{?dist}
Summary:        Download and install Proton releases with centralized storage
License:        MIT
URL:            https://github.com/sachesi/protonupd
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

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

install -Dm644 assets/usr/share/completions/bash/%{name} \
    %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 assets/usr/share/completions/zsh/_%{name} \
    %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 assets/usr/share/completions/fish/%{name}.fish \
    %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
* Thu Apr 23 2026 protonupd packager <packager@protonupd> - 3.0.0-1
- Add Fedora RPM spec and COPR SRPM workflow
- Install shell completions from assets/usr/share/completions
