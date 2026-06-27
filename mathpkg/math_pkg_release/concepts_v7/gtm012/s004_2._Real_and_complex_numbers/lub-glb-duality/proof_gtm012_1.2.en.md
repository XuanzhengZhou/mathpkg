---
role: proof
locale: en
of_concept: lub-glb-duality
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of Duality between Least Upper Bound and Greatest Lower Bound

Let $A \subset \mathbb{R}$ be a nonempty set that is bounded below. Define

$$B = \{ x \in \mathbb{R} \mid -x \in A \}.$$

In other words, $B = -A$, the set of negatives of elements of $A$.

**Step 1: $B$ is bounded above.** Since $A$ is bounded below, there exists $m \in \mathbb{R}$ such that $m \leq y$ for all $y \in A$. Then for any $x \in B$, we have $-x \in A$, so $m \leq -x$, which implies $x \leq -m$. Hence $-m$ is an upper bound for $B$.

**Step 2: Existence of $\operatorname{lub} B$.** By the completeness axiom O5, since $B$ is nonempty (as $A$ is nonempty) and bounded above, $B$ has a least upper bound; let $x = \operatorname{lub} B$.

**Step 3: $-x = \operatorname{glb} A$.** First, $-x$ is a lower bound for $A$: for any $y \in A$, we have $-y \in B$, so $-y \leq x$ (since $x$ is an upper bound for $B$), which gives $y \geq -x$. Second, if $z$ is any lower bound for $A$, then $z \leq y$ for all $y \in A$, so $-y \leq -z$ for all $y \in A$. This means $-z$ is an upper bound for $B$, so $x \leq -z$ (since $x$ is the least upper bound), which implies $z \leq -x$. Thus $-x$ is the greatest lower bound of $A$.

Therefore, the completeness axiom O5 (existence of least upper bounds) implies the existence of greatest lower bounds for nonempty sets bounded below, and conversely.
