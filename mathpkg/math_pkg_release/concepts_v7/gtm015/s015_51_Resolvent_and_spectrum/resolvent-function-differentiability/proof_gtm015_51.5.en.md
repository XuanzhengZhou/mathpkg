---
role: proof
locale: en
of_concept: resolvent-function-differentiability
source_book: gtm015
source_chapter: "51"
source_section: "51.5"
---

# Proof of Differentiability of the resolvent function

(51.5) Theorem. If $x \in A$ and $R = R_x$ is the resolvent function of $x$, then

(i) $\lim_{\lambda \to \infty} R(\lambda) = 0$;

(ii) $R$ is differentiable at every $\lambda \in \rho(x)$, in the sense that the limit

$$\lim_{h \to 0} (1/h)[R(\lambda + h) - R(\lambda)]$$

exists; the limit is $-(\lambda 1 - x)^{-2}$.

Proof. (i) In view of (51.2) it is permissible to contemplate the limit. Assuming $\lambda_n \in \rho(x)$, $|\lambda_n| \to \infty$, it is to be shown that $\|R(\lambda_n)\| \to 0$. We can suppose that the $\lambda_n$ are nonzero. Since $\lambda_n^{-1} \to 0$, we have $1 - \lambda_n^{-1}x \to 1$; citing (50.7) we have $(1 - \lambda_n^{-1}x)^{-1} \to 1$, therefore

$$R(\lambda_n) = (\lambda_n 1 - x)^{-1} = \lambda_n^{-1}(1 - \lambda_n^{-1}x)^{-1} \to 0 \cdot 1 = 0.$$

(ii) At any rate, $R$ is continuous (it is the composite of continuous mappings $\lambda \mapsto \lambda 1 - x$ and $y \mapsto y^{-1}$). Let $\lambda \in \rho(x)$ and let $h$ be a nonzero complex variable; for $h$ sufficiently small, we have $\lambda + h \in \rho(x)$ and, by the resolvent identity,

$$R(\lambda + h) - R(\lambda) = -hR(\lambda + h)R(\lambda).$$

Thus

$$(1/h)[R(\lambda + h) - R(\lambda)] = -R(\lambda + h)R(\lambda)$$

for all sufficiently small $h \neq 0$; by continuity, the right side tends to $-R(\lambda)^2

by the continuity and linearity of $f$; in other words,

$$\frac{F(\lambda + h) - F(\lambda)}{h} \rightarrow -f((\lambda 1 - x)^{-2})$$

as $h \rightarrow 0$.

The resolvent set of an element is large (51.2) but not too large:
