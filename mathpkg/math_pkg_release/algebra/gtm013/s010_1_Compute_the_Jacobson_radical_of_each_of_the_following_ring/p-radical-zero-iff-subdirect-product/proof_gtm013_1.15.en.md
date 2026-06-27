---
role: proof
locale: en
of_concept: p-radical-zero-iff-subdirect-product
source_book: gtm013
source_chapter: "1"
source_section: "15"
---

$(\Rightarrow)$ Suppose $\operatorname{rad}_{\mathcal{P}}(R) = 0$. For each $r \in R$ with $r \neq 0$, there exists a homomorphism $\varphi_r: R \to P_r$ with $P_r \in \mathcal{P}$ such that $\varphi_r(r) \neq 0$ (otherwise $r$ would lie in all kernels and hence in the radical). The product map $\prod \varphi_r: R \to \prod P_r$ has kernel $\bigcap \ker \varphi_r = \operatorname{rad}_{\mathcal{P}}(R) = 0$, so it is injective. Thus $R$ is isomorphic to a subdirect product of the $P_r \in \mathcal{P}$.

$(\Leftarrow)$ Suppose $R$ is a subdirect product of rings $P_\alpha \in \mathcal{P}$, so there is an embedding $\iota: R \hookrightarrow \prod P_\alpha$ such that each projection $\pi_\alpha \circ \iota: R \to P_\alpha$ is surjective. Then $\operatorname{rad}_{\mathcal{P}}(R) \subseteq \bigcap \ker(\pi_\alpha \circ \iota) = \ker \iota = 0$, so $\operatorname{rad}_{\mathcal{P}}(R) = 0$.
