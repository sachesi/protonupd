# protonupd

CLI tool to manage Proton builds. Downloads releases to a central store and symlinks them into compatibility tool paths for Steam, Bottles, Lutris, and Leyen.

## Features

- Centralized storage for Proton builds.
- Automatic symlinking for Steam (Native/Flatpak), Bottles (Native/Flatpak), Lutris (Native/Flatpak), and Leyen.
- CPU instruction set detection (v2, v3, v4) for build compatibility.
- "latest" and source-specific (e.g. `ge-proton-latest`) symlink aliases.

## Installation

```bash
pip install .
```

To build an RPM:
```bash
make ba-local
```

### Nix

Run directly:
```bash
nix run github:sachesi/protonupd
```

Install to system (NixOS):
Add to `environment.systemPackages` or use as a flake input.


## Usage

Run the interactive wizard:
```bash
protonupd
```

For specific actions:
```bash
protonupd --help
```

### Configuration
- Config: `~/.config/protonupd/config.json`
- Store: `~/.local/share/protonupd/store`

Built with Gemini
