---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

A process in a category $\mathcal{H}$ is simply an endofunctor $X: \mathcal{H} \to \mathcal{H}$, which provides the transition structure for state-based systems. This notion generalizes the idea of a sequential machine's input alphabet and transition function: the endofunctor encodes how inputs transform the state space. For any such process $X$, one may construct the category $\operatorname{Dyn}(X)$ of $X$-dynamics whose objects are pairs $(Q, \delta)$ with $\delta: QX \to Q$, representing state objects equipped with a dynamics morphism.
