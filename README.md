# terraform-rpm

> RPM package for Terraform.

## Requirements

```bash
## Fedora
dnf install fedora-packager fedora-review -y
```

## Setup your tree ( Optional )

Create the directory structure for the `~/rpmbuild` directory.

```bash
rpmdev-setuptree
```

## Download Source0

This will download the sources or patches listed with a URL into your RPM's `%{_sourcedir}`.

```bash
spectool -g -R terraform.spec
```

## Build the package

To package up the binary.

```bash
rpmbuild -bb terraform.spec
```