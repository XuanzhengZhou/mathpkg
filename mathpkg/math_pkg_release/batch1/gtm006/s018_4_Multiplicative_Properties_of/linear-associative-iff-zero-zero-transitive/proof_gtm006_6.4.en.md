---
role: proof
locale: en
of_concept: linear-associative-iff-zero-zero-transitive
source_book: gtm006
source_chapter: "6"
source_section: "4. Multiplicative Properties of (R,T)"
---

**Proof.** (i) Suppose $(R, T)$ is linear with associative multiplication.

For any $a \in R^*$ we must exhibit a $((0), [0])$-homology sending $(1, 0)$ onto $(a, 0)$. Since the required homology does not have axis $[0]$ we will show its existence by defining its action on all of $\mathcal{P}$. We define $\phi_a$ by

$$\phi_a : (x, y) \rightarrow (ax, y), \quad (m) \rightarrow (ma^{-1}), \quad (\infty) \rightarrow (\infty),$$
$$[m, k] \rightarrow [ma^{-1}, k], \quad [k] \rightarrow [ak], \quad [0] \rightarrow [\infty]$$

where $t = a^{-1}$ is the unique solution of $ta = 1$ in $(R^*, \cdot)$. Clearly if $\phi_a$ is a collineation then it is a $((0), [0])$-homology mapping $(1, 0)$ onto $(a, 0)$ and so, in order to prove the theorem, we need only show that $\phi_a$ preserves incidence.

As $(R, T)$ is linear, $(x, y)$ is on $[m, k]$ if and only if $mx + y = k$, whereas $(x, y)^{\phi_a}$ is on $[m, k]^{\phi_a}$ if and only if $(ma^{-1})(ax) + y = k$, i.e. $m(ax) + y = k$ by associativity. But $mx + y = k$ iff $m(ax) + y = k$ since $a$ acts as a group automorphism, so $\phi_a$ preserves incidence. Hence $\mathcal{P}$ is $((0), [0])$-transitive.

(ii) Conversely, suppose $\mathcal{P}$ is $((0), [0])$-transitive. Then for each $a \in R^*$ there exists a unique $((0), [0])$-homology $\alpha_a$ sending $(1, 0)$ to $(a, 0)$. Since $\alpha_a$ fixes $(0)$ and $(\infty)$ and maps $[0]$ to itself, it induces a permutation $\beta_a$ on the affine points of $[0]$ and a permutation $\gamma_a$ on the lines through $(0)$ distinct from $[0]$.

We now introduce a new mapping $\gamma_a$ of $R^*$ onto itself given by $x^{\gamma_a} = xa$ for all $x \in R^*$; i.e. $\gamma_a$ is the mapping of multiplication on the right by $a$. From the relationship $\alpha_a = \gamma_a^{-1}$ we obtain

$$mx = m^{\gamma_a^{-1}} x^{\beta_a}. \tag{3}$$

Putting $m = a$ in (3) and using the fact that $a^{\gamma_a^{-1}} = 1$ we have $ax = x^{\beta_a}$ so that

$$mx = m^{\gamma_a^{-1}} (ax). \tag{4}$$

Since $\gamma_a$ is a permutation on $R^*$, for any $m \neq 0$ there is a unique $u \in R$ with $m = ua$. Note that since $m$ was arbitrary then so is $u$. By substituting $m = ua$ in (4) we get

$$(ua) x = (ua)^{\gamma_a^{-1}} (ax) = (ua)^{\gamma_a^{-1}} (ax) = u(ax) \tag{5}$$

for all $u, a, x \in R^*$, and so $R$ has associative multiplication.

To prove the linearity of $(R, T)$ we note that, for all $m, a, x \in R$, $a \neq 0$, $T(m, x, y) = T(ma^{-1}, ax, y)$. Thus, putting $m = a$ we have $T(a, x, y) = T(1, ax, y) = ax + y$ as required.
