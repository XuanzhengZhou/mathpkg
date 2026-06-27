---
role: proof
locale: en
of_concept: existence-uniqueness-free-t-algebra
source_book: gtm022
source_chapter: "2"
source_section: "2"
---

**Proof. (a) Uniqueness.** We show first that if $\psi: F \to F$ is a homomorphism such that $\psi \sigma = \sigma$, then $\psi = 1_F$. Indeed, by the universal property of $(F, \sigma)$, the identity $1_F: F \to F$ is the unique homomorphism satisfying $1_F \sigma = \sigma$. Since $\psi$ also satisfies this condition, we must have $\psi = 1_F$.

Now let $(F, \sigma)$ and $(F', \sigma')$ be free on $X$.

Since $(F, \sigma)$ is free, there exists a homomorphism $\varphi: F \rightarrow F'$ such that $\varphi \sigma = \sigma'$. Since $(F', \sigma')$ is free, there exists a homomorphism $\varphi': F' \rightarrow F$ such that $\varphi' \sigma' = \sigma$. Hence $\varphi' \varphi \sigma = \varphi' \sigma' = \sigma$, and by the result above, $\varphi' \varphi = 1_F$. Similarly, $\varphi \varphi' = 1_{F'}$. Thus $\varphi, \varphi'$ are mutually inverse isomorphisms, and so uniqueness is proved.

**(b) Existence.** An algebra $F$ will be constructed as a union of sets $F_n$ ($n \in \mathbb{N}$), which are defined inductively as follows.

(i) $F_0$ is the disjoint union of $X$ and $T_0$ (the set of 0-ary operation symbols).

(ii) Assume $F_r$ is defined for $0 \leqslant r < n$. Then define

$$F_n = \left\{(t, a_1, \ldots, a_k) \mid t \in T,\ \operatorname{ar}(t) = k,\ a_i \in F_{r_i},\ \sum_{i=1}^{k} r_i = n-1 \right\}.$$

(iii) Put $F = \bigcup_{n \in \mathbb{N}} F_n$.

The set $F$ is now given. To make it into a $T$-algebra, we must specify the action of the operations $t \in T$.

(iv) If $t \in T_k$ and $a_1, \ldots, a_k \in F$, put $t(a_1, \ldots, a_k) = (t, a_1, \ldots, a_k)$. In particular, if $t \in T_0$, then $t_F$ is the element $t$ of $F_0$.

This makes $F$ into a $T$-algebra. To complete the construction, we must give the map $\sigma: X \rightarrow F$.

(v) For $x \in X$, define $\sigma(x) = x$, regarding $X$ as a subset of $F_0$ and hence of $F$.

We now verify that $(F, \sigma)$ satisfies the universal property. Let $A$ be any $T$-algebra and $\tau: X \to A$ any function. We construct a homomorphism $\varphi: F \to A$ satisfying $\varphi \sigma = \tau$ by induction on the layers $F_n$.

Define $\varphi_0: F_0 \to A$ by:
- $\varphi_0(x) = \tau(x)$ for $x \in X$,
- $\varphi_0(t) = t_A$ (the interpretation of the 0-ary operation $t$ in $A$) for $t \in T_0$.

Thus $\varphi_0: F_0 \rightarrow A$ is defined, and is uniquely determined by the conditions to be satisfied by $\varphi$.

Suppose that $\varphi_k$ is defined and uniquely determined for $k < n$. An element of $F_n$ ($n > 0$) is of the form $(t, a_1, \ldots, a_k)$, where $t \in T_k$, $a_i \in F_{r_i}$ and $\sum_{i=1}^{k} r_i = n - 1$. Thus $\varphi_{r_i}(a_i)$ is already uniquely defined for $i = 1, \ldots, k$.

Furthermore, since $(t, a_1, \ldots, a_k) = t(a_1, \ldots, a_k)$, and since the homomorphism property of $\varphi$ requires that

$$\varphi(t, a_1, \ldots, a_k) = t(\varphi(a_1), \ldots, \varphi(a_k)),$$

we must define

$$\varphi_n(t, a_1, \ldots, a_k) = t(\varphi_{r_1}(a_1), \ldots, \varphi_{r_k}(a_k)).$$

This determines $\varphi_n$ uniquely, and as each element of $F$ belongs to exactly one subset $F_n$, on putting $\varphi(\alpha) = \varphi_n(\alpha)$ for $\alpha \in F_n$ ($n \geqslant 0$), we see that $\varphi$ is a homomorphism from $F$ to $A$ satisfying $\varphi\sigma(x) = \varphi_0(x) = \tau(x)$ for all $x \in X$ as required, and that $\varphi$ is the only such homomorphism.

Thus $(F, \sigma)$ is a free $T$-algebra on $X$. $\square$
