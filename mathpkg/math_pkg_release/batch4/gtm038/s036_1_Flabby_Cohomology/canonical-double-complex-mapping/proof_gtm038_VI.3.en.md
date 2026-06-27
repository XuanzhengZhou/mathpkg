---
role: proof
locale: en
of_concept: canonical-double-complex-mapping
source_book: gtm038
source_chapter: "VI"
source_section: "3"
---
The canonical double complex is defined by $C_{ij} = C^j(\mathfrak{U}, \mathcal{S}_i)$, where $\mathcal{S}_0 \rightarrow \mathcal{S}_1 \rightarrow \cdots$ is a flabby resolution of $\mathcal{S}$. The differentials are: $d' = (-1)^j d$ where $d$ is induced by the flabby resolution, and $d'' = \delta$ the Čech coboundary.

**Definition of $\varphi_{ij}$.** Let $q_{ij}: Z_{ij} \rightarrow H_{ij}$ be the canonical projection. For $\xi_{ij} \in Z_{ij}$ ($d'\xi_{ij}=0, d''\xi_{ij}=0$), since the columns are augmented cochain complexes and $\mathcal{S}_{i-1}$ is flabby, there exists $\eta_{i-1,j} \in C_{i-1,j}$ with $d'\eta_{i-1,j} = \xi_{ij}$.

(a) $d''(d''\eta_{i-1,j}) = 0$, $d'(d''\eta_{i-1,j}) = -d''(d'\eta_{i-1,j}) = d''(-\xi_{ij}) = 0$. Therefore $d''\eta_{i-1,j}$ lies in $Z_{i-1,j+1}$.

The class of $d''\eta_{i-1,j}$ in $H_{i-1,j+1}$ does not depend on the choice of $\eta_{i-1,j}$: if $\eta^*$ is another choice, then $\eta - \eta^* \in Z_{i-1,j}$, and if $i=1$, then $\gamma^* := \eta - \eta^*$ satisfies $d''\gamma^* = 0$. Thus $d''\gamma^* \in B_{0,j+1}$, and $q_{0,j+1}(d''\eta) = q_{0,j+1}(d''\eta^*)$.

(b) Let $\xi_{ij} \in B_{ij}$. If $i \geqslant 1$ and $j \geqslant 1$, then $\xi_{ij} = d'd''\gamma$ with $\gamma \in C_{i-1,j-1}$ and $d''(d''\gamma) = 0$. If $j = 0$, then $\xi_{ij} = d'\gamma^*$ with $d''\gamma^* = 0$. Therefore the definition depends only on the cohomology class of $\xi_{ij}$.

(c) From (a), $d''\eta_{i-1,j} \in Z_{i-1,j+1}$.

Because of (a), (b), and (c), $\varphi_{ij}$ actually defines a mapping from $H_{ij}$ to $H_{i-1,j+1}$. It is clear that the map is a homomorphism.

The existence of $\psi_{ij}$ follows by an analogous construction. When both $\varphi_{ij}$ and $\psi_{ij}$ exist, one verifies that
$$\varphi_{ij} \circ \psi_{ij} \circ q_{i-1,j+1} \circ d'' = \varphi_{ij} \circ q_{ij} \circ d' = q_{i-1,j+1} \circ d'' \circ d'$$
which establishes the commutation relation between these maps.
