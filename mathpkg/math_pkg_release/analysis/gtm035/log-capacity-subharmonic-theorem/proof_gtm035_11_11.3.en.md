---
role: proof
locale: en
of_concept: log-capacity-subharmonic-theorem
source_book: gtm035
source_chapter: "11"
source_section: "11.3"
---
# Proof of Logarithm of Capacity is Subharmonic

**Theorem 11.3.** Let $(A, X, \Omega, p)$ be a maximum modulus algebra over $\Omega$. Fix $F \in A$. Then $\lambda \mapsto \log Z_F(\lambda)$ is subharmonic on $\Omega$.

*Proof.* In view of Exercise 11.3, it suffices to show that $\log Z_F$ satisfies the sub-mean-value inequality (17).

We fix a disk $\Delta = \{ |\lambda - \lambda_0| \leq r \}$ contained in $\Omega$ and apply Theorem 11.2 to the function $F$. Let $x^0 \in p^{-1}(\lambda_0)$ be arbitrary. By Theorem 11.2, there exists a bounded analytic function $G$ on $\operatorname{int}(\Delta)$ such that

$$G(\lambda_0) = F(x^0),$$

and for almost all $\lambda \in \partial \Delta$,

$$|G(\lambda)| \leq \max_{x \in p^{-1}(\lambda)} |F(x)| = Z_F(\lambda).$$

Since $G$ is analytic on $\operatorname{int}(\Delta)$, $\log |G|$ is subharmonic there (or identically $-\infty$). In particular,

$$\log |G(\lambda_0)| \leq \frac{1}{2\pi} \int_0^{2\pi} \log |G(\lambda_0 + re^{i\theta})| d\theta.$$

But $|G(\lambda_0)| = |F(x^0)|$, and $|G(\lambda)| \leq Z_F(\lambda)$ for a.a. $\lambda \in \partial \Delta$. Hence

$$\log |F(x^0)| \leq \frac{1}{2\pi} \int_0^{2\pi} \log Z_F(\lambda_0 + re^{i\theta}) d\theta.$$

Since this holds for every $x^0 \in p^{-1}(\lambda_0)$, taking the supremum over $x^0 \in p^{-1}(\lambda_0)$ yields

$$\log Z_F(\lambda_0) \leq \frac{1}{2\pi} \int_0^{2\pi} \log Z_F(\lambda_0 + re^{i\theta}) d\theta.$$

Together with the upper semicontinuity of $\log Z_F$ (Exercise 11.3), this establishes that $\log Z_F$ is subharmonic on $\Omega$. $\square$
