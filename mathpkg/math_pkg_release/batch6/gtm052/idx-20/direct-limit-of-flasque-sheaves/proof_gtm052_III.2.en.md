---
role: proof
locale: en
of_concept: direct-limit-of-flasque-sheaves
source_book: gtm052
source_chapter: "III"
source_section: "§2 Cohomology of Sheaves"
---

Let $(\mathcal{F}_\alpha)$ be a directed system of flasque sheaves. Then for any inclusion of open sets $V \subseteq U$, and for each $\alpha$, we have $\mathcal{F}_\alpha(U) \to \mathcal{F}_\alpha(V)$ is surjective. Since $\varinjlim$ is an exact functor, we get

$$\varinjlim \mathcal{F}_\alpha(U) \to \varinjlim \mathcal{F}_\alpha(V)$$

is also surjective. But on a noetherian topological space, $\varinjlim \mathcal{F}_\alpha(U) = (\varinjlim \mathcal{F}_\alpha)(U)$ for any open set (II, Ex. 1.11). So we have

$$(\varinjlim \mathcal{F}_\alpha)(U) \to (\varinjlim \mathcal{F}_\alpha)(V)$$

is surjective, and so $\varinjlim \mathcal{F}_\alpha$ is flasque.
