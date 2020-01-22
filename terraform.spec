%define debug_package %nil

Name:       terraform
Version:    0.12.19
Release:    1%{?dist}
Summary:    Infrastructure as Code to provision and manage any cloud, infrastructure, or service
License:    MPL 2.0
URL:        https://www.terraform.io/
BuildArch:  x86_64
Source0:    https://releases.hashicorp.com/%{name}/%{version}/%{name}_%{version}_linux_amd64.zip

%description

Terraform is a tool for building, changing, and versioning infrastructure 
safely and efficiently. Terraform can manage existing and popular service 
providers as well as custom in-house solutions.

%prep
unzip %{SOURCE0}

%install
install -D -m 755 %{name} %{buildroot}/usr/local/bin/%{name}

%files
/usr/local/bin/%{name}