---
role: proof
locale: en
of_concept: null-basic-example-potential-kernel
source_book: gtm040
source_chapter: "6"
source_section: "The basic example"
---

From the null case entry probability formulas, we have
$$^i\hat{\lambda}_j = \begin{cases} 1 & \text{if } j > i, \\ 0 & \text{if } j \leq i. \end{cases}$$

Since $^i\hat{N}_{jj} = {^i N_{jj}}$ (the diagonal entries of the potential kernel are the same for $P$ and $\hat{P}$), the Green function is:
$$\hat{G}_{ij} = {^i\hat{\lambda}_j} \cdot {^i N_{jj}} = \begin{cases} 1 \cdot {^i N_{jj}} & \text{if } j > i, \\ 0 & \text{if } j \leq i. \end{cases}$$

In the null recurrent case, ${^i N_{jj}} = 1$ for all $j$, since the expected number of visits to $j$ starting from $i$ (before absorption, in the extended chain) equals the probability of ever reaching $j$ times the expected number of visits. Here the absorption probability from any state is 0 (null recurrence), and the process is certain to visit any state, giving ${^i N_{jj}} = 1$. Thus $\hat{G}_{ij} = 1$ for $j > i$ and 0 otherwise.

For the potential kernel $C$, using the relation $C_{ij} = \frac{\beta_j}{\beta_i} \hat{G}_{ji}$:
$$C_{ij} = \frac{\beta_j}{\beta_i} \hat{G}_{ji} = \begin{cases} \frac{\beta_j}{\beta_i} \cdot 1 & \text{if } i > j \text{ (i.e., } j < i), \\ 0 & \text{if } i \leq j \text{ (i.e., } j \geq i). \end{cases}$$

The statement $C = G$ follows from the general identity $G = C$ for null recurrent chains that are in duality with respect to $\beta$. In the transient case, the formula for the potential kernel $N$ specialized to the basic example gives $-C$ (or $-G$) as the limit when $\beta_\infty \to +\infty$.
