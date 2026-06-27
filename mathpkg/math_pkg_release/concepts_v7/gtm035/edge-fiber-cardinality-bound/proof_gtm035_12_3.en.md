---
role: proof
locale: en
of_concept: edge-fiber-cardinality-bound
source_book: gtm035
source_chapter: "12"
source_section: "12.3"
---
# Proof of Lemma 12.3 (Edge Fiber Cardinality Bound)

Let $X = f^{-1}(U)$ lie at most $k$-sheeted over $U$, and let $\alpha$ be a smooth arc on $\partial U$ such that $X$ lies $s$-sheeted over $\alpha$ for some positive integer $s$. We prove that for almost all $\lambda_0 \in \alpha$, there are at most $k + s$ points in $\hat{X}$ lying over $\lambda_0$.

**Claim 1.** For almost all $\lambda_0 \in \alpha$, there exists an open triangle $S$ such that $\overline{S} \subseteq U \cup \{\lambda_0\}$ with vertex at $\lambda_0$, and there exist $k$ single-valued bounded $\mathbb{C}^N$-valued analytic functions on $S$,

$$\omega^1, \omega^2, \ldots, \omega^k,$$

such that

$$f^{-1}(S) = \bigcup_{\nu=1}^{k} \{\omega^\nu(\lambda) : \lambda \in S\}$$

and

$$\lim_{\substack{\lambda \in S \\ \lambda \to \lambda_0}} \omega^\nu(\lambda) \text{ exists}.$$

*Proof of Claim 1.* Fix $\tau \in U$ such that $f^{-1}(\tau)$ consists of exactly $k$ distinct points $z_1^0, \ldots, z_k^0$. Let $g$ be a polynomial in $\mathbb{C}^N$ separating these points. By Exercise 11.5, form the polynomial

$$P(\lambda, Z) = Z^k + a_{k-1}(\lambda) Z^{k-1} + \cdots + a_0(\lambda)$$

such that for $\lambda \in U$, the roots of $P(\lambda, Z)$ are the values of $g$ on the $k$ (with multiplicity) points of $f^{-1}(\lambda)$. The coefficient functions $a_j(\lambda)$ are bounded analytic on $U$. Let $D(\lambda)$ be the discriminant of $P(\lambda, Z)$. The set where $D(\lambda) \neq 0$ is dense, and on this set the roots of $P(\lambda, Z)$ are distinct. For each coordinate $z_j$, we form the analogous polynomial $P_j(\lambda, Z)$ whose roots are the values of $z_j$ at the $k$ points of $f^{-1}(\lambda)$, for each $\lambda \in U$.

The finite set $\{a_{t,j}\}$ of bounded analytic functions have nontangential limits everywhere on $\alpha$ except for a set $Q$ of measure zero. We show that the limit property holds for $\lambda_0 \in \alpha \setminus Q$. Fix such $\lambda_0$, the associated triangle $S$, and the functions $\omega^1, \ldots, \omega^k$. For a fixed $\nu$ and coordinate $j$, write $\omega^\nu = (h_1, \ldots, h_N)$. The function $h_j$ is a bounded analytic function on $S$, and for each $\lambda \in S$, $h_j(\lambda)$ is a root of $P_j(\lambda, Z)$. As $\lambda \in S$ approaches $\lambda_0$, the coefficients of $P_j(\lambda, Z)$ approach the coefficients of $P_j(\lambda_0, Z)$. Hence the roots of $P_j(\lambda, Z)$ approach the roots of $P_j(\lambda_0, Z)$. The set $L$ of limit points of $h_j(\lambda)$,

$$L = \bigcap_{m=1}^{\infty} \overline{h_j(\{\lambda \in S : |\lambda - \lambda_0| \leq 1/m\})},$$

is a compact connected subset of the finite set of roots of $P_j(\lambda_0, Z)$. Thus $L$ consists of a single point, and the limit exists. This proves Claim 1.

**Claim 2.** For almost all $\lambda_0 \in \alpha$, the set $\hat{X} \cap f^{-1}(\lambda_0)$ contains at most $k + s$ points.

*Proof of Claim 2.* By Claim 1, for almost all $\lambda_0 \in \alpha$, the $k$-sheeted cover over $U$ extends to $k$ analytic branches on $S$ with limits at $\lambda_0$. These limits give at most $k$ points in $f^{-1}(\lambda_0)$ lying in $\overline{U}$. Additionally, the $s$ points of $X$ over $\alpha$ may contribute further points. If $p$ is any other point of $\hat{X}$ over $\lambda_0$, then Lemma 12.2 implies $p$ is not a peak-point of $\overline{A|_{f^{-1}(\lambda_0)}}$. Consequently, the set of peak-points of $\overline{A|_{f^{-1}(\lambda_0)}}$ is contained in the finite set $\{p_1^0, \ldots, p_k^0, q_1, \ldots, q_s\}$ consisting of the limits of the $k$ branches plus the $s$ points over the arc. Hence $\hat{X} \cap f^{-1}(\lambda_0)$ is a subset of this set of at most $k+s$ points.

**Conclusion.** Claim 2 gives the result: for almost all $\lambda_0 \in \alpha$, $\#(\hat{X} \cap f^{-1}(\lambda_0)) \leq k + s$. This completes Step 2 in the proof of Theorem 12.1: by the regularity of arclength measure, there is a compact subset $E \subseteq \alpha$ of positive measure where the bound holds, and then Theorem 11.12 implies that $f^{-1}(V)$ lies at most $(k+s)$-sheeted over $V$. $\square$
