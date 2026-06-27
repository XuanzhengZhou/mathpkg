---
role: proof
locale: en
of_concept: simultaneous-mapping-reduction
source_book: gtm049
source_chapter: "6"
source_section: "6.3"
---

Since $V = M \oplus [c]$, every $m \in M$ can be written uniquely as $mf = mf' + xc$ with $mf' \in M$ and $x \in F$. The map $f' \colon M \to M$ defined by $m \mapsto mf'$ is linear because for any $m_1, m_2 \in M$ and $\lambda \in F$,
$$(m_1 + m_2)f = m_1f + m_2f = (m_1f' + x_1c) + (m_2f' + x_2c) = (m_1 + m_2)f' + (x_1 + x_2)c,$$
and
$$(\lambda m_1)f = \lambda(m_1f) = \lambda(m_1f' + x_1c) = (\lambda m_1)f' + (\lambda x_1)c.$$
By uniqueness of the decomposition, $(m_1 + m_2)f' = m_1f' + m_2f'$ and $(\lambda m_1)f' = \lambda(m_1f')$, so $f'$ is linear. Similarly define $g'$ on $M$.

Now compute $(fg)'$. For $m \in M$, write $mg = mg' + yc$. Then
$$m(fg) = (mg')f + y(cf).$$
Since $c$ is an eigenvector of $f$, $cf = \lambda c$ for some $\lambda \in F$. Moreover, $mg' \in M$, so $mg' f = (mg')f' + zc$ for some $z \in F$. Thus
$$m(fg) = (mg')f' + (z + y\lambda)c.$$
But $m(fg) = (m(fg)') + w c$ by definition of $(fg)'$. By uniqueness of the decomposition into $M \oplus [c]$, we obtain $(fg)' = f'g'$.
