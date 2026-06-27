---
role: proof
locale: en
of_concept: two-body-problem-reduction
source_book: gtm060
source_chapter: "2"
source_section: "10"
---

The equations of motion are $m_1 \ddot{r}_1 = -\partial U/\partial r_1$, $m_2 \ddot{r}_2 = -\partial U/\partial r_2$ with $U = U(|r_1 - r_2|)$.

By the momentum theorem, $r_0$ moves uniformly: $\ddot{r}_0 = 0$.

For $r = r_1 - r_2$, multiply the first equation by $m_2$, the second by $m_1$, and subtract:
$$m_1 m_2 \ddot{r} = -m_2 \frac{\partial U}{\partial r_1} + m_1 \frac{\partial U}{\partial r_2} = -(m_1 + m_2) \frac{\partial U}{\partial r},$$
since $\partial U/\partial r_1 = \partial U/\partial r$ and $\partial U/\partial r_2 = -\partial U/\partial r$. Therefore
$$\frac{m_1 m_2}{m_1 + m_2} \ddot{r} = -\frac{\partial U}{\partial r}.$$
