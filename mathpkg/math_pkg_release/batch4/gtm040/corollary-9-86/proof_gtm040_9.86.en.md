---
role: proof
locale: en
of_concept: corollary-9-86
source_book: gtm040
source_chapter: "9"
source_section: "86"
---

**Proof:** Restrict the equations of Proposition 9-85 to square matrices indexed by the states of $E$.

We shall see shortly how Corollary 9-86 may be used to compute $P^E$ from $K_E$. Although we have the formula $P^E = T + UNR$ for $P^E$, this expression is not of practical value for infinite chains, since $N$ is indexed by the states of $\tilde{E}$. On the other hand, $K_E$ can be computed

Proposition 9-87: For any finite set $E$ there is a constant $k(E)$ such that

$$\lambda_E^E K_E = k(E) \alpha_E \text{ and } K_E l_E^E = k(E) 1.$$

Furthermore,

$$k(E) = \lambda_E^E K_E l_E^E \text{ and } k(E) = \hat{k}(E).$$

Proof: In Corollary 9-86, multiply the first equation by $K_E$ on the right and the second by $K_E$ on the left and equate the results. Then

$$1(\lambda_E^E K_E) = (K_E l_E^E) \alpha_E.$$

Thus for some constant $k(E)$, we have $K_E l_E^E = k(E) 1$ and $\lambda_E^E K_E = k(E) \alpha_E$. Multiplication of $\lambda_E^E K_E = k(E) \alpha_E$ on the right by $l_E^E$ gives $k(E) = \lambda_E^E K_E l_E^E$, since $\alpha_E l_E^E = 1$. The dual of this equation is $k(E) = \hat{k}_E^E \hat{k}_E l_E^E$, and thus $k(E) = \hat{k}(E).$

Definition 9-88: For a finite set $E$ the constant $k(E)$ such that $K_E l_E^E = k(E) 1$ is called the capacity of $E$.

Just as the $K$-matrix in general depends upon the state 0 selected, so capacity in general is a function of the distinguished state. If $E = \{i\}$, then $\lambda_j^E = \delta_{ij}$, and from Proposition 9-87 we see that

$$K_{ii} = k(\{i\}) \alpha_i$$

or

$$k(\{i\}) = (G_{0i} - C_{0i}) / \alpha_i.$$

In particular, $k(\{0\}) = 0$.

If we form a $K'$ matrix by using a distinguished state $0'$, then

$$K_{ij}' - K_{ij}

In general, there is no reason why $k(E)$ should be positive. However, if 0 is in $E$, then

$$k(E) = (Kl^E)_0 = (Gl^E)_0 \geq 0,$$

since $Kl^E$ is constant on $E$. The dual expression is

$$\alpha_0 k(E) = (\lambda^E C)_0.$$

In the following discussions we shall restrict ourselves to sets which contain the reference point. We accordingly denote by $\mathcal{L}_0$ the collection of all finite sets which contain 0.
