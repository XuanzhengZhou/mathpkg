---
role: proof
locale: en
of_concept: existence-of-representing-chain
source_book: gtm040
source_chapter: "9"
source_section: "10"
---

We first prove uniqueness. Let $P$ represent the circuit. Let $i$ and $j$ be any two distinct states, and let $E = \{j\}$ and $F = \{i, j\}$. Put a unit voltage at $j$ and ground $\tilde{F}$. Then by Kirchhoff's Law,
$$\sum_k (v_i - v_k) c_{ik} = 0.$$
Since $v_k = 0$ except when $k$ is $i$ or $j$ and since $c_{ii} = 0$, we have $v_i \sum_k c_{ik} = c_{ij}$, hence $v_i = c_{ij} / \sum_k c_{ik}$. Since $P$ represents the circuit, $v_i = P_{ij} v_j = P_{ij}$. Thus $P$ is unique.

For existence, define $P_{ij} = c_{ij} / \sum_k c_{ik}$. Then $P_{ij} \geq 0$, $P_{ii} = 0$, and $\sum_j P_{ij} = 1$, so $P$ is a transition matrix. Let $E$ and $F$ be finite sets with $E \subset F$, let $v_E$ be specified, and $v_{\tilde{F}} = 0$. Define $v = B^{E \cup \tilde{F}} \binom{v_E}{v_{\tilde{F}}}$. Then $v$ is regular on $F - E$ and solves the standard voltage problem.
