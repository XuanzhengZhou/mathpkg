---
role: proof
locale: en
of_concept: elementary-embedding-into-ultrapower
source_book: gtm053
source_chapter: "2"
source_section: "2.12"
---

Define the diagonal embedding $d : \mathbf{A} \to \mathbf{A}^I / U$ by
$$d(a) = [(a, a, a, \ldots)_{i \in I}]_U,$$
the equivalence class of the constant sequence with value $a$.

Let $\varphi(x_1, \ldots, x_n)$ be any $L$-formula and let $a_1, \ldots, a_n \in A$. By Łoś's theorem,
$$\mathbf{A}^I / U \vDash \varphi(d(a_1), \ldots, d(a_n)) \iff \{i \in I : \mathbf{A} \vDash \varphi(a_1, \ldots, a_n)\} \in U.$$

The set on the right-hand side is either all of $I$ (if $\mathbf{A} \vDash \varphi(a_1, \ldots, a_n)$) or the empty set $\varnothing$ (if $\mathbf{A} \vDash \neg \varphi(a_1, \ldots, a_n)$). Since $U$ is a nonprincipal ultrafilter on $I$, we have $I \in U$ and $\varnothing \notin U$. Therefore,
$$\mathbf{A}^I / U \vDash \varphi(d(a_1), \ldots, d(a_n)) \iff \mathbf{A} \vDash \varphi(a_1, \ldots, a_n).$$

This shows that $d$ is an elementary embedding, and consequently $\mathbf{A} \prec \mathbf{A}^I / U$.
