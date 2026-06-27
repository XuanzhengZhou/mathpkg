---
role: proof
locale: en
of_concept: ptr-associative-addition-characterization
source_book: gtm006
source_chapter: "VI"
source_section: "3"
---

**Proof.** (i) Suppose $(R, T)$ is linear with associative addition. Let $A, B$ be any two distinct points which are collinear with $(\infty)$ but not incident with $[\infty]$. We must exhibit a $((\infty), [\infty])$-elation mapping $A$ onto $B$. In view of Exercise 4.1, it is sufficient to exhibit a collineation of $\mathcal{P}^{[\infty]}$ that maps $A$ onto $B$ and fixes every line through $(\infty)$ and every point on $[\infty]$.

Define $\phi_a$ for any $a \in R$ by:
$$\phi_a: (x, y) \mapsto (x, y + a), \quad (m) \mapsto (m), \quad (\infty) \mapsto (\infty).$$

Since $(R, T)$ is linear, a point $(x, y)$ lies on the line $[m, k]$ if and only if $mx + y = k$. Under $\phi_a$, the image $(x, y)^{\phi_a} = (x, y + a)$ lies on $[m, k]^{\phi_a} = [m, k + a]$ if and only if $mx + (y + a) = k + a$. By associativity of addition,
$$mx + (y + a) = (mx + y) + a,$$
so $mx + (y + a) = k + a$ if and only if $mx + y = k$. Hence $(x, y)$ is on $[m, k]$ if and only if $(x, y)^{\phi_a}$ is on $[m, k]^{\phi_a}$. For vertical lines $[k]$, the point $(x, y)$ lies on $[k]$ if and only if $x = k$, and $(x, y)^{\phi_a}$ lies on $[k]^{\phi_a} = [k]$ if and only if $x = k$ as well. Thus $\phi_a$ preserves incidence and is a $((\infty), [\infty])$-elation.

(ii) Suppose $\mathcal{P}$ is $((\infty), [\infty])$-transitive. By Theorem 4.29, $\mathcal{P}$ is $((\infty), [\infty])$-desarguesian, which implies by Theorem 6.1 that $(R, T)$ is linear.

For any point $(0, a)$ on $[0]$, there is a $((\infty), [\infty])$-elation mapping $(0, 0)$ onto $(0, a)$. Denote this elation by $\phi_a$. Then for any point $(x, y)$, we have $(x, y)^{\phi_a} = (x, u)$ where $u$ depends only on $y$ and $a$. Thus we may write $(x, y)^{\phi_a} = (x, y^{\alpha_a})$ where $\alpha_a$ is a one-to-one mapping from $R$ onto $R$ such that $0^{\alpha_a} = a$.

The action of $\phi_a$ on points is completely determined:
$$\phi_a: (x, y) \mapsto (x, y^{\alpha_a}), \quad (m) \mapsto (m), \quad (\infty) \mapsto (\infty).$$
Since $(m)^{\phi_a} = (m)$ and $(0, k)^{\phi_a} = (k)^{\phi_a}$, the action on lines is:
$$\phi_a: [m, k] \mapsto [m, k^{\alpha_a}], \quad [k] \mapsto [k], \quad [\infty] \mapsto [\infty].$$

Using linearity of $(R, T)$ and the fact that $\phi_a$ preserves incidence, we have $mx + y = k$ if and only if $mx + y^{\alpha_a} = k^{\alpha_a}$. In particular, taking the case where $(x, y)$ is on $[0, a]$ (so $y = a$), the preservation of incidence gives $y^{\alpha_a} = y + a$ for all $y \in R$. Thus the condition becomes $mx + y = k$ if and only if $mx + (y + a) = k + a$, which holds if and only if $(mx + y) + a = k + a$. Since $(R, +)$ is a loop, this implies $mx + y = k$ if and only if $mx + y = k$, and moreover yields that addition in $R$ is associative. Hence $(R, T)$ is linear with associative addition. $\square$
