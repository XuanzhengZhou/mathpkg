---
role: proof
locale: en
of_concept: cor-2-1
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Corollary 2: Fast Convergence in Probability Implies Almost Sure Convergence

**Corollary 2.** Let $(\varepsilon_n)_{n \geq 1}$ be a sequence of positive numbers such that $\varepsilon_n \downarrow 0$, $n \to \infty$. If $\xi_n$ converges to $\xi$ in probability sufficiently "fast" in the sense that

$$\sum_{n=1}^{\infty} P\{|\xi_n - \xi| \geq \varepsilon_n\} < \infty,$$

then $\xi_n \to \xi$ (P-a.s.).

*Proof.* Apply Corollary 1. For each fixed $\varepsilon > 0$, choose $N$ such that $\varepsilon_n \leq \varepsilon$ for all $n \geq N$. Then

$$\{|\xi_n - \xi| \geq \varepsilon\} \subseteq \{|\xi_n - \xi| \geq \varepsilon_n\}, \quad n \geq N.$$

Hence $\sum_{n=N}^{\infty} P\{|\xi_n - \xi| \geq \varepsilon\} \leq \sum_{n=N}^{\infty} P\{|\xi_n - \xi| \geq \varepsilon_n\} < \infty$, and the result follows from Corollary 1. $\square$
