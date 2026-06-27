---
role: proof
locale: en
of_concept: tangent-hyperplane-criterion
source_book: gtm015
source_chapter: "3"
source_section: "30"
---

# Proof of Criterion for existence of a tangent hyperplane

Let $E$ be a real vector space, $A$ a nonempty subset of $E$, $g$ a nonzero linear form, and $M = \{x : g(x) = 0\}$. In order that $A$ admit a tangent hyperplane parallel to $M$, it is necessary and sufficient that $g(A)$ contain a largest element or a smallest element.

Suppose there exists a hyperplane $H$ that is tangent to $A$ and parallel to $M$. Say $H = \{x : g(x) = \alpha\}$. If, for instance, $g \ge \alpha$ on $A$, then $g(A)$ has a smallest element (namely, $\alpha$). Similarly, if $g \le \alpha$ on $A$, then $g(A)$ has a largest element.

Conversely, suppose $g(A)$ has, say, a smallest element $\alpha$. Choose any $a \in A$ with $g(a) = \alpha$. Then $g \ge \alpha$ on $A$, thus the hyperplane $H = \{x : g(x) = \alpha\}$ is tangent to $A$.
