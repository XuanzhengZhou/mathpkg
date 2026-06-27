---
role: exercise
locale: en
chapter: "5"
section: "20"
exercise_number: 37
---

Let $X$ be a nonvoid set and let $U$ be a family of subsets of $X$.

(a) Prove that $U$ has the following properties:

(i) $\varnothing \notin U$;
(ii) if $A \in U$ and $A \subset B \subset X$, then $B \in U$;
(iii) if $A, B \in U$, then $A \cap B \in U$;
(iv) if $A \subset X$, then $A \in U$ or $A' \in U$.

Any family $U$ that satisfies (i)-(iii) is called a filter in $X$. A filter in $X$ satisfying (iv) is called an ultrafilter in $X$.

(b) Prove that if $V$ is any ultrafilter in $X$ and if $\sigma$ is defined on $P(X)$ by

$$\sigma(A) = \begin{cases} 1 & \text{if } A \in V, \\ 0 & \text{if } A \notin V, \end{cases}$$

then $\sigma$ is a finitely additive measure on $(X, P(X))$.

Thus we have set up a one-to-one correspondence between ultrafilters and finitely additive zero-one measures.

(c) Let $(X, \mathcal{A}, \mu)$ be any measure space and let $\tau$ be a finitely additive measure in $F(X, \mathcal{A}, \mu)$. Prove that

$$\int_X f g d\tau = \int_X f d\tau \cdot \int_X g d\tau$$

for all $f, g \in \mathfrak{L}_\infty$ if and only if $\tau(A) = 0$ or $1$ for all $A \in \mathcal{A}$.
