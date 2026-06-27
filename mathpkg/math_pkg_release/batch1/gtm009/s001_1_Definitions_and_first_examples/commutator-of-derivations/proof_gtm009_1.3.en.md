---
role: proof
locale: en
of_concept: commutator-of-derivations
source_book: gtm009
source_chapter: "1"
source_section: "1.3"
---

Let $\delta, \delta'$ be derivations of $\mathfrak{A}$. For any $a, b \in \mathfrak{A}$, compute:

$$[\delta, \delta'](ab) = (\delta\delta' - \delta'\delta)(ab) = \delta(\delta'(ab)) - \delta'(\delta(ab)).$$

Using the derivation property on each inner term:
$$\delta'(ab) = a\delta'(b) + \delta'(a)b,$$
$$\delta(ab) = a\delta(b) + \delta(a)b.$$

Now compute $\delta(a\delta'(b) + \delta'(a)b)$:
$$\delta(a\delta'(b)) + \delta(\delta'(a)b) = a\delta(\delta'(b)) + \delta(a)\delta'(b) + \delta'(a)\delta(b) + \delta(\delta'(a))b.$$

Similarly, $\delta'(a\delta(b) + \delta(a)b)$:
$$\delta'(a\delta(b)) + \delta'(\delta(a)b) = a\delta'(\delta(b)) + \delta'(a)\delta(b) + \delta(a)\delta'(b) + \delta'(\delta(a))b.$$

Subtracting, the four middle terms cancel (each appears once in each expansion), leaving:
$$[\delta, \delta'](ab) = a(\delta\delta' - \delta'\delta)(b) + (\delta\delta' - \delta'\delta)(a)b = a[\delta, \delta'](b) + [\delta, \delta'](a)b.$$

Thus $[\delta, \delta']$ satisfies the product rule and is a derivation. The ordinary product $\delta\delta'$ need not be a derivation because it does not satisfy the Leibniz rule in general.
