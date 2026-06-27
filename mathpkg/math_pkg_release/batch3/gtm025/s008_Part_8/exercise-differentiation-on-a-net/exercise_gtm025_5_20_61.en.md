---
role: exercise
locale: en
chapter: "5"
section: "20"
exercise_number: 61
---

Differentiation on a net. Let $(X, \mathcal{A}, \mu)$ be a $\sigma$-finite measure space. Consider a sequence $(\mathcal{N}_n)_{n=1}^{\infty}$ of countable measurable partitions of $X$.

(a) Let $\eta$ be a $\sigma$-finite signed measure on $\mathcal{A}$. Apply (20.56) and the definition of derivative in (20.53) to study limits of averages.

(b) Let $\varphi$ be a Lebesgue measurable function on $R$ such that $\int_{-a}^{a} |\varphi| d\lambda < \infty$ for all $a > 0$. For every $x \in R$, let $J(n, x)$ be the interval $[k \cdot 2^{-n}, (k + 1) \cdot 2^{-n}]$ that contains $x$ ($n \in N, k \in Z$). Prove that $\lim_{n \to \infty} 2^n \int_{J(n, x)} \varphi d\lambda = \varphi(x)$ for $\lambda$-almost all $x \in R$. [Hint. Apply part (a) with $X = R$, $\mathcal{A} = \mathcal{M}_{\lambda}$, $\mathcal{N}_n = \{[k 2^{-n}, (k + 1) 2^{-n}]\}_{k=-\infty}^{\infty}$, $\eta(A) = \int_{A} \varphi d\lambda$.] Compare this result with (18.3).

(c) Let $\eta$ be a $\sigma$-finite signed measure on $\mathcal{B}(R)$ such that $|\eta|$ and $\lambda$ are mutually singular. Prove that $\lim_{n \to \infty} 2^n \eta(J(n, x)) = 0$ for $\lambda$-almost all $x \in R$. For $\eta$ a signed measure, prove that $\lim_{n \to \infty} 2^n \eta(J(n, x)) = \pm \infty$ on a set $B$ such that $|\eta|(B') = 0$.
