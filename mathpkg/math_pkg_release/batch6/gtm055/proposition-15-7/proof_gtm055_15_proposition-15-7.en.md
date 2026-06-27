---
role: proof
locale: en
of_concept: proposition-15-7
source_book: gtm055
source_chapter: "15"
source_section: "Section 16_Section_16"
---

Proof. It is clear that if $M$ is bounded, then $M$ is weakly bounded. On the other hand, if $M$ is weakly bounded, and if $j$ denotes the natural embedding of $\mathcal{E}$ in $\mathcal{E}^{**}$, then $j(M)$ is, by hypothesis, pointwise bounded on $\mathcal{E}^{*}$, and is therefore bounded in $\mathcal{E}^{**}$ by the uniform boundedness theorem (Th. 12.15). Since $j$ is an isometry, the proposition follows. (Note that we here use the fact that $\mathcal{E}^{*}$ is always complete, whether $\mathcal{E}$ itself is complete or not; see Proposition 12.2.)

Example C. Let $\{x_n\}_{n=1}^{\infty}$ be a weakly convergent sequence in a normed space $\mathcal{E}$. Since convergent sequences in $\mathbb{C}$ are bounded, it follows that $\{x_n\}$ is weakly bounded, and therefore bounded. It is worth noting that this argument fails for more general nets, and that, in fact, it is possible for an unbounded net to be weakly convergent (cf. Problem A or Problem 3L).

Example D. Let $\mathcal{E}$ and $\mathcal{F}$ be normed spaces, and let $\mathcal{E}_w$ and $\mathcal{F}_w$ denote the topological linear spaces obtained by equipping $\mathcal{E}$ and $\mathcal{F}$, respectively, with their weak topologies. Suppose $T$ is a bounded linear transformation

on $\Delta$ for every $f$ in $\mathcal{E}^*$. (Such an $\mathcal{E}$-valued mapping is said to be weakly analytic on $\Delta$.) If we write $Q(\Phi; \zeta, \xi)$ for the difference quotient

$$Q(\Phi; \zeta, \xi) = \frac{\Phi(\zeta + \xi) - \Phi(\zeta)}{\xi}$$

whenever it is defined (that is, for all $\zeta$ in $\Delta$ and $\xi \neq 0$ such that $\zeta + \xi$ is also in $\Delta$), then it is clear from linearity that

$$f(Q(\Phi; \zeta, \xi)) = Q(f \circ \Phi; \zeta, \xi)$$

for every $f$ in $\mathcal{E}^*$. Hence if $K$ denotes a compact subset of $\Delta$, then there exists a positive number $\varepsilon$ and, for each $f$ in $\mathcal{E}^*$, a positive number $M_f$, such that

$$\frac{1}{|\zeta - \eta|} |Q(f \circ \Phi; \zeta, \xi) - Q(f \circ \Phi; \zeta, \eta)| \leq M_f$$

for all $\zeta$ in $K$ and all $\xi$, $\eta$ such that $0 < |\xi|, |\eta| < \varepsilon$ and $\zeta \neq \eta$ (see Example 5I). In other words the set

$$\left\{ \frac{1}{\xi - \eta} \left[ Q(\Phi; \zeta, \xi) - Q(\Phi; \zeta, \eta) \right] : \zeta \in K, 0 < |\xi|, |\eta| < \varepsilon, \zeta \neq \eta \right\}$$

is weakly bounded in $\mathcal{E}$, and is therefore norm bounded. Hence there exists a single positive number $M$ such that

$$\| Q(\Phi; \zeta, \xi) - Q(\Phi; \zeta, \eta) \| \leq M

Example F. Let $\mathcal{E}$ and $\mathcal{F}$ be two Banach spaces, and let $\Psi$ be a mapping of a domain $\Delta$ in $\mathbb{C}$ into $\mathcal{L}(\mathcal{E}, \mathcal{F})$. An argument entirely similar to the one presented in the preceding example shows that if $\Psi$ possesses the property that the mapping $\Psi_x(\lambda) = \Psi(\lambda)(x)$ is an analytic $\mathcal{F}$-valued mapping for every vector $x$ in $\mathcal{E}$, then the mapping $\Psi$ is automatically analytic as a mapping of $\Delta$ into $\mathcal{L}(\mathcal{E}, \mathcal{F})$. The details are left to the interested reader.

Example G. Analytic mappings taking their values in Banach spaces turn up frequently in functional analysis. We reconsider here one very important instance of such a mapping that has already appeared. Let $\mathcal{A}$ be a unital Banach algebra and let $x$ be an element of $\mathcal{A}$. We recall from Chapter 12 that the spectrum $\sigma_{\mathcal{A}}(x)$ is, by definition, the set of complex numbers $\lambda$ such that $\lambda - x$ is not invertible in $\mathcal{A}$, and that if $\lambda_0 \notin \sigma_{\mathcal{A}}(x)$, so that $\lambda_0 - x$ is invertible in $\mathcal{A}$, then

$$(\lambda - x)^{-1} = \sum_{n=0}^{\infty} (\lambda_0 - \lambda)^n (\lambda_0 - x)^{-(n+1)}$$

for every complex number $\lambda$ such that $|\lambda - \lambda_0| < 1/||\lambda_0 - x|^{-1}$ (Prop. 12.12). As was noted in Chapter 12, this shows that the spectrum $\sigma_{\mathcal{A}}(x)$ is closed, but it also shows that the resolvent $R_x(\lambda) = (\lambda - x)^{-1}$ is a locally analytic $\mathcal{A}$-valued mapping on the resolvent set $\mathbb{C} \setminus \sigma_{\mathcal{A}}(x)$, i.e., $R_x(\lambda)$ is an

There is a natural and far-reaching generalization of the notion of the weak topology on a normed space. Suppose $\mathcal{E}$ is an arbitrary linear space and $\mathcal{M}$ is an arbitrary linear manifold of linear functionals defined on $\mathcal{E}$. The coarsest topology on $\mathcal{E}$ making all of the functionals in $\mathcal{M}$ continuous, that is, the topology (inversely) induced on $\mathcal{E}$ by the family of functionals in $\mathcal{M}$ (see Chapter 3) will be called simply the topology induced on $\mathcal{E}$ by $\mathcal{M}$. (There is no loss of generality in assuming $\mathcal{M}$ to be a linear manifold; if $\mathcal{M}$ is an arbitrary set of linear functionals on $\mathcal{E}$, and if $\mathcal{M}$ denotes the linear submanifold of the full algebraic dual of $\mathcal{E}$ generated algebraically by $\mathcal{M}$, then every functional in $\mathcal{M}$ is continuous with respect to the topology inversely induced by $\mathcal{M}$ (Prob. 12U), so the latter topology coincides with the topology induced by $\mathcal{M}$.) If we continue to use the notation (1), writing $\sigma_f$ for the pseudonorm

$$\sigma_f(x) = |f(x)|, \quad x \in \mathcal{E},$$

for each $f$ in $\mathcal{M}$, then by Lemma 15.1 the topology induced on $\mathcal{E}$ by $\mathcal{M}$ coincides with the (linear) topology induced on $\mathcal{E}$ by the indexed family $\{\sigma_f\}_{f \in \mathcal{M}}$. Thus we obtain the following result, whose proof is virtually a repetition of the proofs of Propositions 15.2 and 15.3 and Corollary 15.4, and is therefore omitted.
