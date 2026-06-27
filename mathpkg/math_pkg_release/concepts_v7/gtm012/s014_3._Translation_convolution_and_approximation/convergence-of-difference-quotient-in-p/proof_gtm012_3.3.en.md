---
role: proof
locale: en
of_concept: convergence-of-difference-quotient-in-p
source_book: gtm012
source_chapter: "3"
source_section: "3. Translation, convolution, and approximation"
---

# Proof of Corollary 3.3: Convergence of Difference Quotient in $\mathcal{P}$

**Corollary 3.3.** If $u \in \mathcal{P}$, then

$$t^{-1}(T_{-t} u - u) \to u \quad (\mathcal{P}) \quad \text{as} \quad t \to 0.$$

Here convergence in $\mathcal{P}$ means convergence with respect to each seminorm $|u|_k = \sum_{j=0}^k |D^j u|$, i.e., uniform convergence of all derivatives.

**Proof.** First observe that differentiation commutes with translation:

$$D^k(T_{-t} u) = T_{-t}(D^k u).$$

Indeed, $D^k(T_{-t} u)(x) = D^k[u(x + t)] = (D^k u)(x + t) = T_{-t}(D^k u)(x)$.

Consequently,

$$
\begin{aligned}
D^k\left[t^{-1}(T_{-t} u - u)\right] &= t^{-1}\left[D^k(T_{-t} u) - D^k u\right] \\
&= t^{-1}\left[T_{-t}(D^k u) - D^k u\right].
\end{aligned}
$$

Since $u \in \mathcal{P}$, we have $D^k u \in \mathcal{P}$ for all $k$. Applying Lemma 3.2 to the function $D^k u$ (in place of $u$), we obtain

$$|t^{-1}[T_{-t}(D^k u) - D^k u] - D(D^k u)| \to 0 \quad \text{as} \quad t \to 0.$$

But $D(D^k u) = D^{k+1} u = D^k(D u)$. Therefore, for each $k \geq 0$,

$$|D^k\left[t^{-1}(T_{-t} u - u)\right] - D^k(D u)| \to 0 \quad \text{as} \quad t \to 0.$$

This means precisely that $t^{-1}(T_{-t} u - u)$ converges to $D u$ in the topology of $\mathcal{P}$ as $t \to 0$. $\square$
