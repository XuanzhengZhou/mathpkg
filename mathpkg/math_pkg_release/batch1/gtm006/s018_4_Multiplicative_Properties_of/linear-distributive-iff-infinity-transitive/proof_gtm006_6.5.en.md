---
role: proof
locale: en
of_concept: linear-distributive-iff-infinity-transitive
source_book: gtm006
source_chapter: "6"
source_section: "4. Multiplicative Properties of (R,T)"
---

**Proof.** (i) Suppose $(R, T)$ is linear with associative multiplication and satisfies the left distributive law.

A repetition of the arguments used in the earlier proofs of this chapter shows that the mapping

$$\phi_a: (x, y) \rightarrow (x, ay), \quad (m) \rightarrow (am), \quad (\infty) \rightarrow (\infty),$$
$$[m, k] \rightarrow [am, k], \quad [k] \rightarrow [k], \quad [0, 0] \rightarrow [0, 0]$$

is a $((\infty), [0, 0])$-homology mapping $(0, 1)$ onto $(0, a)$ for any $a \in R^*$. Hence $\mathcal{P}$ is $((\infty), [0, 0])$-transitive.

(ii) Conversely, suppose $\mathcal{P}$ is $((\infty), [0, 0])$-transitive. Then for each $a \in R^*$ there exists a unique $((\infty), [0, 0])$-homology $\phi_a$ sending $(0, 1)$ to $(0, a)$. As $\phi_a$ fixes $(\infty)$ and $[0, 0]$ pointwise, and since $(R, T)$ is linear so that $T(m, x, y) = mx + y$, the incidence condition for $\phi_a$ yields the equation

$$m(ay) + x = (am)y + x$$

for all $m, a \in R^*$ and $y \in R$. Putting $y = 0$ in this equation gives associative multiplication, and the left distributive law follows by putting $m = 1$. $\square$
