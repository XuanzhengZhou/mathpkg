---
role: proof
locale: en
of_concept: uniform-integrability
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Theorem 5 (Uniform Integrability Characterization)

**Theorem 5.** Let $0 \leq \xi_n \to \xi$ (P-a.s.) and $E\xi_n < \infty$, $n \geq 1$. Then $E\xi_n \to E\xi < \infty$ if and only if the family $\{\xi_n\}_{n \geq 1}$ is uniformly integrable.

*Proof.* **Sufficiency.** Follows from conclusion (b) of Theorem 4.

**Necessity.** Consider the (at most countable) set

$$A = \{a : P(\xi = a) > 0\}.$$

Then we have $\xi_n I_{\{\xi_n < a\}} \to \xi I_{\{\xi < a\}}$ for each $a \notin A$, and the family $\{\xi_n I_{\{\xi_n < a\}}\}_{n \geq 1}$ is uniformly integrable. Hence, by the sufficiency part, $E\xi_n I_{\{\xi_n < a\}} \to E\xi I_{\{\xi < a\}}$ for $a \notin A$, and therefore

$$E\xi_n I_{\{\xi_n \geq a\}} \to E\xi I_{\{\xi \geq a\}}, \quad a \notin A, \; n \to \infty. \tag{15}$$

Take $\varepsilon > 0$ and choose $a_0 \notin A$ so large that $E\xi I_{\{\xi \geq a_0\}} < \varepsilon/2$; then choose $N_0$ so large that

$$E\xi_n I_{\{\xi_n \geq a_0\}} \leq E\xi I_{\{\xi \geq a_0\}} + \varepsilon/2$$

for all $n \geq N_0$, and consequently $E\xi_n I_{\{\xi_n \geq a_0\}} \leq \varepsilon$. Then choose $a_1 \geq a_0$ so large that $E\xi_n I_{\{\xi_n \geq a_1\}} \leq \varepsilon$ for all $n \leq N_0$. Thus for all $n \geq 1$, $E\xi_n I_{\{\xi_n \geq a_1\}} \leq \varepsilon$, establishing uniform integrability. $\square$
