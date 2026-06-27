---
role: proof
locale: en
of_concept: theorem-serre
source_book: gtm029
source_chapter: "VII"
source_section: "11"
---

The fact that the length $\varphi_M(q)$ of $M_q$ is finite follows immediately from Theorem 40 and from the fact that $A$ is a ring with d.c.c. In order to prove that $\

where all homomorphisms, except the one in the middle, are natural homomorphisms. ($i$ is the inclusion isomorphism into $M, j$ the canonical homomorphism of $M$ onto the difference module $P$.) In this sequence, the image of each homomorphism is equal to the kernel of the following one. In the terminology of cohomological algebra this is expressed by saying that the sequence (1) is exact. If we start from the homogeneous elements of degree $q$ of $N$ or $M$, we get the exact sequence

(2) $0 \rightarrow N_q \xrightarrow{i} M_q \xrightarrow{\theta} M_{q+1} \xrightarrow{j} P_{q+1} \rightarrow 0$.

We now use the following lemma (a proof of this lemma will be given immediately after the proof of the theorem):

Lemma. Let $0 \rightarrow E_1 \rightarrow E_2 \rightarrow \cdots \rightarrow E_n \rightarrow 0$ be an exact sequence of $A$-modules, having finite lengths $\ell(E_i)$. Then the alternating sum $\ell(E_1) - \ell(E_2) + \ell(E_3) - \cdots + (-1)^{n-1}\ell(E_n)$ of the lengths of these modules is equal to 0.

In our particular case, and with the notation which has been introduced before, the lemma gives the relation

(3) $\varphi_M(q+1) - \varphi_M(q) = \varphi_P(q+1) - \varphi_N(q)$.

By the induction hypothesis, for $q$ large enough $\varphi_P(q+1)$ and $\varphi_N(q)$ are polynomials in $q$, of degree at most $n-2$. Hence the first difference $\varphi_M(q+1) - \varphi_M(q)$ is, for $q$ large, a polynomial of degree at most $n-2$ in $q$, and this polynomial takes integral values for all large values of $q$.

We now observe that since $q^s = s! \binom{q}{s}$ and a polynomial in $q$, of degree $s-1$, it follows that every polynomial $f(q)$ in $q$,

coefficients $q$ are integers for all $q$ and $s$ it follows from the above expression of $f(q)$ that also $c_d$ is an integer, and this proves our assertion.

Applying this result to the first difference $\varphi_M(m) - \varphi_M(m-1)$, where $m$ is a sufficiently high integer, say $m \geq N$, we can write

(5) $\varphi_M(m) - \varphi_M(m-1) = a_0 \binom{m-1}{n-2} + a_1 \binom{m-1}{n-3} + \cdots + a_{n-2}, (m \geq N)$

where the $a_i$ are integers. Let us also write

(6) $\varphi_M(m) - \varphi_M(m-1) = a_0 \binom{m-1}{n-2} + a_1 \binom{m-1}{n-3} + \cdots + a_{n-2} + c_m,$

$m = 2, 3, \cdots, N-1,$

$\varphi_M(1) = c_1,$

where we set $t(s)=0$ if $t < s$ and where $c_1, c_2, \cdots, c_{N-1}$ are integers. If we add relations (4) for $h=q-1, q-2, \cdots, s-1$ we find the identity

$q(s) = \binom{q-1}{s-1} + \binom{q-2}{s-1} + \cdots + \binom{s}{s-1} + 1,$

and using this identity we find, by adding the relations (5) for $m=q, q-1, \cdots, N$ and the $N-1$ relations (6):

$\varphi_M(q) = a_0 \binom{q-1}{n-1} + a_1 \binom{q-2}{n-2} + \cdots + a_{n-2} \binom{q}{1} + a_{n-1}, (q \geq N)$

where $a_{n-1}$ is a suitable constant

REMARK (2). Let $E$ and $F$ be two homogeneous submodules of the graded module $M$. Since $(E + F)_q = E_q + F_q$ and $(E \cap F)_q = E_q \cap F_q$, the $\mathfrak{A}$-modules $(E + F)_q / E_q$ and $F_q / (E \cap F)_q$ are isomorphic. Therefore we have for every $q$, the relation:

(7) $$\varphi_E(q) + \varphi_F(q) = \varphi_{E + F}(q) + \varphi_{E \cap F}(q).$$

In the case of two homogeneous ideals $\mathfrak{A}$, $\mathfrak{B}$ in the polynomial ring $R$, (7) gives the relation

(8) $$\chi(\mathfrak{A}; q) + \chi(\mathfrak{B}; q) = \chi(\mathfrak{A} + \mathfrak{B}; q) + \chi(\mathfrak{A} \cap \mathfrak{B}; q).$$

REMARK (3). Let $E$ be a homogeneous submodule of a graded module $M$. Since $E_q \subset M_q$, we have the relation

(9) $$\varphi_E(q) \leq \varphi_M(q).$$

In the case of two homogeneous ideals $\mathfrak{A}$, $\mathfrak{B}$ such that $\mathfrak{A} \subset \mathfrak{B}$, relation (9) gives:

(10) $$\chi(\mathfrak{A}; q) \geq \chi(\mathfrak{B}; q).$$

REMARK (4). It is often necessary to distinguish the characteristic function $\varphi_E(q)$ (or $\chi(\mathfrak{A}; q)$) from the polynomial which is equal to this function for $q$ large enough. In such a case we denote this polynomial by $\bar{\varphi}_E$ (or $\bar{\chi}(\mathfrak{A}; q)$). We call this polynomial the characteristic polynomial of $E$ (or $\mathfrak{A}$).

The degree of the characteristic polynomial of a homogeneous ideal $\mathfrak{A}$ is closely

their projective dimensions. By normalization (§ 9, Theorem 31) there exists a homogeneous system of integrity $\{G_1, \cdots, G_n\}$ composed of forms of like degree $h$ in $k[X_1, \cdots, X_n]$ such that $w \cap k[G_1, \cdots, G_n] = (G_{d+1}, \cdots, G_n)$. Since $w$ is the radical of $F$, there exists an exponent $h'$ such that $G_j h' E \subset F$ for $j=d+1, \cdots, r$. Thus, if we set $F_i = G_i h'$, $k[F_1, \cdots, F_n]$ is a homogeneous subring of $k[X_1, \cdots, X_n]$, and, since $k[X_1, \cdots, X_n]$ is a finite module over $k[F_1, \cdots, F_n]$, $E$ is also a finite graded module over $k[F_1, \cdots, F_n]$. Since $E/F$ is annihilated by the ideal $(F_{d+1}, \cdots, F_n)$, $E/F$ is actually a graded module over $k[F_1, \cdots, F_d]$.

Then Theorem 41 shows that the degree of $\bar{\varphi}_{E/F}(q)$ is at most $d-1$.

On the other hand, no non-zero element of $k[F_1, \cdots, F_d]$ is in the radical of the submodule (0) of $E/F$. Let $(\alpha_1, \cdots, \alpha_i)$ be a finite basis of $M=E/F$ over $S=k[F_1, \cdots, F_d]$, composed of homogeneous elements. The radical of (0) in $S\alpha_i$, i.e., the set $\mathfrak{A}_i$ of elements $x \in S$ such that $x^e \alpha_i=0$ for some $e$, is an ideal in $S$ (and even a homogeneous one).

Since $\bigcap \mathfrak{
