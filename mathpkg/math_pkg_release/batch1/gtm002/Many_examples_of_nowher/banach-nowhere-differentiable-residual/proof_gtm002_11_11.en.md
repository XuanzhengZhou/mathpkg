---
role: proof
locale: en
of_concept: banach-nowhere-differentiable-residual
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

The set $E = \bigcup_n E_n$ of functions with bounded right difference quotients at some point of $[0,1)$ is of first category in $C$. By the same reasoning applied to the isometry induced by $x \mapsto 1-x$, the set of functions with bounded left difference quotients at some point of $(0,1]$ is also of first category.

The union of these two first-category sets is again of first category. Now, any function $f \in C$ that has a finite one-sided derivative at some point must, in particular, have bounded one-sided difference quotients at that point (since the existence of a finite limit $(f(x+h)-f(x))/h$ as $h \to 0^+$ implies boundedness of the difference quotient for small $h$). Therefore, the set of functions possessing a finite one-sided derivative somewhere in $[0,1]$ is contained in the union of the two first-category sets, and is itself of first category.

Its complement in the complete metric space $C$ is therefore a residual set (a dense $G_\delta$ set, by the Baire category theorem). Functions in this residual set have no finite one-sided derivative at any point, i.e., they are nowhere differentiable in the strongest possible sense.
