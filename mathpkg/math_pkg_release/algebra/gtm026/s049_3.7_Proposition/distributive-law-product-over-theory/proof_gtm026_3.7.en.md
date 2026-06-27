---
role: proof
locale: en
of_concept: distributive-law-product-over-theory
source_book: gtm026
source_chapter: "3"
source_section: "3.7"
---

**Proof.** This is an easy consequence of the commutative diagrams expressing the two distributive law axioms from Definition 3.6. We verify the axioms for the natural transformation $\lambda$ defined by $\lambda_Q(p, x) = \langle p, \mathrm{in}_x T \rangle$, i.e., $\lambda_Q = T(\mathrm{in}_x)(p)$.

Let $F = - \times X$, and recall that a distributive law $\lambda \colon FT \to TF$ (in the sense of 3.6) must satisfy:

1. **(Unit axiom)** $\lambda_Q \circ F(e_Q) = e_{F(Q)}$, i.e., $\lambda_Q \circ (e_Q \times \mathrm{id}_X) = e_{Q \times X}$.

2. **(Multiplication axiom)** $\lambda_Q \circ F(m_Q) = m_{F(Q)} \circ T(\lambda_Q) \circ \lambda_{T(Q)}$.

For the unit axiom, take $(q, x) \in Q \times X$. Then
$$
\lambda_Q(e_Q(q), x) = T(\mathrm{in}_x)(e_Q(q)).
$$
By naturality of the unit $e \colon \mathrm{Id} \to T$, the diagram
$$
\begin{CD}
Q @>{e_Q}>> QT \\
@V{\mathrm{in}_x}VV @VV{T(\mathrm{in}_x)}V \\
Q \times X @>>{e_{Q \times X}}> (Q \times X)T
\end{CD}
$$
commutes, so $T(\mathrm{in}_x) \circ e_Q = e_{Q \times X} \circ \mathrm{in}_x$. Hence
$$
\lambda_Q(e_Q(q), x) = e_{Q \times X}(\mathrm{in}_x(q)) = e_{Q \times X}(q, x),
$$
as required.

For the multiplication axiom, take $(w, x) \in QTT \times X$, where $w \in QTT = T(T(Q))$. The left side is
$$
\lambda_Q(m_Q(w), x) = T(\mathrm{in}_x)(m_Q(w)).
$$
For the right side, first note that $\lambda_{T(Q)}(w, x) = T(\mathrm{in}'_x)(w)$ where $\mathrm{in}'_x \colon T(Q) \to T(Q) \times X$ sends $p$ to $(p, x)$. Then
$$
T(\lambda_Q)(\lambda_{T(Q)}(w, x)) = T(\lambda_Q \circ \mathrm{in}'_x)(w).
$$
For any $p \in T(Q)$, we have $\lambda_Q(\mathrm{in}'_x(p)) = \lambda_Q(p, x) = T(\mathrm{in}_x)(p)$, so $\lambda_Q \circ \mathrm{in}'_x = T(\mathrm{in}_x)$. Thus
$$
T(\lambda_Q \circ \mathrm{in}'_x)(w) = T(T(\mathrm{in}_x))(w).
$$
Now apply $m_{Q \times X}$:
$$
m_{Q \times X}(T(T(\mathrm{in}_x))(w)).
$$
By naturality of the multiplication $m \colon TT \to T$, the diagram
$$
\begin{CD}
(Q \times X)TT @>{T(T(\mathrm{in}_x))}>> (Q \times X)TT \\
@V{m_{Q \times X}}VV @VV{m_{Q \times X}}V \\
(Q \times X)T @>>{T(\mathrm{in}_x)}> (Q \times X)T
\end{CD}
$$
commutes, yielding $m_{Q \times X} \circ T(T(\mathrm{in}_x)) = T(\mathrm{in}_x) \circ m_Q$. Hence the right side equals $T(\mathrm{in}_x)(m_Q(w))$, matching the left side.

Both axioms are satisfied, so $\lambda$ is indeed a distributive law of $-\times X$ over $\mathbf{T}$.
