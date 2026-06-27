---
role: proof
locale: en
of_concept: nuclear-space-equivalent-conditions
source_book: gtm003
source_chapter: "III"
source_section: "7. Nuclear Mappings and Spaces"
---

**(a) $\Rightarrow$ (b).** Let $F$ be any Banach space and $u \in \mathcal{L}(E, F)$. There exists a convex, circled $0$-neighborhood $V$ in $E$ such that $\phi_V: E \to \tilde{E}_V$ is nuclear (by (a)) and such that $u(V)$ is bounded in $F$. Since $\phi_V(E) = E_V$, the map $u$ determines a unique $v \in \mathcal{L}(\tilde{E}_V, F)$ such that $u = v \circ \phi_V$. By Corollary 2 of (7.1), the composition of the nuclear map $\phi_V$ with the continuous map $v$ is nuclear; hence $u$ is nuclear.

**(b) $\Rightarrow$ (c).** Let $U$ be any convex, circled $0$-neighborhood in $E$. By assumption (b), the canonical map $\phi_U: E \to \tilde{E}_U$ is nuclear, and hence by (7.1) is of the form $\phi_U(x) = \sum_{n=1}^{\infty} \lambda_n f_n(x) y_n$ with $\sum |\lambda_n| < +\infty$, $\{f_n\}$ equicontinuous in $E'$, and $\{y_n\}$ bounded in $\tilde{E}_U$. Set
$$V = U \cap \{x \in E : |f_n(x)| \leq 1,\ n \in \mathbb{N}\}.$$
Then $V \subset U$ is convex, circled, and a $0$-neighborhood by equicontinuity of $\{f_n\}$. Each $f_n$ induces a continuous linear form of norm $\leq 1$ on $E_V$; let $h_n$ be its continuous extension to $\tilde{E}_V$. The canonical map $\phi_{U,V}: \tilde{E}_V \to \tilde{E}_U$ is then given by
$$\phi_{U,V} = \sum_{n=1}^{\infty} \lambda_n h_n \otimes y_n,$$
which is nuclear by the series characterization of (7.1).

**(c) $\Rightarrow$ (a).** If $U$ is a given convex, circled $0$-neighborhood in $E$, by (c) there exists $V \subset U$ such that $\phi_{U,V}: \tilde{E}_V \to \tilde{E}_U$ is nuclear. Since $\phi_U = \phi_{U,V} \circ \phi_V$ and $\phi_V: E \to \tilde{E}_V$ is the canonical map, applying (c) again or directly using that $\phi_V$ is continuous (and can be made nuclear through the same argument by nesting neighborhoods), one shows $\phi_U$ is nuclear. Hence $E$ is nuclear by definition (a).
