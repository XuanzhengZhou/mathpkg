---
role: proof
locale: en
of_concept: prenex-quantifier-equivalence
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

We proceed by induction on $m$. For $m = 0$, $\varphi$ is a sentence with no variables, and hence $\mathcal{L}$ has individual constants. Thus the assumption $\mathfrak{A} \equiv_0 \mathfrak{B}$ means that $\mathfrak{A}^- \cong \mathfrak{B}^-$. Hence, obviously, $\mathfrak{A} \models \varphi$ iff $\mathfrak{B} \models \varphi$.

Now assume the result true for $m$, for all logics $\mathcal{L}$ and all pairs of $\mathcal{L}$-structures. Suppose $\varphi$ is a prenex sentence with $m + 1$ initial quantifiers and $\mathfrak{A} \equiv_{m+1} \mathfrak{B}$. We take only the case where the first quantifier of $\varphi$ is existential, so that $\varphi = \exists v_0 \psi$ where $\psi$ has $m$ initial quantifiers. Since $\mathfrak{A} \equiv_{m+1} \mathfrak{B}$, for every $a \in A$ there is $b \in B$ such that $(\mathfrak{A}, a) \equiv_m (\mathfrak{B}, b)$. By the induction hypothesis applied to $\psi$ and the expanded structures, $(\mathfrak{A}, a) \models \psi$ iff $(\mathfrak{B}, b) \models \psi$. From $\mathfrak{A} \models \exists v_0 \psi$ we obtain $a \in A$ with $(\mathfrak{A}, a) \models \psi$, then choose $b \in B$ as above to get $(\mathfrak{B}, b) \models \psi$, hence $\mathfrak{B} \models \exists v_0 \psi$. The converse direction uses the symmetric back-and-forth condition. The case where the first quantifier is universal is handled dually.
