---
role: proof
locale: en
of_concept: thm-11
source_book: gtm095
source_chapter: "2"
source_section: "11"
---

# Proof of Theorem 11 (Integration by Parts for Lebesgue&ndash;Stieltjes Integrals)

Let $F = F(x)$ and $G = G(x)$ be two generalized distribution functions on $(R, \mathcal{B}(R))$. The following formulas are valid for all real $a$ and $b$, $a < b$:

$$F(b)G(b) - F(a)G(a) = \int_a^b F(s)\, dG(s) + \int_a^b G(s-)\, dF(s), \tag{62}$$

$$F(b)G(b) - F(a)G(a) = \int_a^b G(s)\, dF(s) + \int_a^b F(s-)\, dG(s). \tag{63}$$

**Proof.** We first recall that in accordance with Subsection 1 an integral $\int_a^b (\cdot)$ means $\int_{(a,b]}(\cdot)$. Then (see formula (2) in Sect. 3)

$$\bigl(F(b) - F(a)\bigr)\bigl(G(b) - G(a)\bigr) = \int_a^b dF(s) \cdot \int_a^b dG(t).$$

Let $F \times G$ denote the direct product of the measures corresponding to $F$ and $G$. Then by Fubini's theorem

$$\bigl(F(b) - F(a)\bigr)\bigl(G(b) - G(a)\bigr) = \int_{(a,b] \times (a,b]} d(F \times G)(s,t)$$

$$= \int_{(a,b] \times (a,b]} I_{\{s \geq t\}}(s,t)\, d(F \times G)(s,t) + \int_{(a,b] \times (a,b]} I_{\{s < t\}}(s,t)\, d(F \times G)(s,t)$$

$$= \int_{(a,b]} \bigl(G(s) - G(a)\bigr)\, dF(s) + \int_{(a,b]} \bigl(F(t-) - F(a)\bigr)\, dG(t)$$

$$= \int_a^b G(s)\, dF(s) + \int_a^b F(s-)\, dG(s) - G(a)\bigl(F(b) - F(a)\bigr) - F(a)\bigl(G(b) - G(a)\bigr), \tag{65}$$

where $I_A$ is the indicator of the set $A$.

Expanding the left-hand side of (65):

$$(F(b) - F(a))(G(b) - G(a)) = F(b)G(b) - F(b)G(a) - F(a)G(b) + F(a)G(a).$$

Now moving the terms $-G(a)(F(b)-F(a))$ and $-F(a)(G(b)-G(a))$ from the right-hand side of (65) to the left-hand side, and expanding them:

$$-G(a)(F(b)-F(a)) = -G(a)F(b) + G(a)F(a),$$
$$-F(a)(G(b)-G(a)) = -F(a)G(b) + F(a)G(a).$$

Adding these to the left-hand side of (65):

$$F(b)G(b) - F(a)G(b) + F(a)G(a) = \int_a^b G(s)\, dF(s) + \int_a^b F(s-)\, dG(s).$$

Wait, simplifying more carefully: the left-hand side becomes

$$F(b)G(b) - F(b)G(a) - F(a)G(b) + F(a)G(a) + G(a)F(b) - G(a)F(a) + F(a)G(b) - F(a)G(a)$$
$$= F(b)G(b) - F(a)G(a).$$

Thus from (65) we obtain

$$F(b)G(b) - F(a)G(a) = \int_a^b G(s)\, dF(s) + \int_a^b F(s-)\, dG(s),$$

which is formula (63).

Formula (62) follows from (63) by interchanging the roles of $F$ and $G$, or equivalently, by splitting the product as $I_{\{s < t\}} + I_{\{s \geq t\}}$ in the opposite order. One may also derive (62) directly from (63) by observing that

$$\int_a^b \bigl(G(s) - G(s-)\bigr)\, dF(s) = \sum_{a < s \leq b} \Delta G(s) \cdot \Delta F(s),$$

and therefore the integrals involving $G(s-)$ in (63) and $G(s)$ in (62) differ by the sum of products of simultaneous jumps. Noting that the same jump terms appear symmetrically, one obtains (62):

$$F(b)G(b) - F(a)G(a) = \int_a^b F(s)\, dG(s) + \int_a^b G(s-)\, dF(s).$$

This completes the proof. $\square$

**Remark.** The conclusion of the theorem remains valid for functions $F$ and $G$ of bounded variation on $[a, b]$. Every such function that is continuous on the right and has limits on the left can be represented as the difference of two monotone nondecreasing functions.
