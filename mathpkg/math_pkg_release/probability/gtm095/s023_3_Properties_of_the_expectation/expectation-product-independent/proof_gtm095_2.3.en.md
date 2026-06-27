---
role: proof
locale: en
of_concept: expectation-product-independent
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof that Expectation of Product of Independent Random Variables Factorizes

**Theorem.** Let $\xi$ and $\eta$ be independent random variables with $E|\xi| < \infty$ and $E|\eta| < \infty$. Then $E|\xi\eta| < \infty$ and

$$E[\xi\eta] = E\xi \cdot E\eta.$$

*Proof.* First consider $\xi \geq 0$, $\eta \geq 0$. Discretize them by

$$\xi_n = \sum_{k=0}^{\infty} \frac{k}{n} I_{\{k/n \leq \xi < (k+1)/n\}}, \quad \eta_n = \sum_{k=0}^{\infty} \frac{k}{n} I_{\{k/n \leq \eta < (k+1)/n\}}.$$

Then $\xi_n \leq \xi$, $|\xi_n - \xi| \leq 1/n$, $\eta_n \leq \eta$, $|\eta_n - \eta| \leq 1/n$. By dominated convergence, $E\xi_n \to E\xi$ and $E\eta_n \to E\eta$.

By independence, for any $k, l$,

$$E[I_{\{k/n \leq \xi < (k+1)/n\}} I_{\{l/n \leq \eta < (l+1)/n\}}] = P(k/n \leq \xi < (k+1)/n) \cdot P(l/n \leq \eta < (l+1)/n).$$

Hence $E[\xi_n\eta_n] = E\xi_n \cdot E\eta_n$. Since $|E\xi\eta - E\xi_n\eta_n| \leq E[\xi|\eta - \eta_n|] + E[\eta_n|\xi - \xi_n|] \leq \frac{1}{n}(E\xi + E\eta) \to 0$, we obtain $E\xi\eta = \lim E\xi_n\eta_n = E\xi \cdot E\eta$.

The general case follows by decomposing $\xi = \xi^+ - \xi^-$, $\eta = \eta^+ - \eta^-$ and using independence. $\square$
