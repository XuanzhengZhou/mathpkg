---
role: proof
locale: en
of_concept: corollary-let-variety-defined-polynomial-vanishes
source_book: gtm029
source_chapter: "VII"
source_section: "3"
---

Assume that $(y_0, y_1, \cdots, y_n)$ is a set of strictly homogeneous coördinates of $P$ and let $F(Z)$ be a non-zero polynomial in one indeterminate $Z$, with coefficients in $k(P)$. Since every element of $k(P)$ is a quotient of two forms in $k[y_0, y_1, \cdots, y_n]$, of like degree, we have

$$F(Z) = \left( \sum_i f^{(i)}(y_0, y_1, \cdots, y_n) Z^i \right) / f^{(0)}(y_0, y_1, \cdots, y_n),$$

where $f^{(0)}$ and the $f^{(i)}$ are forms in $k[Y_0, Y_1, \cdots, Y_n]$, of like degree $h$. We have $f^{(0)}(y_0, y_1, \cdots, y_n) \neq 0$, and $f^{(i)}(y_0, y_1, \cdots, y_n) \neq 0$ for some $i \neq 0$. Let $G(Y_0, Y_1, \cdots, Y_n) = \sum_i f^{(i)}(Y_0, Y_1, \cdots, Y_n) Y_s^i$. If, say, $f^{(\nu)}(y_0, y_1, \cdots, y_n) \neq 0$ and if we set $G_{\nu+h} = f^{(\nu)}(Y_0, Y_1, \cdots, Y_n) Y_s^{\nu}$, then $G_{\nu+h}$ is the homogeneous component of $G$, of degree $\nu+h$, and we have $

Note that if $\mathfrak{A}$ is an irrelevant ideal (§ 2, p. 154) then $\mathcal{V}(\mathfrak{A})$ is empty, for if $\mathfrak{A}$ is irrelevant then $Y_i^\rho \in \mathfrak{A}$ for some integer $\rho \geq 1$ and for all $i$, showing that no point $(y_0, y_1, \cdots, y_n)$ (not all $y_i$ being zero) can be a zero of $\mathfrak{A}$.

As in the case of the affine space $A_n^K$, we have a natural topology in the projective space $P_n^K$ in which the algebraic (projective) varieties are the closed sets. The closure of any subset $E$ of $P_n^K$, i.e., the least variety containing $E$, is given by $\mathcal{V}(\mathcal{I}(E))$. By a specialization of a point $P$, over $k$, we mean any point $Q$ which belongs to the closure of the point $P$; in symbols: $P \xrightarrow{k} Q$.

These notations and terms are identical with those used in the preceding section for affine varieties. The formulas (1)-(6) continue to hold for projective varieties and homogeneous ideals, and there is no change whatsoever in the proofs except that whenever we use polynomials $f, g$, etc., we must now assume that $f, g, \cdots$ are forms. It is only necessary to bear in mind the fact that the set of homogeneous ideals is closed under all the basic ideal-theoretic operations (see § 2, Theorem 8). The definition of irreducible varieties can be repeated verbatim for projective varieties, and then Theorems 12 and 13 continue to hold, the proofs remaining the same (we need only recall, from § 2, that for a homogeneous ideal $\mathfrak{p}$ to be prime it is sufficient that the condition “$fg \in \mathfrak{p} \Rightarrow f \in \mathfrak{p}$ or $g \in \mathfrak{p}$” be satisfied for forms $f$ and $g

of $K$, and we cannot therefore, in general, regard $(y_0, y_1, \cdots, y_n)$ as a point of $P_n^K$. We do call, however, the $(n+1)$-tuple $(y_0, y_1, \cdots, y_n)$ the general point of $V$. Since the kernel $\mathfrak{p}$ of the canonical homomorphism $k[Y_0, Y_1, \cdots, Y_n] \rightarrow k[y_0, y_1, \cdots, y_n]$ is homogeneous, it follows that $(y_0, y_1, \cdots, y_n)$ is a set of strictly homogeneous coördinates of the general point of $V$.

If $K$ is a universal domain, there exist $k$-isomorphisms of $k(y_0, y_1, \cdots, y_n)$ into $K$. If $\sigma$ is such an isomorphism then the point $(\sigma(y_0), \sigma(y_1), \cdots, \sigma(y_n))$ is a point of $V$ and is also called a general point of $V$; the point $(y_0, y_1, \cdots, y_n)$ may be singled out by referring to it as the canonical general point of $V$. Note that the set $(\sigma(y_0), \sigma(y_1), \cdots, \sigma(y_n))$ is a set of strictly homogeneous coördinates.

The quotient field of the homogeneous coördinate ring $k[Y]/\mathfrak{p}$ is not what is called the function field of $V$. We notice that $k[Y]/\mathfrak{p}$ is a graded ring (see §2, Lemma 1, p. 150), whence we can talk about homogeneous elements of this ring. Then the set of all quotients $a/b$, where $a$ and $b$ are homogeneous elements of like degree in $k[Y]/\mathfrak{p}$ ($b \neq 0$), is obviously a subfield of the quotient field of $k[Y]/\mathfrak{p}$. This subfield we call the

homogeneous ideal in $k[Y_1, \cdots, Y_n]$, then $\mathcal{V}(\mathfrak{A})$ is non-empty and the ideal of the variety $\mathcal{V}(\mathfrak{A})$ is the radical of $\mathfrak{A}$.

PROOF. We set $V = \mathcal{V}(\mathfrak{A})$ and we consider the affine variety $C(V)$ in $A_{n+1}^K$ which is the variety of the ideal $\mathfrak{A}$: it is the set of all points $(x_0, \cdots, x_n)$ in $A_{n+1}^K$ such that $F(x) = 0$ for every $F$ in $\mathfrak{A}$. Since $\mathfrak{A}$ is a homogeneous ideal, the relation $(x_0, \cdots, x_n) \in C(V)$ implies $(tx_0, \cdots, tx_n) \in C(V)$ for every $t$ in $K$. Thus, if $V$ is non-empty, $C(V)$ is a union of straight lines containing the origin $(0, \cdots, 0)$.

It is furthermore clear that a point $(x_0, x_1, \cdots, x_n)$ of $A_{n+1}^K$, different from the origin, belongs to $C(V)$ if and only if the point of $P_n^K$ whose homogeneous coördinates are $x_0, x_1, \cdots, x_n$ belongs to $V$. The variety $C(V)$ is called the representative cone of $V$. Since $\mathfrak{A}$ is non-irrelevant, $C(V)$ is neither empty nor is it reduced to the origin (by the affine Nullstellensatz). Hence $V$ is non-empty.

Since $V$ is non-empty, it is clear that the (homogeneous) ideal of $V$ is contained in the ideal of $C(V)$. Conversely, if a polynomial $F(Y_0, \cdots, Y_n)$ vanishes on $C(V)$, we have, for every point $(x_0, \cdots, x_n)$ of $V$ and for every

variety can also be proved by means of the existence theorem for algebraic places (VI, § 4, Theorem 5', Corollary 2), as follows:

Let $(y_0, y_1, \cdots, y_n)$ be the canonical general point of an irreducible non-empty variety $V$ in $P_n^K$, and let $\mathcal{P}$ be an algebraic place of $k(y_0, y_1, \cdots, y_n)/k$. If $v$ is the corresponding valuation, we may assume that $v(y_0) \leq v(y_i), 1 \leq i \leq n$. Let $\alpha_i = \mathcal{P}(y_i/y_0)$, where $\alpha_i$ is then different from $\infty$ and is algebraic over $k$. The point $(1, \alpha_1, \cdots, \alpha_n)$ is immediately seen to belong to $V$, and thus $V$ has an algebraic point, as asserted.

§ 4bis. Further properties of projective varieties. We shall begin by generalizing to projective varieties the notion of the center of a place and the notion of a divisor which have been given for affine varieties in the preceding chapter (VI, § 5bis and § 14).

Let $Q$ be a point $(z_0, z_1, \cdots, z_n)$ of $V$. We consider quotients $f(y_0, y_1, \cdots, y_n)/g(y_0, y_1, \cdots, y_n)$ of elements of the homogeneous coordinate ring of $V$, such that $f$ and $g$ are homogeneous, of like degree, and such that $g(z_0, z_1, \cdots, z_n) \neq 0$. These quotients form a ring, contained in the field $k(V)$, called the local ring of $V$ at the point $Q$, or, briefly, the local ring of $Q$ (on $V$).

Without loss of generality we may assume that $z_0 \neq 0$. Then also $y_0 \neq 0$ since $Q$ is a specialization, over $k$, of the general point $(y_0, y_

that the residue field of $\mathcal{P}$ is contained in the coördinate domain $K$ (this is no essential restriction on $\mathcal{P}$ if $K$ is a universal domain; see VI, § 5bis). If $v$ is the valuation determined by $\mathcal{P}$, then $v(y_i/y_j)$ is meaningful for any $i, j = 0, 1, \cdots, n$, provided $y_j \neq 0$, since $y_i/y_j \in k(V)$. It is clear that there exists an index $s$ such that $v(y_i/y_s) \geq 0$ for $i = 0, 1, \cdots, n$. For such an index $s$ let $\mathcal{P}(y_i/y_s) = b_i \in K$. The $b_i$ are not all zero (since $b_s = 1$) and thus determine a point $Q = (b_0, b_1, \cdots, b_n)$ of $P_n^K$. If $t$ is another index such that $v(y_i/y_t) \geq 0$ for $i = 0, 1, \cdots, n$ and if we set $\mathcal{P}(y_i/y_t) = c_i$, then $b_t c_s = 1$, whence $b_t \neq 0, c_s \neq 0$, and furthermore, $c_i = \mathcal{P}(y_i/y_s \cdot y_s/y_t) = b_i c_s, i = 0, 1, \cdots, n$. This shows that the point $Q$ above depends only on the place $\mathcal{P}$ and not on the choice of the index $s$. It is easily seen that $Q$ belongs to $V$. For if $f(Y_0, Y_1, \cdots, Y_n)$ is any form in the homogeneous ideal of $V$, then we have $f(y_0/y_s, y_1/y_s, \cdots, y_n/y_s) = 0$, and since $\mathcal{P}$ is a $k$-homomorphism it follows that $f(b_0, b_1, \cdots, b_n) = 0$, showing that $

of $k(V)$ having center $W$. We denote this divisor by $v_W$. In particular, if $V/k$ is a normal variety then every irreducible $(r-1)$-dimensional subvariety $W$ of $V/k$ is the center of a unique prime divisor of $k(V)$.

We now assume that $V$ is normal and we introduce the free group of divisors on $V$, i.e., the group generated by the irreducible $(r-1)$-dimensional subvarieties $W$ of $V$. Using the notations of VI, § 14, p. 98, we can now define the divisor $(w)$ of any function $w \neq 0$ in $k(V)$:

$$(w) = \sum v_W(w) \cdot W,$$

where the sum is extended to all the irreducible $(r-1)$-dimensional subvarieties of $V/k$. That the sum (1) is finite can be seen as follows:

In the first place, there is only a finite number of irreducible $(r-1)$-dimensional subvarieties $W$ of $V$ such that (a) $V_a$ contains the general point of $W_a/k$ and (b) $v_W(w) \neq 0$; this assertion concerns only the affine variety $V_a$ and has been proved in VI, § 14 (p. 97).

In the second place, since the intersection of $V$ with the hyperplane $Y_0 = 0$ is at most $(r-1)$-dimensional, there is only a finite number of $(r-1)$-dimensional irreducible subvarieties $W$ of $V$ which do not satisfy condition (a) above.

As has been proved in VI, § 14, p. 99, if $w$ is not a constant, i.e., if $w$ is not algebraic over $k$, then there exists at least one polar prime divisor of $w$, i.e., for at least one $W$ in (1) we must have $v_W(w) < 0$. Upon replacing $w$ by $1/w$ we see, under this same assumption, that we must also have $v_W(w)

denominators, an equation of integral dependence for $\xi$ over $k[x_1, x_2, \cdots, x_n]$ takes the form

(2) $y_0^h \xi^\nu + f^{(1)}(y_0, y_1, \cdots, y_n) \xi^{\nu-1} + \cdots + f^{(\nu)}(y_0, y_1, \cdots, y_n) = 0,$

where each $f^{(i)}$ is a form of degree $h$, with coefficients in $k$. Relation (2) implies that $y_0^h \xi \in \bar{R}$. Since the conductor $\mathfrak{C}$ of $R$ in $\bar{R}$ is irrelevant, it contains a power of each $y_i$. In particular, let, say, $y_0^N \in \mathfrak{C}$. Then $y_0^{N+h} \xi \in R$, and since $\xi$ is homogeneous of degree zero, we have $y_0^{N+h} \xi = g(y_0, y_1, \cdots, y_n)$, where $g$ is a form of degree $N+h$, with coefficients in $k$. Hence $\xi = g(1, x_1, x_2, \cdots, x_n) \in k[x_1, x_2, \cdots, x_n]$.

Conversely, assume that $V$ is normal. We have to show that there exists an integer $N$ such that $y_i^N \bar{R} \subset R$ for $i=0, 1, \cdots, n$. Since $\bar{R}$ is a finite $R$-module (Vol. I, Ch. V, § 4, Theorem 9) and since each element of $\bar{R}$ is a sum of homogeneous elements of $\bar{R}$ (§ 2, Theorem 11), it is sufficient to show that for any homogeneous element $\omega$ of $\bar{R}$ there exists an integer $N$ (depending on $\omega$) such that $y_i^N \omega \in R$, for $i=0, 1, \cdots, n$. Let us show,

Corollary to Theorem 11 (§2) that $\bar{R}$ is a graded ring. Let $\bar{R}_q$ (respectively, $R_q$) be the set of homogeneous elements of $\bar{R}$ (respectively of $R$), of degree $q$. Since, for each $q \geq 1$, $R_q$ is a finite dimensional vector space over $k$ and since $\bar{R}$ is a finite $R$-module (admitting an $R$-basis consisting of homogeneous elements), it follows at once that $\bar{R}_q$ is also a finite-dimensional vector space over $k$. Let $\{u_0, u_1, \cdots, u_m\}$ be a $k$-basis of $\bar{R}_q$ and let $\bar{V}_q$ be the projective variety whose general point is $(u_0, u_1, \cdots, u_m)$. A change of $k$-basis of $\bar{R}_q$ leaves $\bar{V}_q$ unchanged, up to projective equivalence. Thus $\bar{V}_q$ is uniquely determined for each integer $q \geq 0$. We shall prove the following:

If $q$ is sufficiently large then $\bar{V}_q$ is the derived normal model of $V/k$ in $F$, and, moreover, $\bar{V}_q$ is an arithmetically normal variety provided $k$ is maximally algebraic in $F$.

[The proof given below applies without modification to models over "restricted" domain (VI, §18) and yields another proof of Theorem 42 of VI, §18.]

Let $\bar{o}_i = k[y_0/y_i, y_1/y_i, \cdots, y_n/y_i]$ and let $V_i$ be the affine model $V(\bar{o}_i)$, so that $V$ is the union of $V_0, V_1, \cdots, V_n$. Let $V'_i$ be the derived normal model of $V_i$ in $F$, i.e., let $V'_i = V(\bar{o}'_i)$, where $\bar{o}'_i$ is the integral closure of $\bar

with coefficients in $k$. Therefore $y_i/y_0 = y_i y_0^{q-1}/u_0 \in \bar{o}_0$. Thus $\bar{o}_0 \subset \bar{o}_0$. On the other hand, if $\eta$ is any element of $\bar{o}'_0$ then, upon writing an equation of integral dependence of $\eta$ on $\bar{o}_0$, we see at once that for large $q$ the product $\eta y_0^q$ is integral over $R$ and therefore belongs to $\bar{R}_q$. Since $\bar{o}'_0$ is a finite $\bar{o}_0$-module, it follows therefore that if $\{\eta_1, \eta_2, \cdots, \eta_q\}$ is an $\bar{o}_0$-basis of $\bar{o}'_0$ and $q$ is sufficiently large, then all the products $\eta_\alpha y_0^q$ are linear combinations of $u_0, u_1, \cdots, u_m$, with coefficients in $k$, and therefore the $\eta_\alpha$ belong to $\bar{o}_0$. Since also $\bar{o}_0$ is contained in $\bar{o}_0$, the inclusion $\bar{o}'_0 \subset \bar{o}_0$ is proved, for all large $q$.

It now remains to prove that $\bar{V}_q$ is arithmetically normal, i.e., that the homogeneous coordinate ring $I = k[u_0, u_1, \cdots, u_m]$ of $\bar{V}_q/k$ is integrally closed (for large $q$). Let $I'$ be the integral closure of $I$ in its quotient field. Then $I'$ is a graded ring: $I' = I'_0 + I'_1 + \cdots + I'_h + \cdots$ (the degree $h$ of a homogeneous element of $I'$ being defined by stipulating that $u_0, u_1, \cdots, u_m$ are homogeneous elements of degree 1). Since $I \subset \bar{R}$, we have $I' \subset \bar{R}$ and hence $I'_h
