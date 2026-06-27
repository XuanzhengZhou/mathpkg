---
role: proof
locale: en
of_concept: thm-theorem-43
source_book: gtm042
source_chapter: "18.3"
source_section: "Reformulations"
---

To prove that $f'$ is a virtual character of $G$ (i.e., belongs to $R_K(G)$), it is enough to prove that, for each elementary subgroup $H$ of $G$, the restriction of $f'$ to $H$ belongs to $R_K(H)$ (cf. 11.1, th. 21). We are thus reduced to the case where $G$ is elementary, and so decomposes as $G = S \times P$ where $S$ has order prime to $p$ and $P$ is a $p$-group. Moreover, we can assume that $f$ is the modular character of a simple $k[G]$-module $E$. By the discussion in 15.7, $E$ is even a simple $k[S]$-module, and we can lift it to a simple $K[S]$-module on which $P$ acts trivially. The character of this module is evidently $f'$, which proves (i).

Assertion (ii) follows from (i) by observing that the restriction of $f'$ to $G_{\text{reg}}$ is equal to $f$.

Exercises

18.7. Let $m$ be the 1.c.m. of orders of the elements of $G$. Write $m$ in the form $p^n m'$ with $(p, m') = 1$ (cf. 18.1.) and choose an integer $q$ such that $q \equiv 0$ (mod. $p^n$) and $q \equiv 1$ (mod. $m'$).
(a) Show that, if $s \in G$, the $p'$-component $s'$ of $s$ is equal to $s^q$.
(b) Let $f$ be a modular character of $G$, and let $\phi$ be an element of $R_K(G)$ whose restriction to $G_{\text{reg}}

Chapter 18: Modular characters

We shall determine its irreducible modular characters in characteristic $p$. We may assume that $p$ divides the order of $G$, i.e., $p = 2$ or $p = 3$.

(a) The case $p = 2$

There are two $p$-regular classes: that of 1 and that of $(abc)$. By cor. 3 to th. 42, there are two irreducible representations in characteristic 2 (up to isomorphism.) The only representation of degree 1 is the unit representation, with modular character $\phi_1 = 1$. On the other hand, the irreducible representation of degree 2 of $\mathfrak{S}_4$ upon reduction mod. 2 gives a representation $\rho_2$ whose modular character $\phi_2$ takes the value $-1$ for the element $(abc)$. Consequently, $\rho_2$ is not an extension of two representations of degree 1 (otherwise we would have $\phi_2 = 2\phi_1 = 2$), hence is irreducible. The irreducible modular characters of $\mathfrak{S}_4$ are thus $\phi_1$ and $\phi_2$:

$$
\begin{array}{c c c c}
& 1 & (abc) \\
\phi_1 & 1 & 1 \\
\phi_2 & 2 & -1
\end{array}
$$

The decomposition matrix $D$ is obtained by expressing the restrictions to $G_{\text{reg}}$ of the characters $\chi_1, \ldots, \chi_5$ as a function of $\phi_1$ and $\phi_2$. We find

$$
\chi_1 = \phi_1 \quad \text{on} \quad G_{\text{reg}}
$$

$$
\chi_2 = \phi_1 \quad \text{on} \quad G_{\text{reg}}
$$

$$
\chi_3 = \phi_2 \quad \text{on} \quad G_{\text{reg}}
$$

$$
\chi_4 = \phi_1 + \phi_2 \quad \text{on} \quad G_{\text{reg}}
$$

$$
\chi_5 = \phi_1

following decomposition of $\Phi_1$ and $\Phi_2$ on $G_{\text{reg}}$:

$$\Phi_1 = 4\phi_1 + 2\phi_2 \quad \text{on } G_{\text{reg}}$$
$$\Phi_2 = 2\phi_1 + 3\phi_2 \quad \text{on } G_{\text{reg}}.$$

(b) The case $p = 3$

There are four $p$-regular classes: 1, $(ab), (ab)(cd), (abcd)$, hence four irreducible representations in characteristic $p = 3$. On the other hand, the reductions of the characters $\chi_1, \chi_2, \chi_4$ and $\chi_5$ are irreducible: this is clear for the first two, which have degree 1, and for the two others it follows from the fact that their degree is the largest power of $p$ dividing the group order (cf. 16.4, prop. 46). Since their modular characters are distinct, they are all the irreducible modular characters of the $\mathfrak{S}_4$. If we denote them by $\phi_1, \phi_2, \phi_3, \phi_4$, we have the table:

$$\begin{array}{c|cccc}
& 1 & (ab) & (ab)(cd) & (abcd) \\
\hline
\phi_1 & 1 & 1 & 1 & 1 \\
\phi_2 & 1 & -1 & 1 & -1 \\
\phi_3 & 3 & 1 & -1 & -1 \\
\phi_4 & 3 & -1 & -1 & 1
\end{array}$$

Since $\chi_3 = \phi_1 + \phi_2$ on $G_{\text{reg}}$ we obtain the following decomposition matrix $D$ and Cartan matrix $C$:

$$D = \begin{pmatrix}
1 & 0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0 \\
0 & 0 &

Chapter 18: Modular characters

EXERCISES

18.9. Verify the Fong-Swan theorem for $\mathfrak{S}_4$ [check that each $\phi_i$ is the restriction of some $\chi_j$ to $G_{\text{reg}}$].

18.10. Show that the irreducible representations of $\mathfrak{S}_4$ are realizable over the prime field (in any characteristic).

18.11. The group $\mathfrak{S}_4$ has a normal subgroup $N$ of order 4 such that $\mathfrak{S}_4/N$ is isomorphic to $\mathfrak{S}_3$. Show that $N$ acts trivially in each irreducible representation of $\mathfrak{S}_4$ in characteristic 2. Use this to classify such representations.

18.6 Example: Modular characters of the alternating group $\mathfrak{A}_5$

The group $\mathfrak{A}_5$ is the group of even permutations of $\{a, b, c, d, e\}$. It has 60 elements, divided into 5 conjugacy classes:

the identity element 1,
the 15 conjugates of $(ab)(cd)$, which have order 2,
the 20 conjugates of $(abc)$, which have order 3,
the 12 conjugates of $s = (abcde)$, which have order 5,
the 12 conjugates of $s^2$, which have order 5.

There are 5 irreducible characters, given by the following table:

$$
\begin{array}{c c c c c c}
& 1 & (ab)(cd) & (abc) & s & s^2 \\
\chi_1 & 1 & 1 & 1 & 1 & 1 \\
\chi_2 & 3 & -1 & 0 & z = \frac{1 + \sqrt{5}}{2} & z' \\
\chi_3 & 3 & -1 & 0 & z' = \frac{1 - \sqrt{5}}{2} & z \\
\chi_4 & 4 & 0 & 1 & -1 & -1 \\
\chi_5 &

18.6: Example: modular characters of the alternating group $\mathfrak{A}_5$

$\chi_5$: a representation of degree 5, realizable over $\mathbf{Q}$, obtained by removing the unit representation from the permutation representation of $\mathfrak{A}_5$ on the set of its 6 subgroups of order 5.

We determine the modular irreducible characters of $\mathfrak{A}_5$ for $p = 2, 3, 5$:

(a) The case $p = 2$

There are four $p$-regular classes, hence 4 modular irreducible characters. Two of these are obvious: the unit character, and the restriction of $\chi_4$ (cf. prop. 46). On the other hand, we have

$$\chi_2 + \chi_3 = 1 + \chi_5 \text{ on } G_{\text{reg}},$$

which shows that the reductions of both the irreducible representations of degree 3 are not irreducible (their characters are conjugate over the field $\mathbf{Q}_2$ of 2-adic numbers since $\sqrt{5} \notin \mathbf{Q}_2$). Each must decompose in $R_k(\mathbf{G})$ as a sum of the unit representation and a representation of degree 2, necessarily irreducible. Therefore, the irreducible modular characters $\phi_1, \phi_2, \phi_3, \phi_4$ are given by the table:

| | 1 | (abc) | s | $s^2$ |
| :--- | :--- | :--- | :--- | :--- |
| $\phi_1$ | 1 | 1 | 1 | 1 |
| $\phi_2$ | 2 | $-1$ | $z-1$ | $z'-1$ |
| $\phi_3$ | 2 | $-1$ | $z'-1$ | $z-1$ |
| $\phi_4$ | 4 | 1 | $-1$ | $-1$ |

We have

$$\chi_1 = \phi_1 \text{ on } G_{\text{reg}}$$
$$\chi_2 = \phi_1

(b) The case $p = 3$

One finds 4 irreducible representations in characteristic 3, namely the reductions of the irreducible representations of degree 1, 3, and 4 (two of degree 3). Moreover, we have $\chi_5 = 1 + \chi_4$ on $G_{\text{reg}}$. Hence:

$$D = \begin{pmatrix}
1 & 0 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 1
\end{pmatrix}, \quad C = \begin{pmatrix}
2 & 0 & 0 & 1 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 2
\end{pmatrix}, \quad \det(C) = 3.$$

(c) The case $p = 5$

There are 3 irreducible representations in characteristic 5, the reductions of the irreducible representations of degree 1, 3, and 5 (note that the two representations of degree 3 have isomorphic reductions). Moreover, we have $\chi_4 = \chi_1 + \chi_3$ on $G_{\text{reg}}$. Hence

$$D = \begin{pmatrix}
1 & 0 & 0 & 1 & 0 \\
0 & 1 & 1 & 1 & 0 \\
0 & 0 & 0 & 0 & 1
\end{pmatrix}, \quad C = \begin{pmatrix}
2 & 1 & 0 \\
1 & 3 & 0 \\
0 & 0 & 1
\end{pmatrix}, \quad \det(C) = 5.$$

EXERCISES

18.12. Check assertions (b) and (c).

18.13. Prove that the irreducible representations of degree 2 of $\mathfrak{A}_5$ in characteristic 2 are realizable over the field $F_4$ of 4 elements; obtain from this an isomorphism of $\mathfrak{A
