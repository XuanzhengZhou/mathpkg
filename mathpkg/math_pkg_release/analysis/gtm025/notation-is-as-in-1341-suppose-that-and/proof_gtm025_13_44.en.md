---
role: proof
locale: en
of_concept: "notation-is-as-in-1341-suppose-that-and"
source_book: gtm025
source_chapter: "Spaces of Integrable Functions"
source_section: "13.44"
---

Choose $\alpha \in R$ such that $\|f_n\|_p \leq \alpha$ for all $n \in N$. By Fatou's lemma (12.23), we have

$$\|f\|_p^p = \int_X |f|^p d\mu = \int_X \lim_{n \rightarrow \infty} |f_n|^p d\mu$$

$$\leq \lim_{n \rightarrow \infty} \int_X |f_n|^p d\mu \leq \alpha^p.$$

Let $\varepsilon > 0$ and $g \in \mathfrak{L}_{p'}$ be given. Use (12.34) to obtain $\delta > 0$ such that for all $E \in \mathcal{A}$ for which $\mu(E) < \delta$, we have

$$2\alpha \left( \int_E |g|^{p'} d\mu \right)^{\frac{1}{p'}} < \frac{\varepsilon}{3}.$$

Next select $A \in \mathcal{A}$ such that $\mu(A) < \infty$ and

$$2\alpha \left( \int_{A'} |g|^{p'} d\mu \right)^{\frac{1}{p'}} < \frac{\varepsilon}{3}.$$

Apply Egorov's theorem (11.32) to obtain $B \in \mathcal{A}$ such that $B \subset A$, $\mu(A \cap B') < \delta$, and $f_n \rightarrow f$ uniformly on $B$. Finally, choose $n_0 \in N$ such that $n \geq n_0$ implies

$$|f(x) - f_n(x)| (\mu(B))^{\frac{1}{p}} \|g\

Proof. Assume that $f_n$ does not converge weakly to $f$. Choose $g \in \mathfrak{L}_p'$ such that

$$\lim_{n \to \infty} \left| \int_X f g d\mu - \int_X f_n g d\mu \right| = \alpha \neq 0.$$

Use (6.84) to find integers $n_1 < n_2 < \cdots$ such that

$$\lim_{k \to \infty} \left| \int_X (f - f_{n_k}) g d\mu \right| = \alpha.$$ (1)

Next use (11.26) to find a subsequence $(f_{n_{kj}})_{j=1}^{\infty}$ of $(f_{n_k})_{k=1}^{\infty}$ such that $\lim_{j \to \infty} f_{n_{kj}} = f \mu$-a.e. It follows from (13.44) that

$$\lim_{j \to \infty} \left| \int_X (f - f_{n_{kj}}) g d\mu \right| = 0.$$

But this equality is incompatible with (1). $\square$

(13.46) Remark. Example (13.43.b) shows that neither (13.44) nor (13.45) is true for the case $p = 1$. However, if we replace the hypothesis that $(\|f_n\|_1)$ be a bounded sequence by the hypothesis that $\|f_n\|_1 \to \|f\|_1$, we get a much stronger conclusion.
