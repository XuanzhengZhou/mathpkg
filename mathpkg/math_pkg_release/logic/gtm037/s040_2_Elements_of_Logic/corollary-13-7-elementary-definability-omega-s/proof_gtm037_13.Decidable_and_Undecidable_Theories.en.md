---
role: proof
locale: en
of_concept: corollary-13-7-elementary-definability-omega-s
source_book: gtm037
source_chapter: "13"
source_section: "Decidable and Undecidable Theories"
---

First we treat $(\omega, s, 0)$.

($\Rightarrow$). Suppose $\varphi$ elementarily defines $A$. Thus $\operatorname{Fv}\varphi \subseteq \{v_0\}$ and $$^{1}\varphi^{2\mathfrak{A}} = A,$$ where $\mathfrak{A} = (\omega, s, 0)$. By Theorem 13.4 let $\psi$ be a quantifier-free combination of basic formulas equivalent under $\Gamma_1$ to $\varphi$ with $\operatorname{Fv}\psi \subseteq \{v_0\}$. Thus $\psi$ also elementarily defines $A$. Now $\psi$ is built up from formulas $\mathbf{O} = \mathbf{O}$, $s^m v_0 = n$ using $\neg, \wedge, \vee$. Note that $s^m v_0 = n$ elementarily defines $0$ if $m > n$, and $\{n - m\}$ if $m \leq n$. Thus $A$ is built up from sets $\omega, \emptyset, \{p\}$ using $\sim, \cap, \cup$. Hence $A$ is finite or cofinite.

($\Leftarrow$). The converse is trivial: finite sets are defined by disjunctions of equations, and cofinite sets are negations of finite-set definitions.

To treat the structure $(\omega, s)$ it is enough to note that if $\varphi$ elementarily defines $A$ in $(\omega, s)$, then it also does in $(\omega, s, 0)$ and hence $A$ is finite or cofinite. Conversely, any finite or cofinite set is elementarily definable in $(\omega, s)$ using the successor function alone.
