---
role: proof
locale: en
of_concept: lindstrom-main-lemma
source_book: gtm037
source_chapter: "XII"
source_section: "4"
---

**Proof.** By assumption there is an $\mathscr{L}$-elementary class $\mathbf{M}$, say in a language $L'$, such that there is no finitely axiomatizable elementary class in the usual sense with the same infinite members as $\mathbf{M}$. Then

(1) there is no finitely axiomatizable elementary class $\mathbf{N}$ with the same denumerable members as $\mathbf{M}$.

For let $\mathbf{N}$ be any elementary class. Since $L_{\text{fo}} \subseteq \mathscr{L}$, we also have that $\mathbf{N}$ is an $\mathscr{L}$-elementary class. Now let $\mathbf{Q} = (\mathbf{N} \sim \mathbf{M}) \cup (\mathbf{M} \sim \mathbf{N})$. If $\mathbf{N}$ and $\mathbf{M}$ had the same denumerable members, then $\mathbf{Q}$ would have no denumerable members while containing at most infinite members. By the downward Löwenheim–Skolem theorem for $\mathscr{L}$, $\mathbf{Q}$ would have no infinite members at all, meaning $\mathbf{N}$ and $\mathbf{M}$ have the same infinite members, contradicting the choice of $\mathbf{M}$.

By the definition of $\mathscr{L} \not\subseteq_{1\text{inf}} L_{\text{fo}}$, there is an expansion $L''$ of $L'$ and an $\mathscr{L}$-sentence $\psi$ such that, letting $\mathbf{K} = \operatorname{Mod}_{\mathscr{L}, L''} \psi$, the class $\mathbf{K} \upharpoonright L$ satisfies conditions (ii)–(iv). In particular, there is a language $L''$ with finitely many relation symbols $S_0, \ldots, S_{m-1}, T_0, \ldots, T_4, P$ (of ranks $n_0, \ldots, n_{m-1}, 3, 2, 2, 3, 3, 1$ respectively), where $P$ is the distinguished unary predicate, such that $\mathbf{K}$ is defined by an $\mathscr{L}$-sentence encoding the following conditions (2)–(10):

(5) for every $a \in A$, the relation $f_a = \{(x, y) : (a, x, y) \in T_3\}$ is a function mapping $T_0^{\mathfrak{A}}$ into $A$;

(6) if $x$ is the $T_2^{\mathfrak{A}}$-first element of $T_0^{\mathfrak{A}}$, then there are $a, b$ such that $(x, a, b) \in T_4^{\mathfrak{A}}$;

(7) if $(x, a, b) \in T_4^{\mathfrak{A}}$, $x \in T_0^{\mathfrak{A}}$, $y$ is the immediate $T_2^{\mathfrak{A}}$-successor of $x$, and $z \in A$, then there exist $c, d, u$ such that $(y, c, d) \in T_4^{\mathfrak{A}}$, $f_c x = z$, $f_d x = u$, while for every $v \in T_0^{\mathfrak{A}}$, if $v \neq x$ then $f_c v = f_a v$ and $f_d v = f_b v$;

(8) like (7), but with $a$ and $b$ interchanged in its conclusion;

(9) if $(x, a, b) \in T_4^{\mathfrak{A}}$, $i < m$, and $y = \langle y_0, \ldots, y_{n_i-1} \rangle$ is a sequence of $T_i^{\mathfrak{A}}$-predecessors of $x$, then $f_a \circ y \in R_i^{\mathfrak{A}}$ iff $f_b \circ y \in S_i^{\mathfrak{A}}$;

(10) if $(x, a, b) \in T_4^{\mathfrak{A}}$ and $y$ and $z$ are $T_2^{\mathfrak{A}}$-predecessors of $x$, then $f_a y = f_a z$ iff $f_b y = f_b z$.

Next, let $L^{iv}$ be the reduct of $L''$ to the symbols $S_0, \ldots, S_{m-1}$. Clearly $L'$ is isomorphic to $L^{iv}$, via the isomorphism $g$ taking $R_i$ to $S_i$ for $i < m$.

To verify the construction satisfies the required conditions, one checks conditions (2)–(10). Conditions (2), (3), (4), (5), and (6) are straightforward. For condition (7): assume the hypotheses, so that

$$\langle g_a 0, \ldots, g_a (x - 1) \rangle \, I_x \, \langle g_b 0, \ldots, g_b (x - 1) \rangle,$$

hence there is a $u \in \omega$ such that $\langle g_a 0, \ldots, g_a (x - 1), z \rangle \, I_{x+1} \, \langle g_b 0, \ldots, g_b (x - 1), u \rangle$. Choose $c, d \in \omega$ so that $g_c = (g_a)_{z}$ (the function extending $g_a$ with value $z$ at $x$) and $g_d = (g_b)_{u}$. Then the conclusion of (7) follows. Condition (8) is checked similarly.

For condition (9): assume the hypothesis, so $\langle g_a 0, \ldots, g_a (x - 1) \rangle \, I_x \, \langle g_b 0, \ldots, g_b (x - 1) \rangle$. By 26.6(ii)(3),(4), for any atomic formula $\varphi'$ with variables among $v_0, \ldots, v_{x-1}$ we have $\mathfrak{A} \models \varphi'[g_a 0, \ldots, g_a (x - 1)]$ iff $\mathfrak{B} \models \varphi'[g_b 0, \ldots, g_b (x - 1)]$. Noting that $f_t = g_t$ for all $t \in \omega$, we obtain

$$f_a \circ y \in \mathbf{R}_i^{\mathfrak{A}} \quad \text{iff} \quad \langle g_a y_0, \ldots, g_a y_{n_i-1} \rangle \in \mathbf{R}_i^{\mathfrak{A}}$$
$$\text{iff} \quad \mathfrak{A} \models \mathbf{R}_i v_{y_0} \cdots v_{y(n_i-1)}[g_a 0, \ldots, g_a (x - 1)]$$
$$\text{iff} \quad \mathfrak{B} \models \mathbf{R}_i v_{y_0} \cdots v_{y(n_i-1)}[g_b 0, \ldots, g_b (x - 1)]$$
$$\text{iff} \quad f_b \circ y \in \mathbf{R}_i^{\mathfrak{B}},$$

establishing (9).

Now assume that $x I_p y$ and $b \in C$ (the case $b \in D$ is symmetric). By the encoding there exist $c, d \in A$ such that $(a_p, c, d) \in \mathbf{T}_4^{\mathfrak{A}}$ and for all $i < p$, $f_c a_i = x_i$ and $f_d a_i = y_i$. From (7) it follows that there are $c', d' \in A$ such that $(a_{p+1}, c', d') \in \mathbf{T}_4^{\mathfrak{A}}$, $f_{c'} a_p = b$, while for any $v \in \mathbf{T}_0^{\mathfrak{A}}$ different from $a_p$ we have $f_{c'} v = f_c v$ and $f_{d'} v = f_d v$. Hence

$$\langle x_0, \ldots, x_{p-1}, b \rangle \, I_{p+1} \, \langle y_0, \ldots, y_{p-1}, f_{d'} a_p \rangle,$$

as required by the back-and-forth property 26.6(ii)(3).

Finally, to verify the atomic formula condition: assume $p \in \omega$, $x, y \in {}^p A$, $x I_p y$, and $Fv(\varphi') \subseteq \{v_0, \ldots, v_{p-1}\}$ where $\varphi'$ is atomic. Choose $c, d$ as above. If $\varphi'$ is $v_i = v_j$, then

$$\mathfrak{C} \models v_i = v_j[x] \;\text{iff}\; x_i = x_j \;\text{iff}\; f_c a_i = f_c a_j$$
$$\text{iff}\; f_d a_i = f_d a_j \quad \text{(by (10))}$$
$$\text{iff}\; \mathfrak{D} \models v_i = v_j[y].$$

If $\varphi'$ is $\mathbf{R}_i v_{j_0} \cdots v_{j(n_i-1)}$ with $i < m$, then

$$\mathfrak{C} \models \varphi'[x] \;\text{iff}\; \langle x_{j_0}, \ldots, x_{j(n_i-1)} \rangle \in \mathbf{R}_i^{\mathfrak{C}}$$
$$\text{iff}\; \langle f_c a_{j_0}, \ldots, f_c a_{j(n_i-1)} \rangle \in \mathbf{R}_i^{\mathfrak{C}}$$
$$\text{iff}\; \langle f_d a_{j_0}, \ldots, f_d a_{j(n_i-1)} \rangle \in \mathbf{R}_i^{\mathfrak{D}} \quad \text{(by (9))}$$
$$\text{iff}\; \mathfrak{D} \models \varphi'[y].$$

This completes the verification of all conditions. The construction yields the desired class $\mathbf{K}$ satisfying (i)–(iv), where condition (i) follows from the encoding of an infinite back-and-forth system, (ii) from the fact that $P^{\mathfrak{A}}$ corresponds to the finite initial segment of the constructed sequence, (iii) from the existence of denumerable models by the downward Löwenheim–Skolem theorem, and (iv) from the fact that $\mathbf{K}$ is the reduct of an $\mathscr{L}$-elementary class. $\square$
