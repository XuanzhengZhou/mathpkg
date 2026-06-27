---
role: proof
locale: en
of_concept: extension-of-monoidal-functor-to-tensor-words
source_book: gtm005
source_chapter: "XI"
source_section: "2"
---

The extension is constructed by induction on the structure of tensor words $v$. Tensor words are defined inductively as tensor products $v \square v'$ of shorter words (as defined in Section VII.2).

**Base cases:** For the binary tensor product $\square$, we have $F_\square = F_2$ by definition. For the unit word $e$, we have $F_e = F_0$ by definition.

**Inductive step:** For a composite word $v = v_1 \square v_2$, define

$$F_{v_1 \square v_2} = F_2 \circ (F_{v_1} \square F_{v_2}).$$

That is, the diagram

$$v_1(F a_i) \square v_2(F a_j) \xrightarrow{F_{v_1} \square F_{v_2}} F v_1(a_i) \square F v_2(a_j) \xrightarrow{F_2} F(v_1(a_i) \square v_2(a_j))$$

commutes, giving a natural transformation $F_v : v(F a_1, \ldots, F a_n) \rightarrow F v(a_1, \ldots, a_n)$.

Naturality in $a_1, \ldots, a_n$ follows from the naturality of $F_2$ and the induction hypothesis that $F_{v_1}$ and $F_{v_2}$ are natural. The commutativity of all diagrams formed from these $F_v$ follows from the coherence conditions satisfied by $F_2$ and $F_0$ (the three diagrams in the definition of monoidal functor) together with the inductive construction. Specifically, any diagram of $F_v$ maps factors through repeated applications of $F_2$, and the associativity coherence of $F_2$ with $\alpha$ ensures all such factorizations agree.
