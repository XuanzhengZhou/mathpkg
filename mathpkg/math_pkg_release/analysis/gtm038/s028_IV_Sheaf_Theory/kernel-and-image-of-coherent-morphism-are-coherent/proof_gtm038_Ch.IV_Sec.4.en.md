---
role: proof
locale: en
of_concept: kernel-and-image-of-coherent-morphism-are-coherent
source_book: gtm038
source_chapter: "IV"
source_section: "4. Coherent Sheaves"
---

**Proof.**

**Kernel:** The sequence
$$
0 \longrightarrow \operatorname{Ker}\varphi \longrightarrow \mathcal{S}_1 \xrightarrow{\varphi} \mathcal{S}_2
$$
is exact. Since $\mathcal{S}_1$ and $\mathcal{S}_2$ are coherent, one can show (by an argument similar to the proof of Theorem 4.3) that $\operatorname{Ker}\varphi$ is coherent.

**Image:** By Theorem 3.2 (First Isomorphism Theorem for Sheaves),
$$
\operatorname{Im}\varphi \simeq \mathcal{S}_1 / \operatorname{Ker}\varphi.
$$
Since $\mathcal{S}_1$ is coherent and $\operatorname{Ker}\varphi$ is a coherent subsheaf (as shown above), Theorem 4.6(1) implies that $\mathcal{S}_1/\operatorname{Ker}\varphi$ is coherent. Hence $\operatorname{Im}\varphi$ is coherent. $\square$
