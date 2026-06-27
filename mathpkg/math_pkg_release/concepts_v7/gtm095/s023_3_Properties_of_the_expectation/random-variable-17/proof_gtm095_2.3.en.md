---
role: proof
locale: en
of_concept: random-variable-17
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Theorem 6 (Expectation of Product of Independent Random Variables)

**Theorem 6.** Let $\xi$ and $\eta$ be independent random variables, $E|\xi| < \infty$, $E|\eta| < \infty$. Then $E|\xi\eta| < \infty$ and

$$E\xi\eta = E\xi \cdot E\eta. \tag{20}$$

*Proof.* First let $\xi \geq 0$, $\eta \geq 0$. Put

$$\xi_n = \sum_{k=0}^{\infty} \frac{k}{n} I_{\{k/n \leq \xi(\omega) < (k+1)/n\}},$$
$$\eta_n = \sum_{k=0}^{\infty} \frac{k}{n} I_{\{k/n \leq \eta(\omega) < (k+1)/n\}}.$$

Then $\xi_n \leq \xi$, $|\xi_n - \xi| \leq 1/n$ and $\eta_n \leq \eta$, $|\eta_n - \eta| \leq 1/n$. Since $E\xi < \infty$ and $E\eta < \infty$, it follows from Lebesgue's dominated convergence theorem that

$$\lim_n E\xi_n = E\xi, \quad \lim_n E\eta_n = E\eta.$$

Moreover, since $\xi$ and $\eta$ are independent,

$$E\xi_n\eta_n = \sum_{k,l \geq 0} \frac{kl}{n^2} E\left[I_{\{k/n \leq \xi < (k+1)/n\}} I_{\{l/n \leq \eta < (l+1)/n\}}\right]$$
$$= \sum_{k,l \geq 0} \frac{kl}{n^2} E\left[I_{\{k/n \leq \xi < (k+1)/n\}}\right] \cdot E\left[I_{\{l/n \leq \eta < (l+1)/n\}}\right] = E\xi_n \cdot E\eta_n.$$

Now notice that

$$|E\xi\eta - E\xi_n\eta_n| \leq E|\xi\eta - \xi_n\eta_n| \leq E[\xi \cdot |\eta - \eta_n|] + E[\eta_n \cdot |\xi - \xi_n|].$$

Since $|\eta - \eta_n| \leq 1/n$ and $|\xi - \xi_n| \leq 1/n$, and $\eta_n \leq \eta$, we have

$$E[\xi \cdot |\eta - \eta_n|] \leq \frac{1}{n} E\xi \to 0,$$
$$E[\eta_n \cdot |\xi - \xi_n|] \leq \frac{1}{n} E\eta \to 0.$$

Therefore $E\xi_n\eta_n \to E\xi\eta$, and taking limits yields $E\xi\eta = E\xi \cdot E\eta$.

For the general case, decompose $\xi = \xi^+ - \xi^-$ and $\eta = \eta^+ - \eta^-$, apply the result for nonnegative variables to each product of components, and use independence to conclude. The finiteness $E|\xi\eta| < \infty$ follows from $E|\xi\eta| = E|\xi| \cdot E|\eta| < \infty$ (applying the result to $|\xi|$ and $|\eta|$, which are also independent). $\square$
