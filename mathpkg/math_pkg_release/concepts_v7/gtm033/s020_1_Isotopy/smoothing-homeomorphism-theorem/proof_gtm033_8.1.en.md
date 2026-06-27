---
role: proof
locale: en
of_concept: smoothing-homeomorphism-theorem
source_book: gtm033
source_chapter: "8"
source_section: "1. Isotopy"
---

# Proof of Smoothing Homeomorphism Theorem

**Theorem 1.9.** For $i = 0, 1$ let $W_i$ be an $n$-manifold without boundary which is the union of two closed $n$-dimensional submanifolds $M_i$, $N_i$ such that

$$M_i \cap N_i = \partial M_i = \partial N_i = V_i.$$

Let $h: W_0 \rightarrow W_1$ be a homeomorphism which maps $M_0$ and $N_0$ diffeomorphically onto $M_1$ and $N_1$ respectively. Then there is a diffeomorphism $f: W_0 \approx W_1$ such that $f(M_0) = M_1$, $f(N_0) = N_1$ and $f|_{V_0} = h|_{V_0}$. Moreover $f$ can be chosen so as to coincide with $h$ outside a given neighborhood $Q$ of $V_0$.

*Proof.* Choose a tubular neighborhood $\tau_i$ for $V_i$ in $W_i$. This defines a collar $\tau_i|_{M_i}$ on $V_i$ in $M_i$, and $\tau_i|_{N_i}$ on $V_i$ in $N_i$. We have another collar $h(\tau_0|_{M_0})$ on $V_1$ in $M_1$, which is the collar induced from $\tau_0|_{M_0}$ by $h|_{M_0}$.

By the ambient tubular neighborhood Theorem 1.8, we can isotop $h|_{M_0}: M_0 \rightarrow M_1$ to a new diffeomorphism $f': M_0 \rightarrow M_1$, with $f' = h$ on $V_0$ and on $M_0 - Q$, such that $f'(\tau_0|_{M_0})$ has the same $V_1$-germ as $\tau_1|_{M_1}$. Similarly we can isotop $h|_{N_0}: N_0 \rightarrow N_1$ to $f'': N_0 \rightarrow N_1$ so that $f'' = h$ on $V_0$ and on $N_0 - Q$, and the collar $f''(\tau_0|_{N_0})$ has the same $V_1$-germ as $\tau_1|_{N_1}$.

Since $f'$ and $f''$ agree on $V_0$ (both equal $h|_{V_0}$), and their collars match the germs of $\tau_1$, they can be glued along $V_0$ to produce a diffeomorphism $f: W_0 \approx W_1$ with the required properties. $\square$
