---
role: proof
locale: en
of_concept: connected-complex-pathwise-connected
source_book: gtm047
source_chapter: "1"
source_section: "Connectivity"
---

Let $v_0 \in K^{0}$. We shall show that for each $v \in K^{0}$ there is a path in $|K^{1}|$ from $v_0$ to $v$. Let $V$ be the set of all vertices $v$ of $K$ that have this property, and let $K_1$ be the set of all simplexes of $K$ all of whose vertices lie in $V$. Then $K_1$ is a subcomplex of $K$, and no edge of $K$ intersects $|K_1|$ and $K^{0} - V$. Therefore no simplex of $K$ intersects $|K_1|$ and $K^{0} - V$. Let $K_2 = K - K_1$. Then $K_2$ is a subcomplex of $K$, and $K_1 \cap K_2 = \emptyset$. Since $K$ is connected, $K_2 = \emptyset$. Therefore $K_1 = K$, and $V$ is all of $K^{0}$, which was to be proved.

Now take $v \in \sigma \in K$, $w \in \tau \in K$. Take a path in $\sigma$ from $v$ to a vertex $v_0$ of $\sigma$, then a path in $|K^{1}|$ from $v_0$ to a vertex $v_1$ of $\tau$, and finally a path in $\tau$ from $v_1$ to $w$. These fit together to give a path from $v$ to $w$.
