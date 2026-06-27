---
role: proof
locale: en
of_concept: rules-for-members-abelian-category
source_book: gtm005
source_chapter: "VIII"
source_section: "4"
---

Rules (i) and (ii) are just the definition of a monic arrow translated into the language of members. For a monic $f$, $f x \equiv 0$ means there exist epis $u, v$ with $f x u = 0 v = 0$, so $f (x u) = 0$, and since $f$ is monic, $x u = 0$, implying $x \equiv 0$. The converse is similar. Rule (ii) follows from the fact that $f x \equiv f y$ implies $f (x u - y v) = 0$ for suitable epis $u, v$, and monicness of $f$ then gives $x u \equiv y v$.

For rule (iii): if $g$ is epi, then for any $z \in_m c$, one can construct $y \in_m b$ with $g y \equiv z$ by forming the pullback of $g$ along $z$ using Proposition 2 (the pullback of an epi is epi). Conversely, if $g$ is not epi, the member $1_c \in_m c$ is not of the form $g y \equiv 1_c$ for any $y \in_m b$, since $g y \equiv 1_c$ would mean there exist epis $u, v$ with $g y u = 1_c v$, implying $g$ is split epi, hence epi.

Rule (iv) is trivial: $h$ is the zero arrow iff it factors through the null object, which is equivalent to $h x \equiv 0$ for all members $x$.

For rule (v): take the standard factorization $f = m e$ with $m = \ker g$ (since the sequence is exact at $b$). If $g y \equiv 0$, then $y$ factors through $m = \ker g$, i.e., $y \equiv m y_1$ for some $y_1$. Using the pullback along $e$ (which is epi), one shows $y_1 \equiv e x$ for some $x$, giving $y \equiv m e x = f x$. Conversely, the condition implies $\operatorname{im} f = \ker g$, hence exactness.

For rule (vi) (Subtraction): given $g x \equiv g y$, there exist epis $u, v$ with $g x u = g y v$. Since the category is abelian, we can form the difference $x u - y v$ (using the abelian group structure on hom-sets). Choose $z$ as the morphism representing $x u - y v$; then $g z \equiv 0$. For any $f$ with $f x \equiv 0$, we have $f x u = 0$, and $f y v = f(x u - (x u - y v)) = f z w$ for suitable epis $w$, yielding $f y \equiv f z$. The dual statement for $h$ follows similarly using the additive inverse.
