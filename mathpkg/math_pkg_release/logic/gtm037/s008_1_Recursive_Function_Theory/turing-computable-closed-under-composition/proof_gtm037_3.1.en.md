---
role: proof
locale: en
of_concept: turing-computable-closed-under-composition
source_book: gtm037
source_chapter: "3"
source_section: "1"
---

Suppose $f, g_0, \ldots, g_{m-1}$ are computed by $M, N_0, \ldots, N_{m-1}$ respectively. Then the following machine computes $K_n^m(f; g_0, \ldots, g_{m-1})$:

$$T_{\text{left}} \rightarrow T_1 \rightarrow T_{\text{left}} \rightarrow T_{(n+1)\text{copy}} \rightarrow T_l^{n_1} \text{seek } 0 \rightarrow T_{\text{right}} \rightarrow T_0 \rightarrow T_{\text{rend}} \rightarrow N_0 \rightarrow T_{(n+1)\text{copy}} \rightarrow N_1 \rightarrow \cdots \rightarrow T_{(n+1)\text{copy}} \rightarrow N_{m-1} \rightarrow T_{(m+(m-1)n)\text{copy}} \rightarrow T_{(m+(m-2)n)\text{copy}} \rightarrow \cdots \rightarrow T_m \text{copy} \rightarrow M \rightarrow T_{\text{fin}}.$$
