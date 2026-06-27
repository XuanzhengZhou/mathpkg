---
role: proof
locale: en
of_concept: uniqueness-of-identity-arrow
source_book: gtm005
source_chapter: "I"
source_section: "1"
---

Suppose $e, e': a \to a$ are both two-sided identities at object $a$. Then:
$$e = e \circ e' = e'.$$
The first equality uses that $e'$ is a right identity (for any $f: a \to x$, $f \circ e' = f$ — wait, no. Let me be precise):

If $e$ and $e'$ both satisfy the identity axioms:
- For all $f: a \to x$: $f \circ e = f$ and $f \circ e' = f$ (right identity on $a$)
- For all $g: x \to a$: $e \circ g = g$ and $e' \circ g = g$ (left identity on $a$)

Then $e = e \circ e'$ (since $e'$ acts as left identity for arrows into $a$: $e' \circ g = g$, but here $e: a \to a$, so we use the right identity property for $e'$) — more carefully:

Apply the left identity property of $e'$ to $e: a \to a$: $e' \circ e = e$. Wait, that gives $e' \circ e = e$.

Apply the right identity property of $e$ to $e': a \to a$: $e' \circ e = e'$. 

Thus $e = e' \circ e = e'$. The identity arrow at each object is uniquely determined by the axioms.
