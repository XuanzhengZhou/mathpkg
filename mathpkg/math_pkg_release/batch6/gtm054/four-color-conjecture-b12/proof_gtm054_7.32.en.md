---
role: proof
locale: en
of_concept: four-color-conjecture-b12
source_book: gtm054
source_chapter: "7"
source_section: "Section 32"
---

Suppose that $\chi_0(\Theta) \leq 4$ for every planar graph $\Theta$ which admits a triangular imbedding. Were there to exist a planar graph with vertex chromatic number 5, consider a 5-critical subgraph $\Gamma = (V, \mathcal{E})$ of it, and let $\{Z_1, \ldots, Z_m\}$ be a planar imbedding of $\Gamma$.

By A17, $\Gamma$ is biconnected. Hence by IIIB3 and IIIE9 each region $Z_i$ is an elementary cycle, and so by IIIA9, $Z_i$ induces an elementary circuit

$$x_{i,0}, E_{i,1}, x_{i,1}, E_{i,2}, \ldots, E_{i,q_i}, x_{i,q_i} = x_{i,0}$$

in $\Gamma$ for each $i = 1, \ldots, m$. Let $y_1, \ldots, y_m$ be $m$ distinct objects not in $V$ and define

$$U = V \cup \{y_1, \ldots, y_m\},$$

$$\mathcal{F} = \mathcal{E} \cup \{\{x_{i,j}, y_i\}: j = 1, \ldots, q_i; i = 1, \ldots, m\},$$

and

$$\Omega = (U, \mathcal{F}).$$

Since $\Gamma = \Omega_V$, it suffices to prove that $\Omega$ admits a triangular imbedding.

We define

$$Z_{i,j} = \{E_{i,j+1}, \{x_{i,j+1}, y_i
