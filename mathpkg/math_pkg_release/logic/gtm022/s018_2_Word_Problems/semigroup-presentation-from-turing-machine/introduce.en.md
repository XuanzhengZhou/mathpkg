---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

To connect Turing machine computation with algebraic word problems, one encodes instantaneous descriptions as semigroup words. An instantaneous description $\sigma q_i \tau$ (with $\sigma, \tau$ strings of symbols) is mapped to $e\sigma q_i \tau e$, using an end marker $e$ and a halting state symbol $q_\infty$. The Turing machine transitions are then translated into semigroup relations of four types: $(b_0)$ for left moves on blank, $(c)$ for right moves on non-blank, $(c_0)$ for right moves on blank, and $(d)$ for undefined transitions (which lead to the halting state). These relations ensure that one computation step corresponds to one forward substitution in the semigroup.
