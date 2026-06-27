---
role: proof
locale: en
of_concept: necessary-condition-for-almost-sure-convergence
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Necessary and Sufficient Condition for Almost Sure Convergence

**Theorem 1.** (a) A necessary and sufficient condition that $\xi_n \to \xi$ (P-a.s.) is that

$$P\left\{ \sup_{k \geq n} |\xi_k - \xi| \geq \varepsilon \right\} \to 0, \quad n \to \infty,$$

for every $\varepsilon > 0$.

(b) The sequence $\{\xi_n\}_{n \geq 1}$ is fundamental with probability 1 if and only if

$$P\left\{ \sup_{k \geq n, l \geq n} |\xi_k - \xi_l| \geq \varepsilon \right\} \to 0, \quad n \to \infty,$$

for every $\varepsilon > 0$; or equivalently

$$P\left\{ \sup_{k \geq 0} |\xi_{n+k} - \xi_n| \geq \varepsilon \right\} \to 0, \quad n \to \infty.$$

*Proof.* (a) Let $A_n^\varepsilon = \{\omega : |\xi_n - \xi| \geq \varepsilon\}$, $A^\varepsilon = \limsup_n A_n^\varepsilon \equiv \bigcap_{n=1}^{\infty} \bigcup_{k \geq n} A_k^\varepsilon$. Then

$$\{\omega : \xi_n \not\to \xi\} = \bigcup_{\varepsilon > 0} A^\varepsilon = \bigcup_{m=1}^{\infty} A^{1/m}.$$

But

$$P(A^\varepsilon) = \lim_{n} P\left( \bigcup_{k \geq n} A_k^\varepsilon \right),$$

hence $P(A^\varepsilon) = 0$ if and only if $\lim_n P(\bigcup_{k \geq n} A_k^\varepsilon) = 0$. But $\bigcup_{k \geq n} A_k^\varepsilon = \{\sup_{k \geq n} |\xi_k - \xi| \geq \varepsilon\}$. Therefore the condition $P\{\sup_{k \geq n} |\xi_k - \xi| \geq \varepsilon\} \to 0$, $\varepsilon > 0$, is equivalent to $P(A^\varepsilon) = 0$ for all $\varepsilon > 0$, i.e., $\xi_n \to \xi$ (P-a.s.).

(b) Let $B_n^\varepsilon = \{\omega : \sup_{k \geq n, l \geq n} |\xi_k - \xi_l| \geq \varepsilon\}$. Then

$$\{\omega : \{\xi_n(\omega)\}_{n \geq 1} \text{ is not fundamental}\} = \bigcup_{\varepsilon > 0} B^\varepsilon,$$

where $B^\varepsilon = \limsup B_n^\varepsilon$. It can be shown as in (a) that

$$P\{\omega : \{\xi_n(\omega)\}_{n \geq 1} \text{ is not fundamental}\} = 0 \Leftrightarrow (6).$$

The equivalence of (6) and (7) follows from the obvious inequalities

$$\sup_{k \geq 0} |\xi_{n+k} - \xi_n| \leq \sup_{k \geq 0, l \geq 0} |\xi_{n+k} - \xi_{n+l}| \leq 2 \sup_{k \geq 0} |\xi_{n+k} - \xi_n|.$$

This completes the proof of the theorem. $\square$
