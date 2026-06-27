---
role: proof
locale: en
of_concept: augmentation-ideal-of-infinite-cyclic-group
source_book: gtm004
source_chapter: "VI. Cohomology of Groups"
source_section: "5. The Augmentation Ideal, Derivations, and the Semi-Direct Product"
---

# Proof of Augmentation Ideal of the Infinite Cyclic Group is Free

**Theorem 5.5.** Let $C$ be the infinite cyclic group with generator $t$. Then the augmentation ideal $IC$ is $C$-free on the single element $t-1$.

*Proof.* Let $C$ be the infinite cyclic group freely generated (as a group) by $t$. Then every element of $C$ is of the form $t^n$ for $n \in \mathbb{Z}$. Let $M$ be an arbitrary $C$-module and let $f: \{t\} \to M$ be any set function from the singleton generator set into $M$. Since $C$ is free on $\{t\}$, we may define a group homomorphism

$$\bar{f}: C \to M \rtimes C$$

by setting $\bar{f}(t) = (f(t), t)$ on the generator and extending multiplicatively. Explicitly, for $n \geq 0$,

$$\bar{f}(t^n) = \left(\sum_{i=0}^{n-1} t^i f(t),\, t^n\right),$$

and for negative $n$ the formula extends accordingly using the semi-direct product structure.

By Corollary 5.4, the group homomorphism $\bar{f}$ determines a derivation $d: C \to M$ given by $d = q \bar{f}$, where $q: M \rtimes C \to M$ is the projection $q(a, c) = a$. On the generator $t$, this derivation satisfies

$$d(t) = q \bar{f}(t) = q(f(t), t) = f(t).$$

Now apply Theorem 5.1 to the derivation $d$. This yields a $C$-module homomorphism

$$\varphi: IC \to M$$

defined on the generators $x-1$ of $IC$ by $\varphi(x-1) = d(x)$. In particular, on the element $t-1$ we have

$$\varphi(t-1) = d(t) = f(t).$$

Thus, every function from the singleton set $\{t-1\}$ to an arbitrary $C$-module $M$ extends uniquely to a $C$-module homomorphism $IC \to M$. This is precisely the universal property that characterizes $IC$ as a free $C$-module with basis $\{t-1\}$. Hence $IC$ is $C$-free on $t-1$. $\square$
