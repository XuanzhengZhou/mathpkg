---
role: proof
locale: en
of_concept: smooth-initial-value-lemma
source_book: gtm014
source_chapter: "IV"
source_section: "2"
---

The formal solution is given by
$$\bar{F}(t, x) = e^{tX} f \equiv \sum_{k=0}^{\infty} \frac{t^k}{k!} X^k f.$$
Differentiating the RHS term by term and evaluating at $t = 0$ shows that (b) holds formally. Condition (a) is also clearly satisfied. The problem is that $\bar{F}$ need not be smooth (the series may diverge).

By the Borel Theorem (Lemma 2.5), we may choose a smooth function $F$ of the form
$$F(t, x) = \sum_{k=0}^{\infty} \frac{t^k}{k!} \rho(\mu_k t) X^k f$$
having the same power series expansion as $\bar{F}$ at $t = 0$, where $\rho$ is a bump function and $\mu_k \to \infty$ sufficiently fast. Since $F$ has the same Taylor series as $\bar{F}$ at $t = 0$, the initial condition $F(0, x) = f(x)$ is satisfied. Moreover, the construction ensures that $\partial F / \partial t - XF$ vanishes to infinite order at $t = 0$, which by the uniqueness of solutions to this first-order linear PDE implies it vanishes identically, giving $\partial F / \partial t = XF$.
