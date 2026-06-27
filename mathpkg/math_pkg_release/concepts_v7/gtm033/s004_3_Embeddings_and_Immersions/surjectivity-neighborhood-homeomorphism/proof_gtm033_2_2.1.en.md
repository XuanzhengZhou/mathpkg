---
role: proof
locale: en
of_concept: surjectivity-neighborhood-homeomorphism
source_book: gtm033
source_chapter: "2. Function Spaces"
source_section: "2.1"
---

# Proof of Surjectivity Neighborhood of Homeomorphisms (Theorem 1.7)

**Theorem 1.7.** Let $M$ and $N$ be manifolds without boundary and $f: M \to N$ a homeomorphism. Then $f$ has a neighborhood of surjective maps in $C^0_S(M,N)$.

*Proof.* Let $g$ be near $f$; then $g^{-1}f$ is near the identity map of $M$. Hence it suffices to take $M = N$ and $f = 1_M$.

Let $\{\varphi_i, U_i\}_{i \in \Lambda}$ be a locally finite cover of $M$ by charts such that $\varphi_i(U_i) \supset D^n$, the closed unit ball in $\mathbb{R}^n$, and $M = \bigcup_i \varphi_i^{-1}(D^n)$. For each $i$ let $B_i \subset \varphi_i(U_i)$ be a slightly larger closed ball, $0 \in D^n \subset \operatorname{Int} B_i$.

It suffices to find $\varepsilon_i > 0$ such that if $h_i: B_i \to \mathbb{R}^n$ is a continuous map with $|h_i(x) - x| < \varepsilon_i$ for all $x \in B_i$, then $h_i(B_i) \supset D^n$. For if this is true, then the set of $g: M \to M$ satisfying, for all $i$,

$$g\varphi_i^{-1}(B_i) \subset U_i,$$

and

$$|\varphi_i g\varphi_i^{-1}(x) - x| < \varepsilon_i, \quad \text{for all } x \in B_i,$$

will consist of surjective maps (put $\varphi_i g\varphi_i^{-1} = h_i$).

Let $\varepsilon_i > 0$ be so small that for any $z \in D^n$, $x \in \partial B_i$ and $y \in \mathbb{R}^n$ with $|y - z| < \varepsilon_i$, we have $|x - z| < |x - y|$.

Now suppose, for contradiction, that $z \in D^n - h_i(B_i)$. Define a map $H: B_i \to S^{n-1} = \partial B_i$ by sending $x \in B_i$ to the unique point where the ray from $h_i(x)$ through $z$ meets $\partial B_i$. More precisely, define $H(x)$ as the unique point on $\partial B_i$ such that $z$ lies on the line segment between $h_i(x)$ and $H(x)$. The homotopy $H_t(x) = (1-t)x + tH(x)$ extends $H$ to a map of the ball $B_i$ into itself that is the identity on $\partial B_i$. Composing with radial projection, one obtains a map of $S^{n-1}$ to itself that extends to the $n$-ball and restricts to the identity on the boundary.

A classical theorem of topology (Theorem 1.3.4 in the book, proved by degree theory) states that no map of an $(n-1)$-sphere to itself which extends to a map of the $n$-ball to the sphere can be homotopic to the identity. This contradiction shows that $D^n \subset h_i(B_i)$.

Since every point of $M$ lies in some $\varphi_i^{-1}(D^n)$, and $D^n \subset h_i(B_i)$ for each $i$, the map $g$ is surjective.

$\square$

**Remark.** The key topological fact used is that the identity map on $S^{n-1}$ does not extend to a map $D^n \to S^{n-1}$ (i.e., $S^{n-1}$ is not a retract of $D^n$). This follows from degree theory or the Brouwer fixed point theorem.
