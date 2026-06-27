---
role: proof
locale: en
of_concept: newtons-equations-as-euler-lagrange
source_book: gtm060
source_chapter: "3"
source_section: "13"
---
With $L = T - U$ where $T = \sum_i m_i \dot{\mathbf{r}}_i^2 / 2$ and $U = U(\mathbf{r})$,

$$\frac{\partial L}{\partial \dot{\mathbf{r}}_i} = \frac{\partial T}{\partial \dot{\mathbf{r}}_i} = m_i \dot{\mathbf{r}}_i, \qquad \frac{\partial L}{\partial \mathbf{r}_i} = -\frac{\partial U}{\partial \mathbf{r}_i}.$$

Substituting into the Euler–Lagrange equation $\frac{d}{dt} \frac{\partial L}{\partial \dot{\mathbf{r}}_i} - \frac{\partial L}{\partial \mathbf{r}_i} = 0$ yields

$$\frac{d}{dt}(m_i \dot{\mathbf{r}}_i) + \frac{\partial U}{\partial \mathbf{r}_i} = 0,$$

which is precisely Newton's equation of motion for the $i$-th particle. Thus the Euler–Lagrange equations with $L = T - U$ reproduce Newtonian dynamics.
