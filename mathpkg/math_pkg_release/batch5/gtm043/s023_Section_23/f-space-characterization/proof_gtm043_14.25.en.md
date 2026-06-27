---
role: proof
locale: en
of_concept: f-space-characterization
source_book: gtm043
source_chapter: "14"
source_section: "23"
---

The prime ideals contained in $M^p$ are just those containing $O^p$. Hence if $O^p$ is prime, the prime ideals contained in $M^p$ form a chain (14.8(a)). Conversely, if they form a chain, then their intersection, which is $O^p$, is prime (14.2(a)). Thus, (1) is equivalent to (2).

The equivalence of (1) with (3) is a special case of Theorem 2.9. Since completely separated sets in $X$ have disjoint closures in $\beta X$, it is clear that (3) is equivalent to (4). The equivalence of (4) with (5) was pointed out in Corollary 14.22. Thus, the conditions (1) to (5) are mutually equivalent.

Next, we establish the cycle $(4) \rightarrow (6) \rightarrow (7) \rightarrow (8) \rightarrow (9) \rightarrow (4)$, from which it will follow that (1) to (9) are mutually equivalent.

(4) implies (6). To show that $X - Z(h)$ is $C^*$-embedded in $X$, we apply the Urysohn extension theorem (1.17): we consider any two completely separated sets $A$ and $B$ in $X - Z(h)$, and prove that they are completely separated in $X$. There exists $k \in C^*(X - Z(h))$ such that $k$ is positive on $A$ and negative on $B$. Define $f$ as follows:

$$f(x) = 0 \quad (x \in Z(h)),$$
$$f(x) = k(x)|h(x)| \quad (x \in X - Z(h)).$$

Since $k$ is bounded, $f$ is continuous on all of $X$. Obviously, $A \subset \operatorname{pos} f$ and $B \subset \operatorname{neg} f$. The hypothesis now implies that $A$ and $B$ are completely separated in $X$.

(6) implies (7). Given $0 \leq f \leq g$ in $C(X)$, we are to prove that $f$ is a multiple of $g$. The condition shows that the cozero-set $\operatorname{coz} g$ is $C^*$-embedded, and using the structure of $C(\operatorname{coz} g)$, one obtains the desired divisibility.

The remaining implications complete the cycle, establishing the equivalence of all conditions. The corresponding condition holds in $C^*$. Consequently, (9) is equivalent to (10).
