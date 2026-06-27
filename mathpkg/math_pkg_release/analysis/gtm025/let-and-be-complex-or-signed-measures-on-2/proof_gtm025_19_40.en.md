---
role: proof
locale: en
of_concept: "let-and-be-complex-or-signed-measures-on-2"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.40"
---

Suppose that $v \ll \mu$ and $\sigma \ll \mu$, and let $E \in \mathcal{A}$ be such that $|\mu|(E) = 0$. Then $(\alpha v)(E) = \alpha v(E) = \alpha \cdot 0 = 0$ and $(v + \sigma)(E) = v(E) + \sigma(E) = 0$. Thus (i) holds.

Next suppose that $v \perp \mu$ and $\sigma \perp \mu$. Choose $A$ and $B$ in $\mathcal{A}$ such that $|\mu|(A) = |\mu|(B) = 0$, $|v|(A') = 0$, and $|\sigma|(B') = 0$. Let $C = A \cup B$. It is clear that

$$|v + \sigma|(C') \leq (|v| + |\sigma|)(C') \leq |v|(A') + |\sigma|(B') = 0$$

and that $|\mu|(C) \

is a measure. Thus suppose that $v$ is a $\sigma$-finite measure on $(X, \mathcal{A})$. The measure $v$ is absolutely continuous with respect to the measure $\mu + v$, and both are $\sigma$-finite. Hence, by (19.24), there exists a nonnegative, real-valued, $\mathcal{A}$-measurable function $f_0$ on $X$ such that

$$\int_X f \, dv = \int_X f f_0 \, d(\mu + v)$$

(1)

for all nonnegative $\mathcal{A}$-measurable functions $f$. We claim that $f_0 \leq 1$ a.e. with respect to $\mu + v$. To see this, let $E = \{x : f_0(x) > 1\}$ and assume that $(\mu + v)(E) > 0$. We can write

$$E = \bigcup_{n=1}^{\infty} \left\{x : f_0(x) \geq 1 + \frac{1}{n}\right\},$$

and from this equality it is clear that there exists a number $\alpha > 1$ such that $(\mu + v)(F) > 0$, where

$$F = \{x : f_0(x) \geq \alpha > 1\}.$$

Since $\mu + v$ is $\sigma$-finite, there is a set $A \in \mathcal{A}$ such that $A \subset F$ and $0 < (\mu + v)(A) < \infty$. Putting $f = \xi_A$ in (1), we obtain

$$v(A) = \int_A f_0 \, d\mu + \int_A f_0 \, dv \geq \alpha \mu(A) + \alpha v(A),$$

and so

$$(1 - \alpha)v(A) \geq \alpha \mu(A).$$

Since $\alpha > 1$, the inequality $v(A) > 0$ implies that $\alpha \mu(A) < 0$; it follows that $v(A) = 0$. Hence we have $0 \geq \alpha \mu(A)$, and so $\mu(A) = 0$

We must show that $v_1$ is absolutely continuous with respect to $\mu$. To do this, first consider any $C \in \mathcal{A}$ such that $\mu(C) = 0$ and $\nu(C) < \infty$. We have

$$v_1(C) = \nu(C \cap B') = \int_{C \cap B'} f_1 d\mu + \int_{C \cap B'} f_1 d\nu = \int_{C \cap B'} f_1 d\nu,$$

and so

$$\int_{C \cap B'} (1 - f_1) d\nu = 0.$$

(3)

The function $1 - f_1$ is positive on $B'$, and so the equality (3) implies that $v_1(C) = \nu(C \cap B') = 0$, as desired. For an arbitrary $C$ in $\mathcal{A}$ such that $\mu(C) = 0$, write $C = \bigcup_{n=1}^{\infty} C_n$ where the $C_n$'s are pairwise disjoint sets in $\mathcal{A}$ and $\nu(C_n) < \infty$ for all $n$. The case just considered applies to each $C_n$, and so $v_1(C_n) = 0$ for $n = 1, 2, \ldots$; and of course it follows by countable additivity that $v_1(C) = 0$.

Finally, we prove the uniqueness of the decomposition. Suppose that $\nu = v_1 + v_2 = \tilde{v}_1 + \tilde{v}_2$, where $v_1$ and $\tilde{v}_1$ are absolutely continuous with respect to $\mu$ and $v_2$ and $\tilde{v}_2$ are mutually singular with respect to $\mu$. Let $B$ and $\tilde{B}$ be sets in $\mathcal{A}$ such that $\mu(B) = \mu(\tilde{B}) = 0$ and $v_2(B') = \tilde{v}_2(\tilde{B}') = 0$. For a set $C$ in $\mathcal{A}$ such that $C \subset B \cup \tilde{B}$ we have $\mu(C) =

and

(ii) $\frac{d\mu_2}{d\mu_0} = \frac{d\mu_2}{d\mu_1} \cdot \frac{d\mu_1}{d\mu_0} \mu_0 - a.e.$

Proof. Assertion (i) is trivial. Let $f_0 = \frac{d\mu_1}{d\mu_0}$ and $f_1 = \frac{d\mu_2}{d\mu_1}$. Assertion (ii) follows from the equalities

$$\int_X f d\mu_2 = \int_X f f_1 d\mu_1 = \int_X f f_1 f_0 d\mu_0.$$

We turn now to a detailed study of the relationship between absolute continuity for functions and for measures. We first show that the mappings

$$\alpha \rightarrow S_\alpha \rightarrow \lambda_\alpha$$

described in §§ 8 and 9 establish one-to-one correspondences between the set of all normalized nondecreasing functions $\alpha$ on $R$ (8.20), the set of all nonnegative linear functionals on $\mathfrak{C}_{00}(R)$, and the set of all [regular] Borel measures on $R$.$^1$
