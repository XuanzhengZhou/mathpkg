---
role: proof
locale: en
of_concept: "let-be-any-complex--or-extended-real-valued--measurable"
source_book: gtm025
source_chapter: "Measurable Functions"
source_section: "11.35"
---

First consider the case $f \geq 0$. For each $n \in N$ and for $1 \leq k \leq n \cdot 2^n$, let

$$A_{n,k} = \left\{x \in X : \frac{k-1}{2^n} \leq f(x) < \frac{k}{2^n}\right\},$$

and

$$B_n = \{x \in X : f(x) \geq n\}.$$

Define

$$s_n(x) = \sum_{k=1}^{n \cdot 2^n} \frac{k-1}{2^n} \xi_{A_{n,k}}(x) + n \xi_{B_n}(x).$$

It is

such that $\iota(\{x \in X : f(x) \neq g(x)\}) < \varepsilon$. Moreover if $\|f\|_u < \infty$, then $g$ can be selected so that $\|g\|_u \leq \|f\|_u$.

Proof. Let $\varepsilon > 0$ be given. Use (9.24) to select an open set $U$ such that $E \subset U$ and $\iota(U) < \iota(E) + \frac{\varepsilon}{4}$. The set $U$ is fixed throughout the proof.

(I) Suppose that $f = \xi_A$. Then $A \subset E$ and $A$ is $\iota$-measurable. Since $\iota(A) < \infty$, we may apply (10.30) to find a compact set $F$ such that $F \subset A$ and $\iota(A \cap F') < \frac{\varepsilon}{2}$. Next use (9.24) and (6.79) to produce an open set $V$ with compact closure such that $F \subset V \subset U$ and $\iota(V \cap F') < \frac{\varepsilon}{2}$. Use (6.80) to obtain a continuous function $g$ from $X$ into $[0, 1]$ such that $g(x) = 1$ for all $x \in F$ and $g(x) = 0$ for all $x \in V'$. Then we have: $g \in \mathfrak{C}_{00}(X)$, $g = 0$ on $U'$, and $\{x \in X : f(x) \neq g(x)\} \subset (V \cap F') \cup (A \cap F')$. It follows that

$$\iota(\{x \in X : f(x) \neq g(x)\}) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon,$$

and so the proof is complete if $f = \xi_A$.

(II) Consider next the case that $f$ is a simple function, say $f = \sum_{k=1}^{n} \alpha

$F \subset B$ such that $\iota(B \cap F') < \frac{\varepsilon}{4}$. Plainly $g_n \rightarrow f$ uniformly on $F \cup U'$ [recall that $g_n = f = 0$ on $U'$]. Since each $g_n$ is continuous, it follows from (7.9) that $f$ is continuous on $F \cup U'$ [in the relative topology]. Applying the Tietze extension theorem (7.40), for the compact set $F$ and its open superset $U$, we find a function $g \in \mathfrak{C}_{00}(X)$ such that $f(x) = g(x)$ for all $x \in F \cup U'$. We have

$$\{x \in X : f(x) \neq g(x)\} \subset U \cap F' = A \cup (U \cap A' \cap B') \cup (B \cap F'),$$

and so

$$\iota(\{x \in X : f(x) \neq g(x)\}) \leq \iota(A) + \iota(U \cap A' \cap B') + \iota(B \cap F')$$

$$< \frac{\varepsilon}{4} + \frac{\varepsilon}{4} + \frac{\varepsilon}{4} < \varepsilon.$$

Finally, suppose that $\|f\|_u < \infty$ and $\|g\|_u > \|f\|_u$. This is certainly possible. In this case we tamper a little with $g$ to obtain the desired conclusion. Let $S = \{z \in K : |z| \leq \|f\|_u\}$ and $T = \{z \in K : |z| \leq \|g\|_u\}$. Define a mapping $\varphi$ from $T$ onto $S$ as follows:

$$\varphi(z) = \begin{cases} z & \text{if } z \in S \\ \frac{z}{|z|} \cdot \|f\|_u & \text{if } z \in T \cap S'. \end{cases}$$

It is easy to see that $\varphi

and $\mu(Y) = \inf\{\mu(U) : U \text{ is open in the topology of } D, U \supset Y\}$ for all $Y \in \mathcal{B}(D)$. That is, $(D, \mathcal{B}(D), \mu)$ is irregular, although "outer" regular. [Hints. Construct a subset $D$ of $[0, 1]$ such that $D \cap F \neq \emptyset \neq D' \cap F$ for every uncountable closed set $F \subset [0, 1]$: see (10.54.b). Then $D$ is non $\lambda$-measurable, and so $0 < \lambda(D) \leq 1$. Let $X$ be a $G_{\delta}$ set such that $D \subset X \subset [0, 1]$ and $\lambda(X) = \lambda(D)$. Then every $\lambda$-measurable subset of $X \cap D'$ has $\lambda$-measure 0, and we may take $\mu$ to be $\left(\frac{1}{\lambda(D)}\lambda\right)^{\dagger}$ as in part (a). All of the claims made for $\mu$ are easy to verify. Compare this result with (10.58).]

**(11.40) Exercise: Extending a measure.** Let $(X, \mathcal{A}, \mu)$ be a measure space. Let $\mathcal{S}$ be a subfamily of $\mathcal{P}(X)$ such that:

(i) $P \in \mathcal{S} \cap \mathcal{A}$ implies $\mu(P) = 0$;

(ii) $P_1, P_2, P_3, \ldots \in \mathcal{S}$ imply $\bigcup_{n=1}^{\infty} P_n \in \mathcal{S}$.

Let $\mathcal{A}^*$ be the family of all subsets $A^*$ of $X$ such that the symmetric difference $A^* \triangle A$ is in $\mathcal{S}$ for some $A \in \mathcal{A}$. For such a set $A^*$, let $\mu^*(A^*) = \mu(A)$.

(a) Prove that

uniformly on no subinterval of $[0, 1]$. [Make $f$ discontinuous on a dense set.]

(b) Use the sequence constructed in (a) to show that the conclusion of (11.42) fails for the measure space $([0, 1], \mathcal{P}([0, 1]), \nu)$ where $\nu$ is counting measure on $[0, 1]$ (10.4.a). [Show that the $E_k$'s can be taken closed and apply Baire's category theorem (6.54).]

(c) Show that there is a sequence $(f_n) \subset \mathcal{C}([0, 1])$ such that $f_n(x) \rightarrow 0$ for every $x \in [0, 1]$ but $f_n \rightarrow 0$ uniformly on no subinterval of $[0, 1]$. [For each $n \in N$, let $F_n$ be the set of all numbers in $]0, 1]$ having the form $\frac{k}{2^m}$ for an integer $k$ and an integer $m \in \{0, 1, \ldots, n\}$. Let $f_n$ be zero on $F_n$. For $\frac{k}{2^m} \in F_n$, where $k$ is odd, let $f_n\left(\frac{k}{2^m} - \frac{1}{2^{n+1}}\right) = \frac{1}{2^m}$. Let $f_n$ be linear in all subintervals of $[0, 1]$ where it is not yet defined.]

(11.44) Exercise. Let $X$ be a locally compact Hausdorff space and let $\iota$ be a measure on $X$ as in §9. Suppose that $f$ is a complex-valued $\mathcal{M}_i$-measurable function on $X$ such that $\{x \in X : f(x) \neq 0\}$ is $\sigma$-finite with respect to $\iota$. Prove that there exists a Borel measurable function $g$ on $X$ such that $|g| \leq |f|$ and $\iota(\{x

Let $\mathcal{B}_0(X)$ be the smallest $\sigma$-algebra of subsets of $X$ that contains all sets of the form $\{x \in X : f(x) = 0\}$, where $f$ is a continuous complex-valued function on $X$. The sets in $\mathcal{B}_0(X)$ are called the Baire sets of $X$.

(d) Prove that $f \in \Re(X)$ if and only if $f$ is a complex-valued function on $X$ and $f$ is $\mathcal{B}_0(X)$-measurable. [For the "if" statement, first show that $\{E \subset X : \xi_E \in \Re(X)\} = \mathcal{B}_0(X)$, and then use (11.35). For the "only if" statement use (b) and transfinite induction.]

(e) Prove that $\mathcal{B}_0(X) = \mathcal{B}(X)$ if $X$ is a metric space [use (6.86)].

§ 12. The abstract Lebesgue integral

This is perhaps the most important single section in the entire book. In it we construct, and study the remarkable properties of, the Lebesgue integral on an arbitrary measure space. It turns out that this integral is equal to the functional $\bar{I}$ for all nonnegative measurable functions when the measure space is $(X, \mathcal{M}, \iota)$. Throughout the present section, $(X, \mathcal{A}, \mu)$ denotes an arbitrary measure space, except where further restrictions are explicitly stated. The symbol $\mathfrak{S}$ denotes all simple, $\mathcal{A}$-measurable functions on $X$ that are complex- or extended real-valued; $\mathfrak{S}^+$ is as usual the set of all nonnegative functions in $\mathfrak{S}$.
