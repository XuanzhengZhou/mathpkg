---
role: proof
locale: en
of_concept: ramification-groups-abelian
source_book: gtm028
source_chapter: "V"
source_section: "10"
---

For $n \geq 2$, the abelian property follows from the commutator lemma: the commutator of $G_{V_n}$ with itself lies in $G_{V_{2n-1}} \subset G_{V_{n+1}}$, so $G_{V_n}/G_{V_{n+1}}$ is abelian.

In the inseparable case, we prove that $G'_1 = G_{V_1}/G_{V_2}$ is also abelian. Any element of $G'_1$ is the $(G_{V_2})$-residue of an element $s \in G_T$ such that $s(u) - u \in \mathfrak{P}^2$ (where $u$ generates the maximal ideal). We have $s(z) - z \in \mathfrak{P}^2$ for every $z \in \mathfrak{P}$. Furthermore, since any element $y \in \mathfrak{P}^2$ may be written as $y = zz'$ with $z, z' \in \mathfrak{P}$, we have $s(y) - y \in \mathfrak{P}^3$ for any $y \in \mathfrak{P}^2$.

Consider two elements $s, t \in G_T$ such that $s(u) - u$ and $t(u) - u$ lie in $\mathfrak{P}^2$. Then for any $z \in \mathfrak{P}$, the difference $st(z) - ts(z)$ is the difference of $s(t(z)-z) - (t(z)-z)$ and $t(s(z)-z) - (s(z)-z)$. Since $y = t(z)-z \in \mathfrak{P}^2$, the first element $s(y)-y \in \mathfrak{P}^3$, and similarly the second. Thus $st(z) - ts(z) \in \mathfrak{P}^3$, so the commutator lies in $G_{V_2}$ modulo $G_{V_3}$, proving $G'_1$ is abelian.

Since the $G_{V_n}$ form a decreasing sequence whose intersection is the identity, and each quotient is abelian, the inertia group $G_T = G_{V_1}$ is solvable.
