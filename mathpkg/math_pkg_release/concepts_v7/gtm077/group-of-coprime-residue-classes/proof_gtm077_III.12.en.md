---
role: proof
locale: en
of_concept: group-of-coprime-residue-classes
source_book: gtm077
source_chapter: "III"
source_section: "12"
---
# Proof: Group of Residue Classes Relatively Prime to $n$

We show that the residue classes modulo $n$ whose representatives are relatively prime to $n$, under composition by multiplication, form an Abelian group $\mathfrak{R}(n)$ of order $\varphi(n)$.

**1. Well-definedness of multiplication on residue classes.** If $a_1 \equiv a_2 \pmod{n}$ and $b_1 \equiv b_2 \pmod{n}$, then
$$a_1 = a_2 + kn, \quad b_1 = b_2 + \ell n$$
for some integers $k, \ell$. Computing the product:
$$a_1 b_1 = (a_2 + kn)(b_2 + \ell n) = a_2 b_2 + n(a_2 \ell + b_2 k + k \ell n) \equiv a_2 b_2 \pmod{n}.$$
Thus the residue class of $a_1 b_1$ modulo $n$ depends only on the residue classes of $a_1$ and $b_1$, not on the chosen representatives. This defines a well-defined multiplication of residue classes.

**2. Closure under multiplication.** Let $A, B$ be residue classes represented by $a, b$ with $(a, n) = 1$ and $(b, n) = 1$. If a prime $p \mid (ab, n)$, then $p \mid n$ and $p \mid ab$, so $p \mid a$ or $p \mid b$, contradicting $(a, n) = (b, n) = 1$. Hence $(ab, n) = 1$. Thus the product $AB$ (the residue class of $ab$) again consists of numbers coprime to $n$, and belongs to $\mathfrak{R}(n)$.

**3. Group axioms.**

- **Associativity:** $(AB)C = A(BC)$ follows from the associativity of integer multiplication: $(ab)c \equiv a(bc) \pmod{n}$.

- **Identity:** The residue class $E$ containing $1$ satisfies $AE = A$ for all $A \in \mathfrak{R}(n)$, since $a \cdot 1 \equiv a \pmod{n}$ and $(1, n) = 1$.

- **Inverse:** Let $A$ be represented by $a$ with $(a, n) = 1$. By the extended Euclidean algorithm, there exist integers $x, y$ such that $ax + ny = 1$. Reducing modulo $n$ gives $ax \equiv 1 \pmod{n}$. Moreover, $(x, n) = 1$ (otherwise a common divisor would divide $ax + ny = 1$). Hence the residue class $X$ of $x$ lies in $\mathfrak{R}(n)$ and satisfies $AX = E$.

- **Commutativity:** $AB = BA$ because $ab \equiv ba \pmod{n}$.

**4. Order of $\mathfrak{R}(n)$.** The number of residue classes modulo $n$ that are relatively prime to $n$ is, by definition, Euler's totient function $\varphi(n)$. Hence $|\mathfrak{R}(n)| = \varphi(n)$.

Thus $\mathfrak{R}(n)$ is an Abelian group of order $\varphi(n)$, the group of units of the ring $\mathbb{Z}/n\mathbb{Z}$. $\square$
