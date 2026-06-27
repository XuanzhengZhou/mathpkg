---
role: proof
locale: en
of_concept: characterization-of-nuclear-spaces
source_book: gtm003
source_chapter: "III"
source_section: "7"
---

(a) $\Rightarrow$ (b): Let $F$ be any Banach space and $u \in \mathcal{L}(E, F)$. There exists a convex, circled $0$-neighborhood $V$ in $E$ such that $\phi_V: E \to \tilde{E}_V$ is nuclear and $u(V)$ is bounded in $F$. Since $\phi_V(E) = E_V$ is dense in $\tilde{E}_V$, $u$ determines a unique $v \in \mathcal{L}(\tilde{E}_V, F)$ such that $u = v \circ \phi_V$. By Corollary 2 of (7.1), the composition of the nuclear map $\phi_V$ with $v$ is nuclear, so $u$ is nuclear.

(b) $\Rightarrow$ (c): Let $U$ be any convex, circled $0$-neighborhood. By assumption the canonical map $\phi_U: E \to \tilde{E}_U$ is nuclear, hence admits a representation $\phi_U = \sum \lambda_n f_n \otimes y_n$ as in (7.1). Set $V = U \cap \{x : |f_n(x)| \leq 1, n \in \mathbb{N}\}$; then $V \subset U$ is a convex, circled $0$-neighborhood by equicontinuity of $\{f_n\}$. Each $f_n$ induces a continuous linear form of norm $\leq 1$ on $E_V$, and its continuous extension $h_n$ to $\tilde{E}_V$ yields $\phi_{U,V}: \tilde{E}_V \to \tilde{E}_U$ given by $\sum \lambda_n h_n \otimes y_n$, which is nuclear.

(c) $\Rightarrow$ (a): Given a convex, circled $0$-neighborhood $U$, choose $V$ such that $\phi_{U,V}$ is nuclear. Then $\phi_U = \phi_{U,V} \circ \phi_V$ is nuclear by Corollary 2 of (7.1).
