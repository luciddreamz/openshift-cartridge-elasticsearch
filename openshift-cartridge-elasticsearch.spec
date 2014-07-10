%global cartridgedir %{_libexecdir}/openshift/cartridges/elasticsearch

Summary:       Provides Elasticsearch support
Name:          openshift-cartridge-elasticsearch
Version:       1.0.0
Release:       1%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://www.elasticsearch.org
Source0:       %{name}-%{version}.tar.gz
Requires:      java-1.7.0-openjdk
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-cartridge-elasticsearch-1.2 = 1.0.0
BuildArch:     noarch

%description
Provides Elasticsearch cartridge support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}/env
%{cartridgedir}/lib
%{cartridgedir}/logs
%{cartridgedir}/metadata
%{cartridgedir}/template
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/README_pt.md
%doc %{cartridgedir}/LICENSE.txt

%changelog