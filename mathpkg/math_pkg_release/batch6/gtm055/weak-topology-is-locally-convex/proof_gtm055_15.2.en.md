---
role: proof
locale: en
of_concept: weak-topology-is-locally-convex
source_book: gtm055
source_chapter: "15"
source_section: "2"
---

The weak topology on $\mathcal{E}$ coincides with the (linear) topology induced by the family of pseudonorms $\{\sigma_f\}_{f \in \mathcal{E}^*}$, and is therefore locally convex. The subbasic neighborhood $U(f_1; \varepsilon) \cap \dots \cap U(f_n; \varepsilon)$ is the intersection of the open balls with center $0$ and radius $\varepsilon$ with respect to the pseudometrics defined by the pseudonorms $\sigma_{f_1}, \dots, \sigma_{f_n}$. Hence each set in the neighborhood base is a weakly open neighborhood of $0$. Conversely, if $U$ is any weakly open subset containing $0$, then there exist $f_1, \dots, f_n \in \mathcal{E}^*$ and positive radii $\varepsilon_1, \dots, \varepsilon_n$ such that $U(f_1; \varepsilon_1) \cap \dots \cap U(f_n; \varepsilon_n) \subset U$ (Ex. 3M), and hence $U(f_1, \dots, f_n; \varepsilon_1 \wedge \dots \wedge \varepsilon_n) \subset U$. Separation follows from the Hahn-Banach theorem. For finite dimensions, the weak and norm topologies coincide; for infinite dimensions, they differ.
