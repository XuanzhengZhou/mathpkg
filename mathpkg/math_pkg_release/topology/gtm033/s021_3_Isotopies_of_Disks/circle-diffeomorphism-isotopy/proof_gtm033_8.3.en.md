---
role: proof
locale: en
of_concept: circle-diffeomorphism-isotopy
source_book: gtm033
source_chapter: "8"
source_section: "3"
---

# Proof of Theorem 3.3 (Classification of Circle Diffeomorphisms up to Isotopy)

Every diffeomorphism $f: S^1 \to S^1$ is isotopic to the identity if $\deg f = 1$, and isotopic to complex conjugation $\delta: S^1 \to S^1$ if $\deg f = -1$.

**Proof.** Let $f: S^1 \to S^1$ be a diffeomorphism. First suppose $f$ has degree $1$. By a preliminary isotopy we may assume $f$ is the identity on some open interval $J \subset S^1$. Let $J' \subset S^1$ be an open interval such that $J \cup J' = S^1$. Identify $J'$ with an interval of real numbers. An isotopy from $f$ to the identity is given by

$$f_t(x) = \begin{cases} x & \text{if } x \in J \\ t x + (1-t)f(x) & \text{if } x \in J' \end{cases}.$$

Now suppose $\deg f = -1$. Let $\delta: S^1 \to S^1$ be complex conjugation (which has degree $-1$). Then $\deg(f\delta) = 1$, so $f\delta$ is isotopic to the identity by an isotopy $g_t$. Then $g_t \delta$ is an isotopy from $f$ to $\delta$. $\square$
