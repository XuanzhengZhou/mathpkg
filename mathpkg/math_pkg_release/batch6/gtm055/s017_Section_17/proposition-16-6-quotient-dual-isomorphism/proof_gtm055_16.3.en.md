---
role: proof
locale: en
of_concept: proposition-16-6-quotient-dual-isomorphism
source_book: gtm055
source_chapter: "16"
source_section: "16.3"
---

A linear functional $f \in \mathcal{E}^*$ can be factored through $\mathcal{E}/\mathcal{M}$ if and only if $\mathcal{M} \subset \ker f$, i.e., $f \in \mathcal{M}^a$. If $f \in \mathcal{M}^a$ and $\hat{f}$ is the unique linear functional on $\mathcal{E}/\mathcal{M}$ such that $f = \hat{f} \circ \pi$, then $\hat{f}$ is continuous since $\pi$ is an open mapping. Conversely, if $\hat{f} \in (\mathcal{E}/\mathcal{M})^*$, then $f = \hat{f} \circ \pi \in \mathcal{M}^a$. Thus $\alpha(\hat{f}) = \hat{f} \circ \pi$ defines a bijection from $(\mathcal{E}/\mathcal{M})^*$ onto $\mathcal{M}^a$, and linearity is clear.

In the Banach space case, $\|\alpha(\hat{f})\| = \|\hat{f} \circ \pi\| \leq \|\hat{f}\| \|\pi\| = \|\hat{f}\|$ since $\|\pi\| = 1$. Conversely, $\|\hat{f}\| = \sup_{\|\pi(x)\| < 1} |\hat{f}(\pi(x))| = \sup_{\|x + \mathcal{M}\| < 1} |f(x)| \leq \sup_{\|x\| < 1} |f(x)| = \|f\|$, giving $\|\alpha(\hat{f})\| = \|\hat{f}\|$, so $\alpha$ is an isometry.
