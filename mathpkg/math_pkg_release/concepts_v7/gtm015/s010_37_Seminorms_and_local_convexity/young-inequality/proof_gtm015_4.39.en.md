---
role: proof
locale: en
of_concept: young-inequality
source_book: gtm015
source_chapter: "4"
source_section: "39"
---

# Proof of Young's inequality for products of nonnegative real numbers

Let $p > 1$ and define $q = p/(p-1)$, so that $p^{-1} + q^{-1} = 1$. Then for all $a \geq 0$, $b \geq 0$,

$$ab \leq \frac{a^p}{p} + \frac{b^q}{q}.$$

*Proof.* The function $t \mapsto e^t$ is convex. For any real numbers $u, v$ and $\lambda \in [0, 1]$,

$$e^{\lambda u + (1-\lambda)v} \leq \lambda e^u + (1-\lambda)e^v.$$

Take $\lambda = 1/p$, $1 - \lambda = 1/q$, $u = p \ln a$ (if $a > 0$), and $v = q \ln b$ (if $b > 0$). Then

$$ab = e^{\ln a + \ln b} = e^{\frac{1}{p}(p\ln a) + \frac{1}{q}(q\ln b)} \leq \frac{1}{p}e^{p\ln a} + \frac{1}{q}e^{q\ln b} = \frac{a^p}{p} + \frac{b^q}{q}.$$

If $a = 0$ or $b = 0$, the inequality is trivial. For $p = 2$, the inequality reduces to $2ab \leq a^2 + b^2$, i.e., $(a - b)^2 \geq 0$.
