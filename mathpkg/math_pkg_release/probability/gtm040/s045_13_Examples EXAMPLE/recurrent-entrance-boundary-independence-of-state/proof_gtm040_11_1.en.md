---
role: proof
locale: en
of_concept: recurrent-entrance-boundary-independence-of-state
source_book: gtm040
source_chapter: "11"
source_section: "1"
---

We first establish the identity

$${}_1 N_{ij} = {}_0 N_{ij} + {}_1 N_{0j} - \frac{\alpha_j}{\alpha_1} {}_0 N_{i1}. \tag{*}$$

In fact, the mean number of times the process started at $i$ visits $j$ from the time of the first visit to $1$ until before the first visit to $0$ is ${}_0 H_{i1} \, {}_0 N_{1j}$. Thus if we compute in two ways the mean number of times the process started at $i$ visits $j$ before reaching both $0$ and $1$, we obtain

$${}_1 N_{ij} + {}_0 H_{i1} \, {}_0 N_{1j} = {}_0 N_{ij} + {}_1 H_{i0} \, {}_1 N_{0j}.$$

Substitute ${}_1 H_{i0} = 1 - {}_0 H_{i1}$ to get

$${}_1 N_{ij} = {}_0 N_{ij} + {}_1 N_{0j} - {}_0 H_{i1}({}_1 N_{0j} + {}_0 N_{1j}).$$

Applying Lemma 9-9 to the reversed chain $\hat{P}$ under the identification $i \to 1$, $j \to 0$, $k \to j$, we find that the term in parentheses equals $(\alpha_j/\alpha_1) {}_0 N_{11}$. From this, $(*)$ follows.

Equation $(*)$ and the expression for the kernel $J(i,j) = {}_0 N_{ij} + \delta_{j0}$ show immediately that Cauchy sequences of $S$ in the chain relative to state $0$ are Cauchy relative to state $1$, and by symmetry the converse is also true. Thus the completed spaces $*S_0$ and $*S_1$ are identical as metric spaces.

For the assertion about the extreme points, let $J_0$ and $J_1$ be the kernels for the two transient chains. Suppose $J_1(y, \cdot)$ is normalized minimal but $J_0(y, \cdot)$ is not. In any case, $J_0(y, \cdot)$ is normalized since $J_0(y,0) = 1$. Thus

$$J_0(y, \cdot) = \int_{*S_0} J_0(x, \cdot) \, d\nu(x)$$

for some measure $\nu$ on $*S_0$. Using the relation between $J_0$ and $J_1$, one shows that this forces $J_1(y, \cdot)$ to be non-minimal as well, a contradiction. Hence the extreme boundary $B^e$ is also independent of the choice of state $0$.
