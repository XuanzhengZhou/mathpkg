---
role: proof
locale: en
of_concept: closure-of-balanced-set-is-balanced
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "17. Balanced sets, absorbent sets"
---

# Proof that the Closure of a Balanced Set is Balanced

**Theorem (17.5).** In a TVS, the closure of a balanced set is balanced.

*Proof.* Suppose $A$ is a balanced subset of the TVS $E$ over $\mathbb{K}$. Let $\lambda \in \mathbb{K}$, $|\lambda| \leq 1$. Then $\lambda A \subset A$ by definition of balanced, and the problem is to show that $\lambda \overline{A} \subset \overline{A}$.

The mapping $x \mapsto \lambda x$ ($x \in E$) is continuous. For any continuous function $f$, we have $f(\overline{A}) \subset \overline{f(A)}$. Applying this to $f(x) = \lambda x$, we obtain

$$\lambda \overline{A} = f(\overline{A}) \subset \overline{f(A)} = \overline{\lambda A} \subset \overline{A},$$

which completes the proof. $\square$
