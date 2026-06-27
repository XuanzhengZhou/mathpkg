---
role: proof
locale: en
of_concept: existence-uniqueness-free-t-algebra
source_book: gtm022
source_chapter: "I"
source_section: "§2 Free Algebras"
---

**Proof.**

**(a) Uniqueness.** First we show that if $(F, \sigma)$ is free on $X$, then the identity homomorphism $1_F: F \to F$ is the unique homomorphism $\varphi: F \to F$ satisfying $\varphi\sigma = \sigma$.

Now let $(F, \sigma)$ and $(F', \sigma')$ be free on $X$. Since $(F, \sigma)$ is free, there exists a homomorphism $\varphi: F \to F'$ such that $\varphi\sigma = \sigma'$. Since $(F', \sigma')$ is free, there exists a homomorphism $\varphi': F' \to F$ such that $\varphi'\sigma' = \sigma$. Hence $\varphi'\varphi\sigma = \varphi'\sigma' = \sigma$, and by the result above, $\varphi'\varphi = 1_F$. Similarly, $\varphi\varphi' = 1_{F'}$. Thus $\varphi, \varphi'$ are mutually inverse isomorphisms, and so uniqueness is proved.

**(b) Existence.** An algebra $F$ will be constructed as a union of sets $F_n$ $(n \in \mathbb{N})$, which are defined inductively as follows.

(i) $F_0$ is the disjoint union of $X$ and $T_0$.

(ii) Assume $F_r$ is defined for $0 \leqslant r < n$. Then define

$$F_n = \left\{(t, a_1, \ldots, a_k) \mid t \in T,\ \text{ar}(t) = k,\ a_i \in F_{r_i},\ \sum_{i=1}^{k} r_i = n-1 \right\}.$$

(iii) Put $F = \bigcup_{n \in \mathbb{N}} F_n$.

The set $F$ is now given. To make it into a $T$-algebra, we must specify the action of the operations $t \in T$.

(iv) If $t \in T_k$ and $a_1, \ldots, a_k \in F$, put $t(a_1, \ldots, a_k) = (t, a_1, \ldots, a_k)$. In particular, if $t \in T_0$, then $t_F$ is the element $t$ of $F_0$.

This makes $F$ into a $T$-algebra. To complete the construction, we must give the map $\sigma: X \to F$.

(v) For $x \in X$, define $\sigma(x) = x$, regarding $x$ as an element of $F_0 \subseteq F$.

Finally, we verify the universal property. Let $A$ be any $T$-algebra and $\tau: X \to A$ any function. We construct $\varphi: F \to A$ by induction on the layers $F_n$.

Define $\varphi_0: F_0 \to A$ by $\varphi_0(x) = \tau(x)$ for $x \in X$, and for $t \in T_0$, define $\varphi_0(t) = t_A$ (the interpretation of the nullary operation $t$ in $A$). Thus $\varphi_0: F_0 \to A$ is defined, and is uniquely determined by the conditions to be satisfied by $\varphi$.

Suppose that $\varphi_k$ is defined and uniquely determined for $k < n$. An element of $F_n$ $(n > 0)$ is of the form $(t, a_1, \ldots, a_k)$, where $t \in T_k$, $a_i \in F_{r_i}$ and $\sum_{i=1}^{k} r_i = n - 1$. Thus $\varphi_{r_i}(a_i)$ is already uniquely defined for $i = 1, \ldots, k$.

Furthermore, since $(t, a_1, \ldots, a_k) = t(a_1, \ldots, a_k)$, and since the homomorphism property of $\varphi$ requires that

$$\varphi(t, a_1, \ldots, a_k) = t(\varphi(a_1), \ldots, \varphi(a_k)),$$

we must define

$$\varphi_n(t, a_1, \ldots, a_k) = t(\varphi_{r_1}(a_1), \ldots, \varphi_{r_k}(a_k)).$$

This determines $\varphi_n$ uniquely, and as each element of $F$ belongs to exactly one subset $F_n$, on putting $\varphi(\alpha) = \varphi_n(\alpha)$ for $\alpha \in F_n$ $(n \geqslant 0)$, we see that $\varphi$ is a homomorphism from $F$ to $A$ satisfying $\varphi\sigma(x) = \varphi_0(x) = \tau(x)$ for all $x \in X$ as required, and that $\varphi$ is the only such homomorphism.
