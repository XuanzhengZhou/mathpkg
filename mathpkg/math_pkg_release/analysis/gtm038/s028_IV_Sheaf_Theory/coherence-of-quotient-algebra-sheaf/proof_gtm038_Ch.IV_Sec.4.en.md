---
role: proof
locale: en
of_concept: coherence-of-quotient-algebra-sheaf
source_book: gtm038
source_chapter: "IV"
source_section: "4. Coherent Sheaves"
---

**Proof.** We already know that $\mathcal{R}/\mathcal{I}$ is coherent as a sheaf of $\mathcal{R}$-modules (by Theorem 4.6). To prove coherence as a sheaf of $\mathbb{C}$-algebras, we must show that for any $(\mathcal{R}/\mathcal{I})$-homomorphism $\varphi: q(\mathcal{R}/\mathcal{I})|U \to (\mathcal{R}/\mathcal{I})|U$, the kernel is finitely generated as an $(\mathcal{R}/\mathcal{I})$-module.

Let $\pi: \mathcal{R} \to \mathcal{R}/\mathcal{I}$ be the canonical projection, and let $\pi_q: q\mathcal{R} \to q(\mathcal{R}/\mathcal{I})$ be the induced map on free sheaves. Define $\psi := \varphi \circ \pi_q: q\mathcal{R}|U \to (\mathcal{R}/\mathcal{I})|U$.

Since $\psi$ is an $\mathcal{R}$-homomorphism, the coherence of $\mathcal{R}$ (as an $\mathcal{R}$-module) implies that for each $\mathfrak{z}_0 \in U$, there exists a neighborhood $V(\mathfrak{z}_0) \subset U$ and sections $s_1, \ldots, s_p \in \Gamma(V, \operatorname{Ker}\psi)$ which generate $\operatorname{Ker}\psi$ over $V$ as an $\mathcal{R}$-module.

Define $\tilde{s}_i := \pi_q(s_i) \in \Gamma(V, q(\mathcal{R}/\mathcal{I}))$. Then $\varphi(\tilde{s}_i) = \varphi \circ \pi_q(s_i) = \psi(s_i) = 0$, so $\tilde{s}_i \in \Gamma(V, \operatorname{Ker}\varphi)$. One verifies that $\tilde{s}_1, \ldots, \tilde{s}_p$ generate $\operatorname{Ker}\varphi$ over $V$ as an $(\mathcal{R}/\mathcal{I})$-module, establishing coherence. $\square$
