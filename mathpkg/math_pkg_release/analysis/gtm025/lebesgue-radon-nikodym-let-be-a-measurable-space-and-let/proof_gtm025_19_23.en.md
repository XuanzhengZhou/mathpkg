---
role: proof
locale: en
of_concept: "lebesgue-radon-nikodym-let-be-a-measurable-space-and-let"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.23"
---

First consider any bounded, nonnegative, $\mathcal{A}$-measurable function $f$. Let $g$ be the function of (19.22.i). Since both $g$ and $f$ are bounded and $\mu + v$ is a finite measure, the function $(1 + g + \cdots + g^{n-1})f$ is in $\mathfrak{L}_2 (X, \mathcal{A}, \mu + v)$ for every positive integer $n$; and by (19.22) the equality

$$\int_X (1 + g + g^2 + \cdots + g^{n-1})f(1-g) dv$$

$$= \int_X (1 + g + g^2 + \cdots + g^{n-1})fg d\mu$$

holds

for all nonnegative, extended real-valued, $\mathcal{A}$-measurable functions $f$ on $X$. For $f \in \mathfrak{L}_1(X, \mathcal{A}, \nu)$, the function $ff_0$ is in $\mathfrak{L}_1(X, \mathcal{A}, \mu)$, and (i) holds. In particular, we have

(ii) $\nu(A) = \int_A f_0 d\mu$

for all $A \in \mathcal{A}$. Moreover, $f_0$ is unique in the sense that if $g_0$ is any nonnegative, extended real-valued, $\mathcal{A}$-measurable function for which (ii) holds, then $g_0 = f_0 \mu$-a.e.

Proof. Let $\{A_n\}_{n=1}^{\infty}$ and $\{B_n\}_{n=1}^{\infty}$ be pairwise disjoint families of $\mathcal{A}$-measurable sets, each with union $X$, such that $\mu(A_n) < \infty$ and $\nu(B_n) < \infty$ for all $n$. The family $\mathcal{C} = \{A_m \cap B_n\}_{m,n=1}^{\infty}$ is pairwise disjoint, and its union is $X$. Also, each member of this family has finite $\nu$ and $\mu$ measure. Let $(E_n)_{n=1}^{\infty}$ be any arrangement of $\mathcal{C}$ into a sequence of sets. For each $n$, define $\mu_n$ and $\nu_n$ on $\mathcal{A}$ by $\mu_n(A) = \mu(A \cap E_n)$ and $\nu_n(A) = \nu(\dot{A} \cap E_n)$. Then $\mu_n$ and $\nu_n$ are finite measures on $(X, \mathcal{A})$ and $\nu_n \ll \mu_n$ for each $n$; and so (19.23) applies. Thus, for each $n$, we obtain a nonnegative, finite-valued, $\mathcal{A}$-measurable function $f_n$ on $X$ such that

$$\int_X f d\nu_n = \int_X ff_n d\
