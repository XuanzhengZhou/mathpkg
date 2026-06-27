---
role: proof
locale: en
of_concept: zero-times-x-equals-zero
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of $0 \cdot x = 0$

From the field axioms, we compute:

$$0 \cdot x = (0 + 0) \cdot x \quad (\text{since } 0 = 0 + 0 \text{ by A3})$$
$$= 0 \cdot x + 0 \cdot x \quad (\text{by the distributive law, DL})$$

Adding $-(0 \cdot x)$ to both sides (using A4):

$$0 \cdot x + (-(0 \cdot x)) = (0 \cdot x + 0 \cdot x) + (-(0 \cdot x))$$
$$0 = 0 \cdot x + (0 \cdot x + (-(0 \cdot x))) \quad (\text{by associativity of addition, A1})$$
$$0 = 0 \cdot x + 0 \quad (\text{since } a + (-a) = 0 \text{ by A4})$$
$$0 = 0 \cdot x \quad (\text{by A3}).$$

Thus $0 \cdot x = 0$ for all $x \in \mathbb{R}$.
