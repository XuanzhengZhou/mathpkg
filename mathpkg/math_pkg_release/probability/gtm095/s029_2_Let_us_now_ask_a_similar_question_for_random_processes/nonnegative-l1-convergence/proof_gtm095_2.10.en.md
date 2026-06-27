---
role: proof
locale: en
of_concept: nonnegative-l1-convergence
source_book: gtm095
source_chapter: "2"
source_section: "10"
---

# Proof of Almost Sure Convergence Plus Convergence of Expectations Implies $L^1$ Convergence

**Theorem 3.** Let $(\xi_n)$ be a sequence of nonnegative random variables such that $\xi_n \xrightarrow{\text{a.s.}} \xi$ and $E\xi_n \to E\xi < \infty$. Then

$$E|\xi_n - \xi| \to 0, \quad n \to \infty.$$

*Proof.* We have $E\xi_n < \infty$ for sufficiently large $n$, and therefore for such $n$ we have

$$E|\xi - \xi_n| = E(\xi - \xi_n)I_{\{\xi \geq \xi_n\}} + E(\xi_n - \xi)I_{\{\xi_n > \xi\}}$$

$$= 2E(\xi - \xi_n)I_{\{\xi \geq \xi_n\}} + E(\xi_n - \xi).$$

But $0 \leq (\xi - \xi_n)I_{\{\xi \geq \xi_n\}} \leq \xi$, and by the dominated convergence theorem (since $\xi_n \xrightarrow{\text{a.s.}} \xi$),

$$E(\xi - \xi_n)I_{\{\xi \geq \xi_n\}} \to 0, \quad n \to \infty.$$

Also $E(\xi_n - \xi) = E\xi_n - E\xi \to 0$ by hypothesis. Hence $E|\xi - \xi_n| \to 0$ as $n \to \infty$. $\square$
