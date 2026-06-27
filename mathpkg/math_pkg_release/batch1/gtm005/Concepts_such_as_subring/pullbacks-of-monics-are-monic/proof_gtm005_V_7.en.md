---
role: proof
locale: en
of_concept: pullbacks-of-monics-are-monic
source_book: gtm005
source_chapter: "V"
source_section: "7. Subobjects and Generators"
---

Consider a parallel pair $h, k$ with $f' h = f' k$. Then $g f' h = g f' k$, so by commutativity of the pullback square, $f g' h = f g' k$. Since $f$ is monic, this gives $g' h = g' k$. But we also have $f' h = f' k$. These two equations $g' h = g' k$ and $f' h = f' k$, together with the universal property of the pullback $p$, imply $h = k$. Therefore $f'$ is monic.

The dual statement (if $g$ is monic then $g'$ is monic) follows by symmetry of the pullback diagram.
