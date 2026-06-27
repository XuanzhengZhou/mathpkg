---
role: proof
locale: en
of_concept: max-flow-min-cut-theorem-classical
source_book: gtm054
source_chapter: "IV"
source_section: "19"
---

The proof of the Classical Form of the Max-Flow–Min-Cut Theorem reduces to the algebraic formulation C6 proved in an earlier section for integral networks. The equivalence between the two formulations is established by Exercise E3. In the rational case, the proof of C6 suffices. In the real case, additional limit arguments are needed: the iteration process need not increase the flow value by a fixed minimum amount and may not terminate in finitely many steps. If a sequence $h_0, h_1, \ldots$ of feasible flows is constructed via the iteration process, boundedness by the capacity $k$ guarantees the existence of a limit function $h \in \mathbb{R}^D$ such that $\lim_{i \to \infty} h_i(x, y) = h(x, y)$ for all $(x, y) \in D$. A further limit argument completes the proof in the real case.
