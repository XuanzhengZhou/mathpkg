---
role: proof
locale: en
of_concept: odd-valence-vertices-even
source_book: gtm054
source_chapter: "III"
source_section: "A"
---

From the Handshaking Lemma, $\sum_{x \in V} \rho(x) = 2\nu_1(\Gamma)$. The right-hand side is even. Let $V_{\text{odd}} = \{x \in V : \rho(x) \text{ is odd}\}$ and $V_{\text{even}} = \{x \in V : \rho(x) \text{ is even}\}$. Then

$$\sum_{x \in V_{\text{odd}}} \rho(x) + \sum_{x \in V_{\text{even}}} \rho(x) = 2\nu_1(\Gamma).$$

The second sum on the left is a sum of even numbers, hence even. The first sum is a sum of $|V_{\text{odd}}|$ odd numbers. A sum of an odd number of odd numbers is odd; a sum of an even number of odd numbers is even. Since the total sum is even, $|V_{\text{odd}}|$ must be even.
