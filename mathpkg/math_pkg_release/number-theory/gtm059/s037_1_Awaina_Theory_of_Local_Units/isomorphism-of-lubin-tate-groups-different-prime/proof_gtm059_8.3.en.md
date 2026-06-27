---
role: proof
locale: en
of_concept: isomorphism-of-lubin-tate-groups-different-prime
source_book: gtm059
source_chapter: "8"
source_section: "3. Changing the Prime"
---

Since $\pi_1 / \pi_2 = u \in \mathfrak{o}^*$, choose $\varepsilon \in \mathfrak{o}^*$ such that $\varepsilon^{q-1} = u$ (such $\varepsilon$ exists because the residue field has $q$ elements and $u \equiv 1 \pmod{\mathfrak{m}}$ if the residue fields have the same prime).

We construct $\theta$ by induction on the degree. Set $\theta^{(1)}(X) = \varepsilon X$. Suppose we have constructed $\theta^{(r)}(X)$ up to degree $r$ satisfying
$$
\theta^{(r)}(X) \equiv \varepsilon X \pmod{\deg 2}, \qquad \theta^{(r)}(f_1(X)) \equiv f_2(\theta^{(r)}(X)) \pmod{\deg r+1}.
$$
We seek $b X^{r+1}$ such that $\theta^{(r+1)} = \theta^{(r)} + b X^{r+1}$ satisfies the congruence modulo $\deg r+2$.

Compute:
$$
\theta^{(r+1)}(f_1(X)) = \theta^{(r)}(f_1(X)) + b (f_1(X))^{r+1} \equiv \theta^{(r)}(f_1(X)) + b \pi_1^{r+1} X^{r+1} \pmod{\deg r+2},
$$
$$
f_2(\theta^{(r+1)}(X)) = f_2(\theta^{(r)}(X) + b X^{r+1}) \equiv f_2(\theta^{(r)}(X)) + \pi_2 b X^{r+1} \pmod{\deg r+2}.
$$
Let $C_{r+1}(X)$ be the degree $r+1$ part of $f_2(\theta^{(r)}(X)) - \theta^{(r)}(f_1(X))$. The required condition is
$$
b \pi_1^{r+1} - b \pi_2 = -C_{r+1},
$$
i.e., $b(\pi_2 - \pi_1^{r+1}) = C_{r+1}$. Since $\pi_2$ is not a zero-divisor and $\pi_1^{r+1}$ is highly divisible by $\pi_2$ (as $\pi_1 = u\pi_2$), the coefficient $\pi_2 - \pi_1^{r+1}$ is a non-zero-divisor, yielding a unique $b$.

This constructs $\theta$ commuting with $f_1, f_2$. The verification that $\theta$ is a formal group isomorphism and commutes with all $[a]_{f_i}$ follows by the uniqueness clause of the Construction Lemma, since both $\theta(F_{f_1}(X,Y))$ and $F_{f_2}(\theta(X), \theta(Y))$ satisfy the same characterizing conditions with respect to $f_1, f_2$.
