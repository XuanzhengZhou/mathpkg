---
role: proof
locale: en
of_concept: two-body-problem-reduction
source_book: gtm060
source_chapter: "2"
source_section: "10"
---

**Proof.** The equations of motion are:
$$m_1 \ddot{\mathbf{r}}_1 = -\frac{\partial U}{\partial \mathbf{r}_1}, \quad m_2 \ddot{\mathbf{r}}_2 = -\frac{\partial U}{\partial \mathbf{r}_2},$$
where $U = U(|\mathbf{r}_1 - \mathbf{r}_2|)$.

Define the center of mass $\mathbf{r}_0 = (m_1 \mathbf{r}_1 + m_2 \mathbf{r}_2)/(m_1 + m_2)$. By the theorem on conservation of momentum, $\ddot{\mathbf{r}}_0 = 0$, so $\mathbf{r}_0$ moves uniformly and linearly.

Now consider the relative vector $\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2$. Multiplying the first equation by $m_2$, the second by $m_1$, and subtracting:
$$m_1 m_2 \ddot{\mathbf{r}} = m_1 m_2 (\ddot{\mathbf{r}}_1 - \ddot{\mathbf{r}}_2) = -m_2 \frac{\partial U}{\partial \mathbf{r}_1} + m_1 \frac{\partial U}{\partial \mathbf{r}_2}.$$

Since $U$ depends only on $|\mathbf{r}|$, we have $\partial U/\partial \mathbf{r}_1 = -\partial U/\partial \mathbf{r}_2 = \partial U/\partial \mathbf{r}$. Thus
$$m_1 m_2 \ddot{\mathbf{r}} = -(m_1 + m_2) \frac{\partial U}{\partial \mathbf{r}}.$$

Dividing by $m_1 + m_2$ gives $m \ddot{\mathbf{r}} = -\partial U / \partial \mathbf{r}$ where $m = m_1 m_2 / (m_1 + m_2)$ is the reduced mass.

In particular, for Newtonian attraction, the relative motion traces a conic section with focus at the common center of mass.
