---
role: proof
locale: en
of_concept: "let-be-a-measurable-space-and-let-and-2"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.26"
---

With an eye to proving (i), consider the family $\mathcal{D} = \{B \in \mathcal{A} : C \subset

$v(F) > 0$, we have $\mu(F) > 0$. But we also have $\mu(F \cup D) = \mu(F) + \mu(D) > \alpha$, and this is a contradiction since $F \cup D \in \mathcal{D}$. The existence of a set $F_1$ satisfying (1) follows.

We will next show that $v$ is $\sigma$-finite on $D'$. To this end, let

$$\mathcal{F} = \{F \in \mathcal{A}: F \subset D' \text{ and } v \text{ is } \sigma$-finite on } F\}.$$

There is a nondecreasing sequence $(F_n)_{n=1}^{\infty}$ in $\mathcal{F}$ such that $\lim_{n \to \infty} \mu(F_n) = \sup \{\mu(F): F \in \mathcal{F}\} = \beta$; let $F = \bigcup_{n=1}^{\infty} F_n$. Since $F$ is a countable union of sets on which $v$ is $\sigma$-finite, $v$ is also $\sigma$-finite on $F$; thus $F \in \mathcal{F}$. Also, the equality $\mu(F) = \beta$ follows from (10.13). We claim that $v(F' \cap D') = 0$. If not, then by the preceding paragraph, there exists a set $H \in \mathcal{A}$ such that $H \subset D' \cap F'$ and $0 < v(H) < \infty$; hence $F \cup H \in \mathcal{F}$ and $\mu(H) > 0$.

However we have

$$\mu(F \cup H) = \mu(H) + \mu(F) > \mu(F) = \beta \geq \mu(F \cup H).$$

This contradiction shows that $v(F' \cap D') = 0$, and so $v$ is $\sigma$-finite on $D'$.

Finally, we define the promised set $E$. Let

$$\mathcal{G} = \{B \in \mathcal{A}: B \subset D \text{ and } v(B) = 0\}.$

(iii) if $f \in \mathcal{L}_1(X, \mathcal{A}, \nu)$ and $\{x \in X : f(x) \neq 0\}$ is $\sigma$-finite with respect to $\mu$, then $ff_0 \in \mathcal{L}_1(X, \mathcal{A}, \mu)$ and $\int_X f d\nu = \int_X ff_0 d\mu$.

Also $f_0$ is unique, in the sense that if $g_0$ is any nonnegative, extended real-valued, $\mathcal{A}$-measurable function on $X$ for which

(iv) $\nu(A) = \int_A g_0 d\mu$

for all $A \in \mathcal{A}$ such that $\mu(A) < \infty$, then $f_0 \xi_E$ and $g_0 \xi_E$ are equal $\mu$-a.e. for all $E \in \mathcal{A}$ that are $\sigma$-finite with respect to $\mu$.

Proof. For each $F \in \mathcal{F}$, the restriction of $\nu$ to $F$ is absolutely continuous with respect to the restriction of $\mu$ to $F$, and so by (19.26) there are sets $D_F$ and $E_F$ in $\mathcal{A}$ such that: $D_F \cap E_F = \varnothing; D_F \cup E_F = F$; (19.26.i) and (19.26.ii) hold for $E_F$; and $\nu$ is $\sigma$-finite on $D_F$. If $\nu$ is $\sigma$-finite on $F$, then we take $D_F = F$. Since $\nu$ is $\sigma$-finite on $D_F$ and $\mu$ is finite on $D_F$, we can apply (19.24) to assert that there is a nonnegative, finite-valued, $\mathcal{A}$-measurable function $f_0^{(F)}$ defined on $D_F$ such that the conclusions of (19.24) hold for $\mu$ and $\nu$ restricted to $D_F$. Now let $f_0$ be the function on $X$ such that for

Therefore

$$v(A \cap E_F) = \int_{A \cap E_F} \infty d\mu = \int_{A \cap E_F} f_0 d\mu .$$

Combining (3), (4), and (5), and harking back to (12.21), we find that

$$v(A) = \sum_{F \in \mathcal{F}_0} v(A \cap F) = \sum_{F \in \mathcal{F}_0} \int_{A \cap F} f_0 d\mu = \int_{A} f_0 d\mu .$$

Assertion (i) is now obvious, since both ends of (6) are countably additive.

The equality (ii) is proved by considering characteristic functions, then simple functions, and finally passing to the limit using (11.35) and (12.22). Equality (iii) follows upon writing $f$ as a linear combination of functions in $\mathfrak{L}_1^+ (X, \mathcal{A}, v)$.

It remains to prove the uniqueness of $f_0$. Let $g_0$ be as in (iv). Then for every $F \in \mathcal{F}$ and every $\mathcal{A}$-measurable subset $A$ of $D_F$, we have

$$v(A) = \int_{A} f_0 d\mu = \int_{A} g_0 d\mu ,$$

and so by (19.24), $f_0(x) = g_0(x)$ for $\mu$-almost all $x \in D_F$. Now assume that there exists a set $A \in \mathcal{A}$ such that $A \subset E_F$, $\mu(A) > 0$, and

$$g_0(x) < \infty = f_0(x)$ for all $x \in A$.

From (19.26.ii), we see that $v(A) > 0$. For each $n \in N$, write

$$A_n = \{x \in A : g_0(x) < n\}.$$

Then $(A_n)_{n=1}^{\infty}$ is a nondecreasing sequence and $\bigcup_{n=1}^{\infty} A_n

space $(X, \mathcal{M}_i, \iota)$ is decomposable in the sense of (19.25), and so we will be able to apply (19.27). The discussion is somewhat technical, unavoidably so in our opinion.
