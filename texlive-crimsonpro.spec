%global tl_name crimsonpro
%global tl_revision 78931

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	CrimsonPro fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/crimsonpro
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crimsonpro.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/crimsonpro.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The CrimsonPro fonts are designed by Jacques Le Bailly and derived from
the Crimson Text fonts designed by Sebastian Kosch. The family includes
eight weights and italics for each weight.

