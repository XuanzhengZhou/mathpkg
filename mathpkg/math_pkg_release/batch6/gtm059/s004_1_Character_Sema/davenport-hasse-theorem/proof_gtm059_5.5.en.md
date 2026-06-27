---
role: proof
locale: en
of_concept: davenport-hasse-theorem
source_book: gtm059
source_chapter: "1"
source_section: "5. Gauss Sums Over Extension Fields"
---

Let $m = [E:F]$. For any polynomial
$$f(X) = X^n + c_1 X^{n-1} + \cdots + c_0$$
with coefficients in $F$, define
$$\psi(f) = \chi(c_0)\lambda(c_1).$$
Then
$$\psi: \{\text{monic polynomials of degree } \ge 1 \text{ over } F\} \to F$$
is a homomorphism, i.e., satisfies $\psi(fg) = \psi(f)\psi(g)$. Write $n(f) = \deg f$. From unique factorization we have the formula
$$1 + \sum_f \psi(f) X^{n(f)} = \prod_P \frac{1}{1 - \psi(P) X^{n(P)}},$$
where the product is taken over all monic irreducible polynomials $P$ over $F$.

Suppose $f$ is of degree $1$, say $f(X) = X + c$. Then we see that
$$\sum_{n(f)=1} \psi(f) X^{n(f)} = S_F(\chi, \lambda) X.$$
On the other hand, if $n \ge 2$ we have
$$\sum_{n(f)=n} \psi(f) X^n = 0,$$
since
$$\sum_{n(f)=n} \psi(f) = \sum_{c_0 \in F^*} \chi(c_0) \sum_{c_1 \in F} \lambda(c_1) \cdot (\text{sum over remaining } c_i) = 0,$$
and the sum over $c_1 \in F$ on the right is $0$. Therefore we find
$$1 + S_F(\chi, \lambda) X = \prod_P \frac{1}{1 - \psi(P) X^{n(P)}}. \tag{1}$$

Mutatis mutandis, using the variable $X^m$ instead of $X$, we get
$$1 + S_E(\chi_E, \lambda_E) X^m = \prod_Q \frac{1}{1 - \psi_E(Q) X^{m \cdot n(Q)}}, \tag{2}$$
where the product is taken over all monic irreducible polynomials $Q$ over $E$, and
$$\psi_E(Q) = \chi_E(\text{co}_E(Q)) \lambda_E(\text{cl}_E(Q)).$$

We shall write the product over $Q$ as
$$\prod_Q = \prod_P \prod_{Q \mid P}.$$
Each irreducible polynomial $P$ splits in $E$ into a product
$$P = Q_1 \cdots Q_r.$$
Let $n = n(P) = \deg P$. Then $\deg Q_i = n/r$. If $\alpha$ is any root of $P$, then $[F(\alpha):F] = n$ and the field $F(\alpha)$ is independent of the chosen root. We have the following lattice of fields:
$$\begin{matrix}
& & E & & \\
& \nearrow & & \nwarrow & \\
F(\alpha) & & & & E \cap F(\alpha) \\
& \nwarrow & & \nearrow & \\
& & F & &
\end{matrix}$$
All the polynomials $Q_i$ are conjugate over $F$, and their coefficients generate the field $F' = E \cap F(\alpha)$, of degree $r$ over $F$. We have $r = (m, n)$. These facts are all obvious from elementary field theory.

Since $\chi_E = \chi \circ \operatorname{N}_{E/F}$ and $\lambda_E = \lambda \circ \operatorname{Tr}_{E/F}$, we get
$$\psi_E(Q) = \bigl(\chi(\text{co}(P)) \lambda(\text{cl}(P))\bigr)^{[E:F']} = \psi(P)^{m/r}.$$

With a view towards (2), we conclude that
$$\prod_{Q \mid P} \bigl(1 - \psi_E(Q) X^{m \cdot n(Q)}\bigr) = \bigl(1 - \psi(P)^{m/r} X^{m n / r}\bigr)^r = \prod_{\zeta^m = 1} \bigl(1 - \psi(P) (\zeta X)^n\bigr). \tag{3}$$

For this last step, we observe that the map $\zeta \mapsto \zeta^{m/r}$ gives a surjection of $\boldsymbol{\mu}_m \to \boldsymbol{\mu}_{m/r}$, and the inverse image of any element of $\boldsymbol{\mu}_{m/r}$ is a coset of $\boldsymbol{\mu}_r$ since $r = (m, n)$. This makes the last step obvious.

Substituting (3) in (2), we now find
$$1 + S_E(\chi_E, \lambda_E) X^m = \prod_P \prod_{\zeta^m = 1} \bigl(1 - \psi(P) (\zeta X)^{n(P)}\bigr) = \prod_{\zeta^m = 1} \bigl(1 + S_F(\chi, \lambda) \zeta X\bigr).$$

This proves the theorem.
