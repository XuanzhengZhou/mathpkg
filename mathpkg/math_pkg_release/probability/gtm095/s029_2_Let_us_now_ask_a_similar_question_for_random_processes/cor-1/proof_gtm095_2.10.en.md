---
role: proof
locale: en
of_concept: cor-1
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Corollary 1: Borel--Cantelli Implication for Almost Sure Convergence

**Corollary 1.** If $A_n^\varepsilon = \{\omega : |\xi_n - \xi| \geq \varepsilon\}$ then the condition

$$\sum_{n=1}^{\infty} P(A_n^\varepsilon) < \infty, \quad \varepsilon > 0,$$

implies, by the Borel--Cantelli lemma, that $P(A^\varepsilon) = 0$, $\varepsilon > 0$, where $A^\varepsilon = \limsup A_n^\varepsilon = \{A_n^\varepsilon \text{ i.o.}\}$. Therefore

$$\sum_{k=1}^{\infty} P\{|\xi_k - \xi| \geq \varepsilon\} < \infty, \quad \varepsilon > 0 \;\Rightarrow\; P(A^\varepsilon) = 0, \quad \varepsilon > 0$$

$$\Leftrightarrow\; P\{\omega : \xi_n \not\to \xi\} = 0.$$

*Proof.* This is a direct application of the Borel--Cantelli Lemma part (a) to the events $A_n^\varepsilon$. The equivalence $P(A^\varepsilon) = 0$ for all $\varepsilon > 0 \Leftrightarrow \xi_n \to \xi$ (P-a.s.) was established in the proof of Theorem 1. $\square$
