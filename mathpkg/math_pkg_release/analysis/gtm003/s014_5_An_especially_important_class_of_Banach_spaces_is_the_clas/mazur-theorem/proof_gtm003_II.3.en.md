---
role: proof
locale: en
of_concept: mazur-theorem
source_book: gtm003
source_chapter: "II"
source_section: "3"
---

After a translation, if necessary, we can assume $0 \in M$, so that $M$ is a subspace of $L$. Consider the set $\mathcal{M}$ of all closed real subspaces of $L$ that contain $M$ and do not intersect $A$. Order $\mathcal{M}$ by inclusion. By Zorn's Lemma, $\mathcal{M}$ contains a maximal element $H_0$. We claim $H_0$ is a closed hyperplane.

Suppose $H_0$ is not a hyperplane. Then the quotient space $L/H_0$ has dimension at least 2. Let $\pi: L \to L/H_0$ be the canonical quotient map. Since $A$ is open and convex and $A \cap H_0 = \varnothing$, the image $\pi(A)$ is an open, convex subset of $L/H_0$ not containing $0$. Pick any two-dimensional subspace $E$ of $L/H_0$ and let $B = E \cap \pi(A)$.

If $B = \varnothing$, any 1-codimensional subspace of $E$ (lifted back to $L$) would contradict maximality. So assume $B \neq \varnothing$. $B$ is a convex, open subset of $E$ not containing $0$. Identify $E$ with $\mathbb{R}^2$. Project $B$ onto the unit circle $C$ of $E$ by the mapping
$$f: (x, y) \mapsto \left( \frac{x}{r}, \frac{y}{r} \right), \quad r = (x^2 + y^2)^{1/2}.$$

Since $B$ is convex and connected, $f(B)$ is connected, for $f$ is continuous on $B$. Moreover, $f(B)$ is an open subset of $C$. Hence $f(B)$ is an open arc on $C$ which subtends an angle $\leq \pi$ at $0$; otherwise, there would exist points in $B$ whose images under $f$ are antipodal, contradicting the hypothesis $0 \notin B$ (since $B$ is convex). Consequently, there exists a straight line in $E$ passing through $0$ and not intersecting $B$. The preimage of this line under $\pi$ gives a closed subspace of $L$ strictly larger than $H_0$ but still not intersecting $A$, contradicting the maximality of $H_0$.

Therefore $H_0$ is a closed hyperplane in $L$, containing $M$ and not intersecting $A$.
