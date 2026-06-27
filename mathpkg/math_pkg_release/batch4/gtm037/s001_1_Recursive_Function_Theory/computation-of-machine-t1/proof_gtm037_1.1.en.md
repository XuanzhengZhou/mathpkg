---
role: proof
locale: en
of_concept: computation-of-machine-t1
source_book: gtm037
source_chapter: "1"
source_section: "1"
---

The statement follows directly from the definition of $T_1$. The machine $T_1$ has two states ($0$ and $1$). When in the initial state $0$ and reading symbol $0$, the machine writes $1$ and goes to state $1$ (row $0 \ 0 \ 1 \ 0$). When in state $0$ and reading $1$, the machine halts (row $0 \ 1 \ 4 \ 0$). Thus, if the scanned cell $Fe = 0$, the machine writes $1$ and goes to the halting state, giving the computation $\langle (F, 0, e), (F_1^e, 0, e) \rangle$. If $Fe = 1$, the machine halts immediately on the first step, giving the computation $\langle (F, 0, e) \rangle$.
