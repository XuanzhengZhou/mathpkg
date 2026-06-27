---
role: proof
locale: en
of_concept: sum-of-nilpotent-normal-endomorphisms-is-nilpotent
source_book: gtm030
source_chapter: "2"
source_section: "13"
---

According to Corollary 1, if $\eta = \eta_1 + \eta_2$ is not nilpotent, then it is an automorphism. Let $\eta^{-1}$ be its inverse. Evidently this mapping is a normal $M$-endomorphism and we have $\eta_1 \eta^{-1} + \eta_2 \eta^{-1} = 1$, or $\lambda_1 + \lambda_2 = 1$ where $\lambda_i = \eta_i \eta^{-1}$.

Since $\eta_i$ is not an automorphism, its kernel is $\neq 1$. Hence this holds for $\lambda_i$ too. Hence $\lambda_i$ is nilpotent. We note next that

$$\lambda_1 = \lambda_1(\lambda_1 + \lambda_2) = \lambda_1^2 + \lambda_1 \lambda_2$$

and

$$\lambda_1 = (\lambda_1 + \lambda_2)\lambda_1 = \lambda_1^2 + \lambda_2 \lambda_1.$$

Hence $\lambda_1 \lambda_2 = \lambda_2 \lambda_1$ and consequently for any positive integer $m$

$$(\lambda_1 + \lambda_2)^m = \lambda_1^m + \binom{m}{1}\lambda_1^{m-1}\lambda_2 + \cdots + \lambda_2^m.$$

If both $\lambda_1$ and $\lambda_2$ are nilpotent, we can choose $m$ large enough so that each term on the right is $0$, giving $(\lambda_1 + \lambda_2)^m = 0$. But $\lambda_1 + \lambda_2 = 1$, so $1^m = 1 = 0$, a contradiction. Hence $\eta_1 + \eta_2$ must be nilpotent.
