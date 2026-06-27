---
role: proof
locale: en
of_concept: proposition-175-lel-definitional-expansion-of-lnos
source_book: gtm037
source_chapter: "Part 3"
source_section: "Decidable and Undecidable Theories"
---

It is clear that $(\mathcal{P}, \mathcal{L}_{\text{el}})$ can be obtained as the union, in an obvious sense, of a sequence
$$(\mathcal{P}, \mathcal{L}_{\text{nos}}) = (\mathcal{S}_0, \mathcal{L}_0), (\mathcal{S}_1, \mathcal{L}_1), \dots$$
where at each stage a single new symbol is added to the language together with a defining axiom that satisfies the existence and uniqueness conditions. For each operation symbol $\mathbf{O}$ introduced, the defining axiom ensures that the symbol is eliminable: every formula containing the new symbol is provably equivalent (in the expanded theory) to a formula of the previous language. Since the union of a chain of definitional expansions is again a definitional expansion, the full structure $(\mathcal{P}, \mathcal{L}_{\text{el}})$ is a definitional expansion of the base $(\mathcal{P}, \mathcal{L}_{\text{nos}})$. In particular, for the summation operator $\Sigma(\mathbf{O})$, the definition is given by:

$$\forall v_0 \dots \forall v_m \{\Sigma(\mathbf{O})(v_0, \dots, v_{m-1}) = v_m \leftrightarrow \exists v_{m+1}[\varphi_4(v_{m+1}, \mathbf{0}, \mathbf{0}) \wedge$$
$$\forall v_{m+2} \{ \mathbf{s}v_{m+2} \leq v_{m-1} \rightarrow \exists v_{m+3}[\varphi_4(v_{m+1}, v_{m+2}, v_{m+3}) \wedge$$
$$\varphi_4(v_{m+1}, \mathbf{s}v_{m+2}, v_{m+3} + \mathbf{O}(v_0, \dots, v_{m-2}, v_{m+2})) \} \wedge$$
$$\varphi_4(v_{m+1}, v_{m-1}, v_m) \}.$$

To show that this is a definition of $\Sigma(\mathbf{O})$ amounts to proving in $\mathcal{S}_{i+1}$ the existence and uniqueness conditions. Two unformalized statements equivalent to the defining axioms for $\Sigma$ are:

(7) $$\sum(f)(x_0, \dots, x_{m-1}, 0) = 0, \text{ while } \sum(f)(x_0, \dots, x_{m-1}, y + 1)$$
$$= \sum(f)(x_0, \dots, x_{m-1}, y) + f(x_0, \dots, x_{m-1}, y);$$

(8) $$\sum(f)(x_0, \dots, x_{m-1}) = y \text{ iff there is a } z \text{ such that } \beta(z, 0) = 0 \text{ and for all } w \text{ with } \mathbf{s}w \leq x_{m-1}, \beta(z, \mathbf{s}w) = \beta(z, w) + f(x_0, \dots, x_{m-2}, w), \text{ and } \beta(z, x_{m-1}) = y.$$
