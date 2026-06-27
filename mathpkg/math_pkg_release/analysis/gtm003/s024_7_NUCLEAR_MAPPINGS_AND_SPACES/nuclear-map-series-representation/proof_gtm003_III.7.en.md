---
role: proof
locale: en
of_concept: nuclear-map-series-representation
source_book: gtm003
source_chapter: "III"
source_section: "7. Nuclear Mappings and Spaces"
---

**Necessity.** If $u$ is nuclear, then by definition $u = \psi_B \circ \bar{u}_0 \circ \phi_U$, where $\bar{u}_0$ is a nuclear map in $\mathcal{L}(\tilde{E}_U, F_B)$, with $U$ a suitable $0$-neighborhood in $E$ and $B$ a suitable bounded subset of $F$ such that $F_B$ is complete. Hence $\bar{u}_0$ originates from an element $v$ of $[\tilde{E}_U]' \hat{\otimes} F_B$, which is, by (6.4), of the form

$$v = \sum_{n=1}^{\infty} \lambda_n h_n \otimes y_n$$

with $\sum_{n=1}^{\infty} |\lambda_n| < +\infty$ and where $\{h_n\}$ and $\{y_n\}$ are null sequences in $[\tilde{E}_U]'$ and $F_B$, respectively.

Define a sequence $\{f_n\}$ of linear forms on $E$ by $f_n = h_n \circ \phi_U$. Since $\{h_n\}$ is a bounded sequence in $[\tilde{E}_U]'$, the sequence $\{f_n\}$ is uniformly bounded on $U$ and hence is equicontinuous. It follows that the mapping

$$u = \psi_B \circ \tau(v) \circ \phi_U$$

is of the form $x \mapsto \sum_{n=1}^{\infty} \lambda_n f_n(x) y_n$, where $\tau: [\tilde{E}_U]' \hat{\otimes} F_B \to \mathcal{L}(\tilde{E}_U, F_B)$ is the canonical map.

**Sufficiency.** If $u$ is of the series form as indicated, let

$$U = \{x \in E : |f_n(x)| \leq 1,\ n \in \mathbb{N}\},$$

which is a convex, circled $0$-neighborhood by the equicontinuity of $\{f_n\}$. The image $u(U)$ of this $0$-neighborhood $U$ is contained in the closed, convex, circled hull $C$ of the null sequence $\{y_n\}$ in $F_B$. Since $\{y_n\}$ is relatively compact in $F_B$ and $F_B$ is complete, $C$ is compact in $F_B$ (cf. (I, 5.2) and (II, 4.3)), and hence a fortiori compact in $F$ by the continuity of the canonical imbedding $F_B \to F$. Consequently, $u$ maps the factorization through $\tilde{E}_U$ and $F_B$, so $u$ is nuclear by definition.
