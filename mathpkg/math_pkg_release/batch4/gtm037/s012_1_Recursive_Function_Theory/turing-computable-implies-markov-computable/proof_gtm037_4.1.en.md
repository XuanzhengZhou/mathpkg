---
role: proof
locale: en
of_concept: turing-computable-implies-markov-computable
source_book: gtm037
source_chapter: "4. Recursive Function Theory"
source_section: "4.1"
---

**Proof.** Let $f$ ($n$-ary) be computed by a Turing machine $M$, with notation as in 1.1 and 3.9. With each row $t_i = (c_{j(i)}, \varepsilon_i, v_i, d_i)$ of $M$ ($1 \leq i \leq 2m$) we shall associate one or more rows $t'(i, 0), \ldots, t'(i, p_i)$ of a Markov algorithm, depending on $v_i$.

**Case 1.** $v_i = 0$ or $1$. We associate the row
$$\langle \varepsilon_i\ 2\ 1^{(c_{j(i)}+1)}\ 2 \rangle \rightarrow \langle v_i\ 2\ 1^{(d_i+1)}\ 2 \rangle.$$

**Case 2.** $v_i = 2$. We associate the rows (in order)
$$\langle 0\ \varepsilon_i\ 2\ 1^{(c_{j(i)}+1)}\ 2 \rangle \rightarrow \langle 0\ 2\ 1^{(d_i+1)}\ 2\ \varepsilon_i \rangle,$$
$$\langle 1\ \varepsilon_i\ 2\ 1^{(c_{j(i)}+1)}\ 2 \rangle \rightarrow \langle 1\ 2\ 1^{(d_i+1)}\ 2\ \varepsilon_i \rangle,$$
$$\langle \varepsilon_i\ 2\ 1^{(c_{j(i)}+1)}\ 2 \rangle \rightarrow \langle 0\ 2\ 1^{(d_i+1)}\ 2\ \varepsilon_i \rangle.$$

**Case 3.** $v_i = 3$. We associate the rows (in order)
$$\langle \varepsilon_i\ 2\ 1^{(c_{j(i)}+1)}\ 2\ 0 \rangle \rightarrow \langle \varepsilon_i\ 0\ 2\ 1^{(d_i+1)}\ 2 \rangle,$$
$$\langle \varepsilon_i\ 2\ 1^{(c_{j(i)}+1)}\ 2\ 1 \rangle \rightarrow \langle \varepsilon_i\ 1\ 2\ 1^{(d_i+1)}\ 2 \rangle.$$

Now suppose $M$ computes the value $f(x_0, \ldots, x_{n-1})$. Let the computation of $M$ on input $x_0, \ldots, x_{n-1}$ be
$$\langle G_0, G_1, \ldots, G_q \rangle.$$
We shall associate with each $G_i$ a pair $(N_i, P_i)$ of words in the alphabet $\{0, 1, 2\}$ and a word $Q_i$ such that the following conditions hold:

(6) $G_i$ is $0$ except for $N_i P_i$;
(7) exactly two $2$'s occur in $Q_i$;
(8) $N_i\ 2 \cdot 1^{(a_i+1)} \cdot 2\ P_i = Q_i$;
(9) if $i \neq 0$, then $(Q_{i-1}, Q_i)$ is a nonterminating algorithmic step under $A$.

Clearly (3)-(9) hold for $i = 0$. We now define $N_{i+1}, P_{i+1}, Q_{i+1}$. Let the row of $M$ beginning with $a_i G_i b_i$ be
$$a_i G_i b_i v w.$$

We now distinguish cases depending on $v$. Note that, since $i < q - 1$, $v \neq 4$. In each case we define $N_{i+1}, P_{i+1}, Q_{i+1}$, and it will then be evident that (3)-(9) hold for $i + 1$.

**Case 1.** $v = 0$. Let $N_{i+1}$ be $N_i$ with its last entry replaced by $0$, and let $P_{i+1} = P_i$.

**Case 2.** $v = 1$. Similarly.

**Case 3.** $v = 2$. Here we take two subcases:

*Subcase 1.* $N_i$ has length at least $2$. Write $N_i = N_{i+1}\varepsilon$, where $\varepsilon = 0$ or $1$, and set $P_{i+1} = \varepsilon P_i$.

*Subcase 2.* $N_i$ has length $1$. Let $N_{i+1} = \langle 0 \rangle$, $P_{i+1} = N_i P_i$.

**Case 4.** $v = 3$. Again we take two subcases:

*Subcase 1.* $P_i \neq 0$. Write $P_i = \varepsilon P_{i+1}$ with $\varepsilon = 0$ or $1$, and set $N_{i+1} = N_i \varepsilon$.

*Subcase 2.* $P_i = 0$. Set $P_{i+1} = N_i 0$, $N_{i+1} = \langle 0 \rangle$.

It can be verified that in each case the conditions (3)-(9) hold for $i+1$, completing the construction. The Markov algorithm $A$ thus simulates the Turing machine $M$ and computes the same function $f$.
