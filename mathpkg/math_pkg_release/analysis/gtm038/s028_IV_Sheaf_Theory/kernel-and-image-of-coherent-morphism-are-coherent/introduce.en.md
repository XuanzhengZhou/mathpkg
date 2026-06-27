---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

**Theorem 4.7** states that for a morphism $\varphi: \mathcal{S}_1 \to \mathcal{S}_2$ between coherent sheaves, both the kernel and image are coherent sheaves.

The proof for the kernel uses the exact sequence $0 \to \operatorname{Ker}\varphi \to \mathcal{S}_1 \to \mathcal{S}_2$, noting that $\mathcal{S}_1$ is coherent (as a subsheaf of a coherent sheaf, $\operatorname{Ker}\varphi$ inherits coherence by an argument similar to Theorem 4.3).

For the image, the first isomorphism theorem (Theorem 3.2) gives $\operatorname{Im}\varphi \simeq \mathcal{S}_1/\operatorname{Ker}\varphi$. Since $\operatorname{Ker}\varphi$ is coherent and $\mathcal{S}_1$ is coherent, Theorem 4.6(1) implies $\mathcal{S}_1/\operatorname{Ker}\varphi$ is coherent, hence $\operatorname{Im}\varphi$ is coherent.

This theorem completes the proof that the category of coherent sheaves is an abelian subcategory of the category of analytic sheaves.
