---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A Turing machine configuration captures the complete instantaneous state of a Turing machine during execution: the tape contents (represented as a function from integers to $\{0,1\}$ with only finitely many non-zero entries), the current internal state, and the current head position. A computation step defines how the machine transitions from one configuration to the next by consulting its matrix for the appropriate action based on the current state and scanned symbol. A full computation is a finite sequence of configurations starting from the initial state, proceeding by valid computation steps, and ending when the machine encounters a stop action ($v_j = 4$). This formalizes the step-by-step operation of a Turing machine.
