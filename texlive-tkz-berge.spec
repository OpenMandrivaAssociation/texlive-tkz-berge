%global tl_name tkz-berge
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Macros for drawing graphs of graph theory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-berge
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-berge.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-berge.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a collection of useful macros for drawing classic
graphs of graph theory, or to make other graphs. This package has been
taken temporarily out of circulation to give the author time to
investigate some problems.

