---
role: proof
locale: en
of_concept: different-discriminant-tower-formula
source_book: gtm028
source_chapter: "IV"
source_section: "11. Different and discriminant"
---

For the formula for the different, we have:

$$\mathfrak{D}_{R''/R} = \mathfrak{D}_{R''/R'} \cdot (R'' \mathfrak{D}_{R'/R}).$$

For the formula for discriminants, we take the norm $N_{K'/K}$ of both sides of the different formula. We get:

$$\mathfrak{d}_{R''/R} = N_{K'/K}(\mathfrak{D}_{R''/R'} \cdot (R'' \mathfrak{d}_{R'/R}))$$
$$= N_{K'/K}(\mathfrak{D}_{R''/R'}) \cdot N_{K'/K}(R'' \mathfrak{d}_{R'/R})$$
$$= N_{K'/K}(\mathfrak{d}_{R''/R'}) \cdot N_{K'/K}(N_{K''/K'}(R'' \mathfrak{d}_{R'/R}))$$
$$= N_{K'/K}(\mathfrak{d}_{R''/R'}) \cdot N_{K'/K}((\mathfrak{d}_{R'/R})^{n})$$
$$= N_{K'/K}(\mathfrak{d}_{R''/R'}) \cdot (\mathfrak{d}_{R'/R})^{n},$$

where $n = [K'' : K']$.
