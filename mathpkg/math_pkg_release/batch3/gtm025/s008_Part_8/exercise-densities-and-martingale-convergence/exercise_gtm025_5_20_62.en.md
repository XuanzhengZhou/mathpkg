---
role: exercise
locale: en
chapter: "5"
section: "20"
exercise_number: 62
---

Densities. Notation is as in (20.61). Let $E$ be any set in $\mathcal{A}$. Let $\eta$ be the measure on $\mathcal{A}$ defined by $\eta(A) = \mu(A \cap E)$.

(a) Prove that $\lim_{n \to \infty} f_n$ is a constant $\mu$-almost everywhere. [Hints. Consider the Lebesgue decomposition $\eta_0 = \eta_{0a} + \eta_{0s}$. Let $B_0 \in \mathcal{M}_0$ be a set such that $\mu_0(B_0) = 0$ and $|\eta_{0s}|(B_0') = 0$. Let $g$ be a Lebesgue-Radon-Nikodym derivative of $\eta_{0a}$ with respect to $\mu_0$. Since $\mu_0$ assumes only the values 0 and 1, there is a number $\alpha$ for which $\mu_0(\{x \in X : g(x) = \alpha\}) = 1$ and so $\lim_{n \to \infty} f_n = \alpha$ $\mu_0$-almost everywhere on $X$.]

(b) Prove that the $\alpha$ of part (a) is equal to $\int_X f_1(x) d\mu_1(x) = \eta_{1a}(X)$, where $\eta_{1a}$ is the $\mu_1$-absolutely continuous part of $\eta_1$.
