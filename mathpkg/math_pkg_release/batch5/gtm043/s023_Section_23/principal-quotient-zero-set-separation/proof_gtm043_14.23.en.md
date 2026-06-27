---
role: proof
locale: en
of_concept: principal-quotient-zero-set-separation
source_book: gtm043
source_chapter: "14"
source_section: "23"
---

By hypothesis, there exists $d \in C$ for which

$$(I(f), I(|f|)) = (I(d)).$$

Hence there exist $g, h, s, t \in C$ such that

$$f \equiv gd \pmod{I}, \quad |f| \equiv hd \pmod{I},$$

and

$$sf + t|f| \equiv d \pmod{I}.$$

Now, congruence modulo $I$ implies equality on some zero-set of $I$. We can therefore find a zero-set $Z \in Z[I]$ on which all three of the above congruences reduce to equalities:

(a) $$f(x) = g(x)d(x), \quad |f(x)| = h(x)d(x), \quad \text{and}$$

$$s(x)f(x) + t(x)|f(x)| = d(x), \quad \text{for} \quad x \in Z.$$

On combining these equations, we get

(b) $$(s(x)g(x) + t(x)h(x))d(x) = d(x) \quad (x \in Z).$$

Now, by (a), $d$ has no zeros on $Z - Z(f)$; with (b), this yields

$$s(x)g(x) + t(x)h(x) = 1 \quad (x \in Z - Z(f)).$$

Note that $Z - Z(f) = (Z \cap \operatorname{pos} f) \cup (Z \cap \operatorname{neg} f)$. Next, (a) implies that

$$g(x) = h(x) \quad (x \in Z \cap \operatorname{pos} f),$$

and

$$g(x) = -h(x) \quad (x \in Z \cap \operatorname{neg} f).$$

Define a function $k$ on $Z - Z(f)$ by $k(x) = 1$ for $x \in Z \cap \operatorname{pos} f$ and $k(x) = -1$ for $x \in Z \cap \operatorname{neg} f$. Then the function $k$ is continuous on $Z - Z(f)$ (as it is constant on each of the two disjoint closed sets), and by the Tietze extension theorem, $k$ extends continuously to all of $Z$. Thus $Z \cap \operatorname{pos} f$ and $Z \cap \operatorname{neg} f$ are completely separated.
