---
role: proof
locale: en
of_concept: uniqueness-of-identities
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of Uniqueness of Additive and Multiplicative Identities and Inverses

**Uniqueness of the additive identity 0.** Suppose $0' \in \mathbb{R}$ also satisfies $x + 0' = x$ for all $x \in \mathbb{R}$. Taking $x = 0$ (the identity from A3), we obtain $0 + 0' = 0$. But by commutativity (A2) and the defining property of $0'$, we have $0 + 0' = 0' + 0 = 0'$. Hence $0 = 0'$.

**Uniqueness of the multiplicative identity 1.** Suppose $1' \in \mathbb{R}$ also satisfies $x \cdot 1' = x$ for all $x \in \mathbb{R}$. Taking $x = 1$, we obtain $1 \cdot 1' = 1$. By commutativity (M2) and the defining property of $1'$, $1 \cdot 1' = 1' \cdot 1 = 1'$. Hence $1 = 1'$.

**Uniqueness of the additive inverse.** For $x \in \mathbb{R}$, suppose $y$ and $y'$ both satisfy $x + y = 0$ and $x + y' = 0$. Then

$$y = y + 0 = y + (x + y') = (y + x) + y' = 0 + y' = y'.$$

Thus $-x$ is unique.

**Uniqueness of the multiplicative inverse.** For $x \neq 0$, suppose $y$ and $y'$ both satisfy $xy = 1$ and $xy' = 1$. Then

$$y = y \cdot 1 = y(xy') = (yx)y' = 1 \cdot y' = y'.$$

Thus $x^{-1}$ is unique.
