---
role: proof
locale: en
of_concept: skornyakov-san-soucie-theorem
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

**Proof of Theorem 6.16 (Skornyakov-San Soucie Theorem).** For any $a, b, c$ in $D$ we define the associator $[a, b, c] = (ab)c - a(bc)$ and the commutator $[a, b] = ab - ba$. It is straightforward to verify that each of these is additive in all arguments.

Throughout the section we shall let (RA) denote the right alternative law, $(xy)y = xy^2$, and let (M) denote the identity $x(yz)y = (xy)z y$. (The $M$ standing for Moufang who first studied division rings with this property.) By Lemma 6.13, since $D$ has RIP, $D$ satisfies both (RA) and (M). We now establish a long series of results which we shall call (1), (2), ...

**(1)** $[a, b, c] = -[a, c, b]$ for all $a, b, c$ in $D$.

**Proof of (1).** By (RA) $[x, y, y] = 0$ for all $x, y \in D$ and we have
$$0 = [a, b + c, b + c] = [a, b, b] + [a, b, c] + [a, c, b] + [a, c, c] = [a, b, c] + [a, c, b].$$
Thus $[a, b, c] = -[a, c, b]$. $\square$

**(2)** $[a, bc] = [a, b]c + b[a, c]$ for all $a, b, c \in D$.

**Proof of (2).** By expanding $[a, bc] = a(bc) - (bc)a$ and adding/subtracting terms, linearizing, one obtains the result from the additive properties and the definition of commutator. $\square$

We define three "functions", $f, g, h$, each of four variables, on $D$ by
$$f(d, a, b, c) = [da, b, c] - [d, ab, c] + [d, a, bc] - [d, a, c]b - [d, a, b]c,$$
$$g(a, d, b, c) = [a, d, bc] + [a, b, dc] - [a, d, c]b - [a, b, c]d,$$
$$h(d, a, b, c) = [da, b, c] + [d, a, [b, c]] - [d, a, b]c - [d, b, c]a.$$

**(3)** $f(d, a, b, c) = g(a, d, b, c) = h(d, a, b, c) = 0$ for all $a, b, c, d$ in $D$.

**Proof of (3).** The proof expands the definition of $f$:
$$\begin{aligned}
f(d, a, b, c) &= ((da) b) c - (da) (bc) - (d(ab)) c + d((ab) c) \\
&\quad + (da) (bc) - d(a(bc)) - d((ab) c) + d(a(bc)) \\
&\quad - ((da) b) c + d((ab)) c = 0.
\end{aligned}$$

Now replace $b$ by $b + d$ in (2) to get
$$\begin{aligned}
0 &= [a, b + d, (b + d) c] - [a, b + d, c] (b + d) \\
&= [a, b, bc] + [a, b, dc] + [a, d, bc] + [a, d, dc] \\
&\quad - [a, b, c] b - [a, b, c] d - [a, d, c] b - [a, d, c] d
\end{aligned}$$
and by (2) the first and fifth terms cancel and so do the fourth and eighth leaving $g(a, d, b, c)$. Now, we have
$$0 = f(d, a, b, c) - g(d, a, b, c) = \dots$$
which yields $h(d, a, b, c) = 0$. $\square$

**(4)** For all $a, b \in D$, $[a, ab + ba, b] = 0$.

**(5)** Define $A(a, b) = \{x \in D \mid [x, a, b] = x[b, a]\}$. Then:
(i) $x \in A(a, b) \iff (xa)b = x(ba)$.
(ii) $0 \in A(a, b)$ so $A(a, b)$ is nonempty.
(iii) $A(a, b)$ is a subgroup of the additive group of $D$.
(iv) $A(a, b) = A(b, a)$.

**Proof of (5).** Let $x$ be in $A(a, b)$. Then $(xa) b - x(ab) = x(ba) - x(ab)$ by definition of $A(a, b)$ and hence $(xa) b = x(ba)$. The converse is clearly true also. We obviously have $[0, a, b] = 0 = 0[b, a]$ so $0 \in A(a, b)$ and $A(a, b)$ is non empty. Let $x, y \in A(a, b)$. Then $[x - y, a, b] = [x, a, b] - [y, a, b] = x[b, a] - y[b, a] = (x - y)[b, a]$. Hence $x - y \in A(a, b)$ so $A(a, b)$ is a subgroup as claimed.

Finally, $x \in A(a, b) \iff [x, a, b] = x[b, a] \iff -[x, b, a] = -x[a, b] \iff [x, b, a] = x[a, b] \iff x \in A(b, a)$. $\square$

**(6)** If $[a, a, b] \neq 0$, then $A(a, b) \cap A(a, ba) = \{0\}$.

**Proof of (6).** Let $x$ be in $A(a, b) \cap A(a, ba)$. Since $x \in A(a, b)$, by (5) $(xa) b = x(ba)$ and hence by (M)
$$x((ab) a) = ((xa) b) a = (x(ba)) a.$$
By (5) since $x \in A(a, ba) = A(ba, a)$, we have
$$(x(ba)) a = x(a(ba))$$
and by the two equations above
$$0 = (x(ba)) a - (x(ba)) a = x((ab) a) - x(a(ba)) = x[a, a, b] = -x[a, a, b]$$
and since $[a, a, b] \neq 0$, this forces $x = 0$. $\square$

**(7)** $[x, y, z] \in A(y, z)$ for all $x, y, z \in D$.

**(8)** [Used implicitly in later steps.]

**(9)** $[[a, b], a, b] = 0$ for all $a, b \in D$.

**Proof of (9).** Let $p = [a, a, b]$, $q = [a, b]$. By (7), $p \in A(a, b)$ and $q = [1, a, b]$ so $q$ also lies in certain associator subspaces. Then using $h(q, s, a, b)$ with $s = [[q, a, b]]$, one computes
$$\begin{aligned}
0 &= h(q, s, a, b) = [qs, a, b] + [q, s, q] - q[s, a, b] - [q, a, b] s \\
&= -(qs) q + (qs) q - q(sq) + q(sq) - s^2.
\end{aligned}$$
Thus, $s^2 = 0$ and we have $0 = s = [[a, b], a, b]$. $\square$

**(10)** $[[a, b], a, c] = -[[a, c], a, b]$ for all $a, b, c \in D$.

**Proof of (10).** By (9) $0 = [[a, b + c], a, b + c]$; expanding this by linearity and applying (9) gives
$$\begin{aligned}
0 &= [[a, b + c], a, b] + [[a, b + c], a, c] \\
&= [[a, b], a, b] + [[a, c], a, b] + [[a, b], a, c] + [[a, c], a, c] \\
&= [[a, c], a, b] + [[a, b], a, c]
\end{aligned}$$
as desired. $\square$

**(11)** $[x[a, b], a, b] = [x, a, b][a, b]$ for all $a, b, x \in D$.

**Proof of (11).** Put $[a, b] = q$. Then
$$0 = h(x, q, a, b) = [xq, a, b] + [x, q, q] - x[q, a, b] - [x, a, b] q$$
and since $[x, q, q] = 0$ by (RA) and $[q, a, b] = 0$ by (9) the result is proved. $\square$

**(12)** $[(xa)b - x(ba), a, b] = 0$ for all $a, b, x \in D$.

This follows from the definition of $A(a, b)$ and (7).

**(13)** Various relations among $p = [a, a, b]$, $q = [a, b]$, and elements of $A(a, b)$, used to establish:
This gives $p^2 = (pq)a - p(aq)$ and so using (12)
$$[p^2, a, q] = [(pq) a - p(aq), a, q] = -[(pq) a - p(aq), q, a] = 0.$$
Also $[p^2, a, ab] = [p^2, a, q] + [p^2, a, ba] = 0 + 0 = 0.$

**(14)** $[x, y, z] (wz) + [x, w, z] (yz) = ([x, y, z] w)z + ([x, w, z] z) y$ for all $x, y, z, w \in D$.

**Proof of (14).** By (7) $[x, y + w, z] \in A(y + w, z)$ and hence by (5)
$$[x, y + w, z] (yz + wz) = ([x, y + w, z] z) (y + w).$$
Expanding both sides linearly and canceling matching terms yields the identity.

**(15)** and **(16)** are five- and six-variable identities used in the subsequent Steps (A)-(E).

The proof continues with five major steps:

**Step (A).** $[q, a, q] = 0 = [q, a, ba]$.

**Proof.** By (2) and (9) $[q, a, ab] = [q, a, b] a = 0$ so that $[q, a, q] = [q, a, ab - ba] = -[q, a, ba]$. Also by (7) $[q, a, ba] \in A(a, ba)$ and by (10) $[q, a, ba] = [[a, b], a, ba] = -[[a, ba], a, b] \in A(a, b)$. Hence $[q, a, ba] \in A(a, b) \cap A(a, ba) = \{0\}$ by (6). Thus $[q, a, ba] = 0$ and $[q, a, q] = 0$. $\square$

**Step (B).** $x + x = 0$ for all $x \in D$ (i.e., $D$ has characteristic 2).

**Proof.** $0 = h(q, a, a, b) = [qa, a, b] + [q, a, q] - q[a, a, b] - [q, a, b] a$. By Step (A) $[q, a, q] = 0$ and by (9) $[q, a, b] = 0$ so we have $0 = [qa, a, b] - qp$ or equivalently $qp = [qa, a, b]$. Furthermore, by (11) $[aq, a, b] = [a, a, b] q = pq$ and thus $pq - qp = [aq - qa, a, b] = [[a, q], a, b] = -[[a, q], a, q]$ by (10) $= -[q, a, q] = 0$ by Step (A). Therefore, $pq = qp$.

By (2) and (13) $[p^2, a, b] a = [p^2, a, ab] = 0$. Further calculation yields $p \neq 0 \implies x + x = 0$ for all $x$. $\square$

**Step (C).** $[q, b, y] = 0$ for all $y \in D$.

**Proof.** By earlier calculations, $[q, b, y] \in A(a, b)$ and $[q, b, a] \in A(a, ba)$ for all $y \in D$. Now $0 = g(q, x, b, a) = [q, x, ba] + [q, b, xa] - [q, x, a]b - [q, b, a]x$. The last two terms vanish on transposition, hence $[q, x, ba] = -[q, b, xa] \in A(a, b) \cap A(a, ba)$. Therefore, by (6) we have $[q, b, xa] = 0$ for all $x \in D$. Since $a \neq 0$, for any $y \in D$, there exists $x$ such that $y = xa$, thus $[q, b, y] = 0$ for all $y \in D$. $\square$

**Step (D).** If $N = \{n \in D \mid [n, a, b] = 0\}$, then $NA = A$ where $A = A(a, b)$.

**Proof.** If $n, s$ are arbitrary elements of $N$ and $A$ respectively, then
$$0 = h(n, s, a, b) = [ns, a, b] + [n, s, q] + n[s, a, b] + [n, a, b] s.$$
Since $n \in N$, $[n, a, b] = 0$ and since $s \in A(a, b)$, $[s, a, b] = -sq$, thus
$$0 = [ns, a, b] + [n, s, q] - n(sq) = [ns, a, b] + (ns)q - n(sq) - n(sq).$$
Hence, by Step (B), $[ns, a, b] = (ns)q$ which implies $ns \in A$ and consequently $NA \subseteq A$. But since $1 \in N$, $A = 1A \subseteq NA \subseteq A$ which gives $NA = A$. $\square$

**Step (E).** $[x, q] = 0$ for all $x \in D$ (i.e., $q$ is in the centre of $D$).

**Proof.** $0 = h(x, y, a, b) = [xy, a, b] + [x, y, q] + x[y, a, b] + [x, a, b] y$ and hence
$$[xy, a, b] = [x, y, q] + x[y, a, b] + [x, a, b] y. \tag{††}$$

For any $s \in A$, from (††) we compute $[p(qs), a, b]$ and using $qs \in NA = A$ by Step (D) along with the identities, we arrive at
$$pq(qs + sq) = [p, s, q]q + [p, q, s]q = 0$$
by (1) and Step (B). Hence, since $p \neq 0$ implies $pq \neq 0$, we have $qs + sq = 0$ which is the same as $[s, q] = 0$ for all $s \in A$. If $n \in N$, then $np \in A$ by Step (D) and thus $[np, q] = 0$. Using (17) with $x = n, y = p, z = q$ we get $[n, q]p = 0$, so $[n, q] = 0$ for all $n \in N$. Now, if $x \in D$, by Step (D), $x = n + s$ where $n \in N$ and $s \in A$, so $[x, q] = [n, q] + [s, q] = 0 + 0 = 0$. $\square$

**Conclusion of the proof.** Step (E) shows $q = [a, b]$ commutes with every element of $D$, i.e., $q$ is central. Together with the identities established in (1)-(14) and Steps (A)-(E), this forces the associator $[x, y, z]$ to vanish for all $x, y, z \in D$, which is precisely the statement that $D$ is alternative. $\square$
