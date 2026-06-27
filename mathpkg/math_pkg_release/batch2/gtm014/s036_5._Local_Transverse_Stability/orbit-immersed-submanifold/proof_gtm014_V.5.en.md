---
role: proof
locale: en
of_concept: orbit-immersed-submanifold
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

Suppose that $\dim X = n$ and $\dim Y = m$. Choose $p$ in $X$ and $q$ in $Y$ with chart nbhds $U$ of $p$ and $V$ of $q$. Via charts we may identify $U$ with $\mathbb{R}^n$, $V$ with $\mathbb{R}^m$, $p$ with $0$, and $q$ with $0$. Consider
$$T: U \times V \times J^k(U, V)_{p,q} \to J^k(U, V)$$
defined by $(p', q', \tau) \mapsto j^k T_{q'} \cdot \tau \cdot j^k(T_{p'}^{-1})$ where $T_c$ is translation by the vector $c$. (This makes sense using the identifications above.) $T$ is a diffeomorphism as it is essentially the inverse of a chart in the manifold structure of $J^k(X, Y)$. (Identify the domain with $\mathbb{R}^n \times \mathbb{R}^m \times J^k(\mathbb{R}^n, \mathbb{R}^m)_{0,0}$ and see II, Theorem 2.6.)

We claim that $T(U \times V \times \mathring{\mathcal{O}}_\sigma) = \mathcal{D}_{\sigma}^{U,V} \equiv$ connected component of $\mathcal{D}_{\sigma} \cap J^k(U, V)$ containing $\sigma$. This will imply the Theorem as $\mathring{\mathcal{O}}_\sigma$ is an immersed submanifold since $T$ is a diffeomorphism; as long as we also show that $\mathcal{D}_{\sigma} \cap J^k(U, V)$ has at most a countable number of components.

First we show that $T(U \times V \times \mathring{\mathcal{O}}_\sigma) \subset \mathcal{D}_{\sigma}^{U,V}$. Since $U \times V \times \mathring{\mathcal{O}}_\sigma$ is connected, it is enough to show that $T(U \times V \times \mathring{\mathcal{O}}_\sigma) \subset \mathcal{D}_{\sigma} \cap J^k(U, V)$. Let $(p', q', \tau)$ be in $U \times V \times \mathring{\mathcal{O}}_\sigma$. Now $\mathring{\mathcal{O}}_\sigma = \mathring{G} \cdot \sigma$ (using Lemma A.14) and $\mathring{G} = \mathring{G}^k(X)_p \times \mathring{G}^k(Y)_q$ where $\mathring{G}^k(X)_p = \{ \alpha \in \mathcal{G}^k(X)_p \mid \det(d\alpha)_p > 0 \}$. Thus $\tau = \beta \cdot \sigma \cdot \alpha^{-1}$ where $\alpha \in \mathring{G}^k(X)_p$ and $\beta \in \mathring{G}^k(Y)_q$.

Now we can represent $\alpha$ and $\beta$ by mappings $a: X \to X$ and $b: Y \to Y$ which are diffeomorphisms on nbhds of $p$ and $q$ respectively. Using Proposition 5.5 we can insure that $a$ and $b$ are globally defined diffeomorphisms. So $\tau = j^k(b)(q) \cdot \sigma \cdot j^k(a^{-1})(p)$.

Now $T(p', q', \tau) = j^k(T_{q'})(q) \cdot \tau \cdot j^k(T_{p'}^{-1})(p')$. By Proposition 5.3, we may assume that $T_{q'}: Y \to Y$ and $T_{p'}: X \to X$ are globally defined diffeomorphisms. Thus $T(p', q', \tau) = (T_{p'} \cdot a, T_{q'} \cdot b) \cdot \sigma \in \mathcal{D}_{\sigma}$.

For the reverse inclusion, let $\tau$ be in $\mathcal{D}_{\sigma}^{U,V}$. Let the source of $\tau$ be $p'$ and the target be $q'$. Consider $\rho = j^k(T_{q'}^{-1})(q') \cdot \tau \cdot j^k(T_{p'})(p)$. Since $T_{p'}$ and $T_{q'}$ are in $\mathrm{Diff}(X)$ and $\mathrm{Diff}(Y)$ respectively (Proposition 5.3 again), we see that $\rho$ is still in $\mathcal{D}_{\sigma}$. Thus there exist $(\gamma, \delta)$ in $\mathrm{Diff}(X) \times \mathrm{Diff}(Y)$ such that $\rho = j^k(\delta)(q) \cdot \sigma \cdot j^k(\gamma^{-1})(p)$ and so $\rho$ is in $\mathring{\mathcal{O}}_\sigma$.

So we have shown that $\mathcal{D}_{\sigma}^{U,V} \subset T(U \times V \times \mathring{\mathcal{O}}_\sigma)$. Also we have shown that $\mathcal{D}_{\sigma} \cap J^k(U, V) \subset T(U \times V \times \mathring{\mathcal{O}}_\sigma)$ so that $\mathcal{D}_{\sigma} \cap J^k(U, V)$ has at most a countable number of components. Since $T$ is a diffeomorphism and $\mathcal{D}_{\sigma}^{U,V}$ is connected we must have that $\mathcal{D}_{\sigma}^{U,V} \subset T(U \times V \times (\text{connected component of } \mathring{\mathcal{O}}_\sigma))$. But certainly $\sigma$ is in $\mathcal{D}_{\sigma}^{U,V} \cap T(U \times V \times \mathring{\mathcal{O}}_\sigma)$ so that $\mathcal{D}_{\sigma}^{U,V} \subset T(U \times V \times \mathring{\mathcal{O}}_\sigma)$. Thus the components of $\mathcal{D}_{\sigma} \cap J^k(U, V)$ are a subset of the components of $T(U \times V \times \mathring{\mathcal{O}}_\sigma)$ and this last set is at most countable.
