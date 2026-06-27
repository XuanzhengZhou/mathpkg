---
role: proof
locale: en
of_concept: exponential-map-convergence-lemma
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* Let $y \in D$, $y \neq 0$. Define

$$\lambda_n(X) = \frac{1}{\pi^n} [\pi^n](X).$$

Then for $i > 0$,

$$\operatorname{ord}_\pi \frac{1}{\pi^i} \frac{[\pi^i](y)}{\pi^i} = (p-1)\operatorname{ord}_\pi y - i.$$

By Lemma 1 (the logarithm lemma), $\lambda(X)$ has integral coefficients. Let $e(X)$ be the power series such that $e(\lambda(X)) = X$. Replacing $X$ with $\lambda(X)$, we see that $\lambda(e(X)) = X$.

If $n$ is large, the coefficients of $\lambda_n(X) - \lambda(X)$ are highly divisible by $\pi$. Let $\lambda(X) = X + \alpha X^2 + \cdots$. Then $e(\lambda(X)) = X$ implies that $e(X) = X - \alpha X^2 + \cdots$ also has integral coefficients for all $y \in D$. It follows that for large $n$, the difference tends to $0$ ($p$-adically) as $n \to \infty$ for each $y \in D$. Furthermore, we conclude that

$$e(\lambda(y)) = y$$

for all $y \in D$, and in particular,

$$\operatorname{ord}_\pi e(y) \geq \operatorname{ord}_\pi y.$$

On the other hand, again using Lemma 4 (from the source text), it is immediate that for $x \in D$, we have

$$\operatorname{ord}_\pi \lambda(x) \geq \operatorname{ord}_\pi x.$$

Since $e$ and $\lambda$ are mutually inverse power series, the valuation inequalities in both directions force equality of valuations, giving

$$\operatorname{ord}_\pi z = \operatorname{ord}_\pi \lambda(z) = \operatorname{ord}_\pi e(z)$$

for all $z \in D$.
