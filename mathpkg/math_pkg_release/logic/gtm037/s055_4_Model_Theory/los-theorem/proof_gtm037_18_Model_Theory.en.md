---
role: proof
locale: en
of_concept: los-theorem
source_book: gtm037
source_chapter: "18"
source_section: "Model Theory"
---

Let $\{\mathcal{A}_i\}_{i \in I}$ be a family of $L$-structures, $F$ an ultrafilter over $I$, and $\mathcal{C} = \prod_{i \in I} \mathcal{A}_i / F$ the reduced product. Define the diagonal embedding $f: \bigcap_{i \in I} A_i \to \mathcal{C}$ as follows. For $a \in \bigcap_{i \in I} A_i$, let $x_a^j$ be the constant sequence with value $a$ at each coordinate, and set $fa = [x_a^j]$.

The map $f$ is injective: if $a \neq b$, then $b = (x_b^j)_j$ and hence $j \notin \{i : (x_a^j)_i = (x_b^j)_i\}$, so $\lnot (x_a^j \bar{F} x_b^j)$ and $fa = [x_a^j] \neq [x_b^j] = fb$. Also, $f$ maps onto $\bigcap_{i \in I} A_i / \bar{F}$; for, if $y \in \bigcap_{i \in I} A_i$, then $(x_y^j)_j = y_j$ and hence $\{j\} \subseteq \{i : (x_y^j)_i = y_i\} \in F$ and so $fy_j = [x_y^j] = [y]$.

The map $f$ preserves operations: if $O$ is an $m$-ary operation symbol, $a_0, \ldots, a_{m-1} \in A_j$, and $b = O^{\mathcal{A}_j}(a_0, \ldots, a_{m-1})$, then with $B = \bigcap_{i \in I} A_i$,

$$[O^{\mathcal{A}_j}(x_{a_0}^j, \ldots, x_{a_{m-1}}^j)] = [x_b^j].$$

Thus with $C = \bigcap_{i \in I} A_i / \bar{F}$,

$$f O^{\mathcal{A}_j}(a_0, \ldots, a_{m-1}) = fb = [x_b^j] = [O^{\mathcal{A}_j}(x_{a_0}^j, \ldots, x_{a_{m-1}}^j)] = O^{C}([x_{a_0}^j], \ldots, [x_{a_{m-1}}^j]) = O^{C}(fa_0, \ldots, fa_{m-1}).$$

The map $f$ also preserves relations. If $R$ is an $m$-ary relation symbol, $a_0, \ldots, a_{m-1} \in A_j$, and $C$ is as above, then $\langle a_0, \ldots, a_{m-1} \rangle \in R^{\mathcal{A}_j}$ iff the corresponding equivalence classes satisfy the relation in $C$ by the ultrafilter property.

We now prove the theorem itself by induction on $\varphi$. First suppose that $\varphi$ is $\sigma = \tau$. Then

$$\mathcal{C} \models \varphi[[\ ] \circ x] \quad \text{iff} \quad \sigma^{\mathcal{C}}([\ ] \circ x) = \tau^{\mathcal{C}}([\ ] \circ x)$$
$$\text{iff} \quad [\sigma^{\mathcal{C}}x] = [\tau^{\mathcal{C}}x] \quad \text{by (1)}$$
$$\text{iff} \quad \{i : (\sigma^{\mathcal{C}}x)_i = (\tau^{\mathcal{C}}x)_i\} \in F$$
$$\text{iff} \quad \{i : \sigma^{\mathcal{A}_i}(\operatorname{pr}_i \circ x) = \tau^{\mathcal{A}_i}(\operatorname{pr}_i \circ x)\} \in F \quad \text{by 18.14}$$
$$\text{iff} \quad \{i : \mathcal{A}_i \models \varphi[\operatorname{pr}_i \circ x]\} \in F.$$

The other atomic case (relation symbols) is entirely analogous.

We now check the result for $\varphi = \psi \lor \chi$; the proof is similar for $\lnot$ and $\land$.

$$\mathcal{C} \models \varphi[[\ ] \circ x] \quad \text{iff} \quad \mathcal{C} \models \psi[[\ ] \circ x] \text{ or } \mathcal{C} \models \chi[[\ ] \circ x]$$
$$\text{iff} \quad \{i \in I : \mathcal{A}_i \models \psi[\operatorname{pr}_i \circ x]\} \in F \text{ or } \{i \in I : \mathcal{A}_i \models \chi[\operatorname{pr}_i \circ x]\} \in F \quad \text{by induction hypothesis}$$
$$\text{iff} \quad \{i \in I : \mathcal{A}_i \models \psi[\operatorname{pr}_i \circ x]\} \cup \{i \in I : \mathcal{A}_i \models \chi[\operatorname{pr}_i \circ x]\} \in F$$
$$\text{iff} \quad \{i \in I : \mathcal{A}_i \models (\psi \lor \chi)[\operatorname{pr}_i \circ x]\} \in F.$$

The last equivalence uses the ultrafilter property that a union of two sets belongs to $F$ iff at least one of the sets belongs to $F$. The cases for $\lnot$ and $\land$ follow similarly, using the properties of ultrafilters (a set belongs to $F$ iff its complement does not, for negation; and $F$ is closed under finite intersections, for conjunction).

The case of the existential quantifier $\exists v_k \varphi$ follows by the axiom of choice: if the set of indices where $\mathcal{A}_i \models \exists v_k \varphi[\operatorname{pr}_i \circ x]$ belongs to $F$, then for each such $i$ we can choose a witness $a_i \in A_i$, extend the assignment $x$ accordingly, and apply the induction hypothesis. This completes the proof of Łoś's Theorem.
