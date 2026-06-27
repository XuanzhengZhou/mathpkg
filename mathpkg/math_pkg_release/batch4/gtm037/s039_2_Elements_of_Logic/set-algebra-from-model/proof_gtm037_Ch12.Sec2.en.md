---
role: proof
locale: en
of_concept: set-algebra-from-model
source_book: gtm037
source_chapter: "12"
source_section: "2"
---

The statement of Proposition 12.24 is truncated in the extracted section text, and no proof is present. The typical argument proceeds as follows: For a model $\mathfrak{A}$ of $\Gamma$, the set $\{\varphi^\mathfrak{A} : \varphi \in \mathrm{Fmla}_\mathcal{L}\}$ of $\omega$-ary relations definable in $\mathfrak{A}$ forms a field of sets because $\varphi^\mathfrak{A} \cap \psi^\mathfrak{A} = (\varphi \wedge \psi)^\mathfrak{A}$, the complement is $(\neg\varphi)^\mathfrak{A}$, etc. Diagonal elements are interpreted as $d_{\kappa\lambda}^\mathfrak{A} = \{(a_i)_{i \in \omega} : a_\kappa = a_\lambda\}$, and cylindrifications as $c_\kappa(\varphi^\mathfrak{A}) = \{(a_i) : \exists b \; (a_i)_{i \neq \kappa} \cup \{(\kappa, b)\} \in \varphi^\mathfrak{A}\}$. The map $f([\varphi]) = \varphi^\mathfrak{A}$ is well-defined because if $\Gamma \vdash \varphi \leftrightarrow \psi$ then $\varphi^\mathfrak{A} = \psi^\mathfrak{A}$, and it preserves all operations by the definition of satisfaction in $\mathfrak{A}$.
