---
role: proof
locale: en
of_concept: proposition-19-10
source_book: gtm055
source_chapter: "18-19"
source_section: "Section 20_Section_20"
---

Proof. If $X$ is a basis for $M$, then for each vector $x$ in $M$ we have $x = \lim_N E_N x$, from which it follows at once (by the uniform boundedness theorem; Theorem 12.15) that the sequence $\{E_N\}$ is uniformly bounded on $M$ (cf. Example 12V). Suppose, on the other hand, that there is a positive constant $M$ such that $\|E_N y\| \leq M \|y\|$ for all $N$ in $\mathbb{N}_0$ and all $y$ in $M$, and let $x$ be a vector in $M$. Then for any positive number $\varepsilon$ there exists a linear combination $x' = \lambda_0 x_0 + \cdots + \lambda_K x_K$ of vectors belonging to $X$ such that $\|x - x'\| < \varepsilon$, and, by the preceding lemma, $E_N x' =

and similarly that

$$\int_Z \bar{f} s_D(f) d\theta = 2\pi \sum_{n \in D} |c_n(f)|^2.$$

In particular, setting $f = s_D(f)$, we obtain $\|s_D(f)\|_2^2 = 2\pi \sum_{n \in D} |c_n(f)|^2$. (We here use the fact that $s_D$, like all expansion operators, is idempotent; recall that $\|g\|_2^2 = \int_Z g\bar{g} d\theta$ for every function $g$ in $\mathcal{L}_2(Z)$.) Hence, summarizing, we see that if $f \in \mathcal{L}_2(Z)$, then

$$\|f - s_D(f)\|_2^2 = \int_Z (f - s_D(f)) (\bar{f} - \bar{s}_D(f)) d\theta = \|f\|_2^2 - 2\pi \sum_{n \in D} |c_n(f)|^2$$

$$= \|f\|_2^2 - \|s_D(f)\|_2^2.$$

Thus $s_D$ (regarded as an operator on $\mathcal{L}_2(Z)$) is a contraction for every choice of $D$. In particular, this is true for $D = \{-M, -M + 1, \ldots, N - 1, N\}$, where $M$ and $N$ are arbitrary nonnegative integers, and it follows (Prob. N) that $U$ is actually a basis for $\mathcal{L}_2(Z)$ in the primary sense. (The sequence $U$ is also an indexed basis for $\mathcal{L}_2(Z)$, as defined in Problem R; these observations are not of great importance since the sum of a Fourier series is invariably taken to be its principal value.) The inequality

$$2\pi \sum_{n=-N}^{+N} |c_n(f)|^2 \leq \|f\|_2^2,$$

valid for all nonnegative integers $N$ and every $f$ in $\mathcal{L}_2(Z)$ according to (7), is known as

(The function $f\bar{g}$ is integrable $[\mu]$ by the Hölder inequality; we are here using the fact that $p = 2$ is its own Hölder conjugate.) This inner product is sesquilinear (that is, linear in the first variable $f$ and conjugate linear in the second variable $g$; see Chapter 2) and is not to be confused with the bilinear pairing of $\mathcal{L}_2(X)$ with itself introduced in Example 17H, from which the inner product may be derived, to be sure, by writing $(f, g) = \langle f, \bar{g} \rangle$, $f, g \in \mathcal{L}_2(X)$. In terms of the inner product $(,)$ the norm $\| \|_2$ is given by

$$\| f \|_2 = (f, f)^{1/2}, \quad f \in \mathcal{L}_2(X).$$

A Banach space in which the norm is given in this way by a sesquilinear functional is called a Hilbert space. Thus, in particular, $\mathcal{L}_2(Z)$ is a Hilbert space, and in terms of inner products it is the substance of the calculations in Example H that

$$(f, s_D(f)) = (s_D(f), f) = \| s_D(f) \|_2^2$$

and therefore

$$\| f - s_D(f) \|_2^2 = (f - s_D(f), f - s_D(f)) = \| f \|_2^2 - \| s_D(f) \|_2^2$$

for every function $f$ in $\mathcal{L}_2(Z)$. The theory of Hilbert spaces and operators thereon will form the principal subject matter of Volume II.

The explicit construction of a basis for a given Banach space may present serious difficulties, and (as Example D shows) require considerable ingenuity. Nevertheless, within a few years of the publication of Schauder’s original memoir [59], bases had been constructed for all of the classical separable Banach spaces, and as new separable Banach spaces were introduced and studied over the intervening years, bases for them were eventually found. Accordingly, the basis problem was formulated

C. If $\{x_\gamma\}_{\gamma \in \Gamma}$ is a summable family of vectors in a Banach space $\mathcal{E}$, and if $\Gamma'$ is any subset of $\Gamma$, then $\{x_\gamma\}_{\gamma \in \Gamma'}$ is also summable. Show also that, if we set $\Gamma'' = \Gamma \setminus \Gamma'$, then

$$\sum_{\gamma \in \Gamma} x_\gamma = \sum_{\gamma \in \Gamma'} x_\gamma + \sum_{\gamma \in \Gamma''} x_\gamma.$$

Show, more generally, that if $\{\Gamma_\delta\}_{\delta \in \Delta}$ is an arbitrary indexed partition of the index set $\Gamma$ into disjoint subsets $\Gamma_\delta$, then

$$\sum_{\gamma \in \Gamma} x_\gamma = \sum_{\delta \in \Delta} \left( \sum_{\gamma \in \Gamma_\delta} x_\gamma \right).$$

D. Show that if $\mathcal{E}$ is a finite dimensional Banach space, and if $\{x_\gamma\}_{\gamma \in \Gamma}$ is an arbitrary indexed family of vectors in $\mathcal{E}$, then $\{x_\gamma\}$ is summable if and only if it is absolutely summable. (Hint: See Problem 4N for the one dimensional case. Recall (Prob. 11J) that if $\mathcal{E}$ is finite dimensional with basis $\{x_1, \ldots, x_r\}$, then $\|\lambda_1 x_1 + \cdots + \lambda_r x_r\|_0 = |\lambda_1| + \cdots + |\lambda_r|$ defines a norm on $\mathcal{E}$ that is equivalent with the given one.)

Our experience to date with the differences between the finite and infinite dimensional cases would lead us to expect the converse of Problem D to be valid, i.e., to guess that in an infinite dimensional normed space there should exist summable families of vectors that are not absolutely summable. That this is indeed the case is the substance of the (surprisingly deep) Dvoretsky–Rogers theorem (see [24]).

E. Let $\mathcal{E}$ be a Banach

F. Let $\mathcal{E}$ be a Banach space, and suppose given a sequence $\{x_n\}_{n=0}^{\infty}$ of vectors in $\mathcal{E}$.

(i) The series $\sum_{n=0}^{\infty} x_n$ is said to be unconditionally convergent if it is convergent to a sum $x$ and if, for every permutation $\sigma$ of $\mathbb{N}_0$, the series $\sum_{n=0}^{\infty} x_{\sigma(n)}$ also converges to $x$. (A permutation of an infinite set is defined, just as for finite sets, as a one-to-one mapping of the set onto itself. As a matter of fact, it is easy to see that if all of the permuted series $\sum_{n=0}^{\infty} x_{\sigma(n)}$ converge, then they all must converge to the same vector $x$.) Prove that $\sum_{n=0}^{\infty} x_n$ is unconditionally convergent if and only if the indexed family $\{x_n\}_{n \in \mathbb{N}_0}$ is summable, and that, in this event,

$$\sum_{n=0}^{\infty} x_n = \sum_{n \in \mathbb{N}_0} x_n.$$

(Hint: Use Problem E(i).)

(ii) A subseries of the series $\sum_{n=0}^{\infty} x_n$ is any series of the form $\sum_{k=0}^{\infty} x_{nk}$ where $\{x_{nk}\}_{k=0}^{\infty}$ is a subsequence of $\{x_n\}$. The series $\sum_{n=0}^{\infty} x_n$ is said to be subseries convergent if every subseries of the given series is convergent. Prove that $\sum_{n=0}^{\infty} x_n$ is subseries convergent if and only if the indexed family $\{x_n\}_{n \in \mathbb{N}_0}$ is summable.

(Hint: Use Problem E(i).)

Problem F, together with Problem 4N, yields a proof of the classical result that an infinite series of scalars is unconditionally convergent if and only if it is absolutely convergent.

G. Let $\mathcal{E}$ be a Banach space and let $\{x

the converse direction, that if an infinite series

$$\sum_{n=1}^{\infty} x_n$$

in $\mathcal{E}$ has the property that $\sum_{n=0}^{\infty} \lambda_n x_n$ is convergent for every bounded sequence of scalars $\{\lambda_n\}$, then $\{x_n\}_{n \in \mathbb{N}_0}$ is summable as an indexed family.

H. Let us equip an index family $\Gamma$ with the counting measure $\kappa$. (See Example 7J; it doesn’t matter which $\sigma$-ring of subsets of $\Gamma$ we declare to be measurable so long as it contains all the singletons $\{\gamma\}$.) Show that for any separable Banach space $\mathcal{E}$ the collection of all absolutely summable vector families $\{x_\gamma\}_{\gamma \in \Gamma}$ in $\mathcal{E}$ coincides with the Banach space $\mathcal{L}_1(\Gamma; \mathcal{E})$ of Theorem 17.11, and that for any such family we have

$$\sum_{\gamma \in \Gamma} x_\gamma = \int_{\Gamma} x_\gamma d\kappa(\gamma)$$

(cf. Theorem 17.14 and Problem 7Q).

I. An indexed family $\{x_\gamma\}_{\gamma \in \Gamma}$ of vectors in a Banach space $\mathcal{E}$ is said to be weakly summable if the family of scalars $\{f(x_\gamma)\}_{\gamma \in \Gamma}$ is summable in $\mathbb{C}$ for every $f$ in $\mathcal{E}^*$. Likewise, $\{x_\gamma\}$ is weakly summable to sum $x$ if (for some $x$ in $\mathcal{E}$)

$$\sum_{\gamma} f(x_\gamma) = f(x)$$

for every $f$ in $\mathcal{E}^*$.

(i) Show that $\{x_\gamma\}$ is weakly summable if and only if the net $\{s_D\}_{D \in \mathcal{D}}$ of finite sums $s_D = \sum_{\gamma \in D} x_\gamma$ is weakly Cauchy in $\mathcal{E}$. (See Problem 1

that if $\mathcal{E}$ is a reflexive Banach space, then every weakly summable indexed family in $\mathcal{E}$ is weakly summable to a sum in $\mathcal{E}$.

It is a remarkable result due to Bessaga and Pelczynski [9] that if $\mathcal{E}$ is a Banach space in which there exists a single indexed family that is weakly summable but not summable (in norm), then $\mathcal{E}$ has a subspace that is equivalent to the space $(c_0)$. (The converse result is obvious in view of Problem I(ii).) Thus in the presence of any condition on $\mathcal{E}$ that prevents it from having such a subspace, every weakly summable indexed family in $\mathcal{E}$ is necessarily summable. Reflexivity is one such condition, to be sure (Ex. 16C; Prob. 16H), but there are many others. Thus, for example (Orlicz [51]): If $\mathcal{E}$ is weakly sequentially complete, then every weakly summable indexed family of vectors in $\mathcal{E}$ is summable.

In Problems F and G it was seen that several senses of summability are equivalent for families of vectors indexed by $\mathbb{N}_0$ (or any other index system with the same order type). Since the Cauchy criterion is the critical ingredient in these arguments, and since the Cauchy criterion may fail for weak summability, as noted in Problem I, the fact developed in the following problem comes as a distinctly pleasant surprise.

L. (Orlicz–Pettis Theorem) Let $\mathcal{E}$ be a Banach space, let $X = \{x_n\}_{n=0}^{\infty}$ be a sequence in $\mathcal{E}$ such that the series $\sum_{n=0}^{\infty} x_n$ is weakly convergent to a sum $x$, that is, such that $\sum_{n=0}^{\infty} f(x_n) = f(x)$ for every $f$ in $\mathcal{E}^*$, and let $\mathcal{M}$ be the subspace of $\mathcal{E}$ spanned by $X$.

(i) Let $\{f_p\}_{p=1}^{\infty}$ be a sequence in the unit ball $(\mathcal

(iv) Use (iii) to prove that if $\sum_{n=0}^{\infty} x_n$ is weakly subseries convergent and if $\{f_p\}_{p=1}^{\infty}$ is an arbitrary infinite sequence in $(\mathcal{E}^*)_1$, then $\{f_p\}$ has a subsequence $\{f_p_k\}$ such that $\{Tf_p_k\}$ is convergent in $(\ell_1)$, and conclude that $T((\mathcal{E}^*)_1)^-$ is compact in $(\ell_1)$. (Hint: Since $\mathcal{M}$ is separable, the sequence $\{f_p|\mathcal{M}\}_{p=1}^{\infty}$ has a weak* convergent subsequence $\{f_p_k|\mathcal{M}\}$ (Prob. 15P). Use the Hahn–Banach theorem to extend $\lim_k (f_p_k|\mathcal{M})$ to a bounded linear functional $f_0$ in $(\mathcal{E}^*)_1$, and invoke (iii) to conclude that $T((\mathcal{E}^*)_1)^-$ is sequentially compact. Finally, recall Prob. 4Q.) Thus $T$ is a compact linear transformation (Prob. 17Y).

(v) (Pettis [52]) Prove that a weakly subseries convergent infinite series in a Banach space is actually subseries convergent and therefore summable (in norm) as an indexed family. (Hint: If for each nonnegative integer $k$ we write $P_k$ for the projection

$$P_k \{\xi_0, \ldots, \xi_k, \xi_{k+1}, \ldots\} = \{0, \ldots, 0, \xi_k, \xi_{k+1}, \ldots\},$$

then $\|P_k x\| \to 0$ for each $x$ in $(\ell_1)$, and therefore, by a standard compactness argument, $\{P_k\}_{k=1}^{\infty}$ tends to zero uniformly on $T((\mathcal{E}^*)_1)$; in other words, $\lim_k \|P_k T\| = 0$. Use the fact that

$$\left\|x_J - \sum

Show that $X$ is a basis in the Cauchy sense for the subspace $\mathcal{M}$ of $\mathcal{E}$ that it spans if and only if the sequence $\{E_n\}_{n=0}^{\infty}$ is uniformly bounded on $\mathcal{M}$. (Hint: Show first that $E_M E_N = E_N E_M = E_M \wedge N$, and then adapt the proof of Proposition 19.10.) Show also that $X$ is a basis in the primary sense for $\mathcal{M}$ if and only if the double sequence $\{E_M, N\}_{M, N=0}^{\infty}$ is uniformly bounded on $\mathcal{M}$, where

$$E_{M, N} x = \sum_{n=-M}^{+N} \alpha_n(x) x_n, \quad x \in \mathcal{E},$$

for all nonnegative integers $M$ and $N$.

O. A sequence $X = \{x_n\}_{n=0}^{\infty}$ in a Banach space $\mathcal{E}$ is said to be a weak basis for $\mathcal{E}$ if for every vector $x$ in $\mathcal{E}$ there exists a unique sequence $\{\alpha_n\}_{n=0}^{\infty}$ of complex numbers such that the series $\sum_{n=0}^{\infty} \alpha_n x_n$ converges weakly to $x$ (see Problem L). Prove that a weak basis for a Banach space $\mathcal{E}$ is actually a Schauder basis for $\mathcal{E}$. (Hint: Use Proposition 19.7 to show that $X$ and the corresponding sequence $A$ of coefficient functionals form a biorthogonal system; then use the uniform boundedness theorem to prove that the sequence of expansion operators is uniformly bounded.) Develop the analogous results for a weak basis indexed by $\mathbb{Z}$.

P. If $X = \{x_n\}_{n=0}^{\infty}$ and $A = \{\alpha_n\}_{n=0}^{\infty}$ form a biorthogonal system for a Banach space $\mathcal{E}$, then $(A, j(X))$ is a biorthogonal system for the dual space $\mathcal{E}^*$ (where $j$ denotes,

for $\mathcal{E}$, that is, a pair of similarly indexed families $X = \{x_{\gamma}\}$ and $A = \{\alpha_{\gamma}\}$ in $\mathcal{E}$ and $\mathcal{E}^*$, respectively, satisfying the biorthogonality relation $\alpha_{\gamma'}(x_{\gamma'}) = \delta_{\gamma' \gamma''}$ (the Kronecker delta) for all $\gamma', \gamma''$ in $\Gamma$. (Hint: Let $\mathcal{L}$ denote the linear space consisting of all those families of scalars $\{\alpha_{\gamma}\}$ indexed by $\Gamma$ with the property that the family $\{\alpha_{\gamma} x_{\gamma}\}_{\gamma \in \Gamma}$ is summable in $\mathcal{E}$. Use Problem 4N to show that the sum $\sum_{\gamma \in \Gamma} |\alpha_{\gamma} f(x_{\gamma})|$ is finite for each $f$ in $\mathcal{E}^*$ and $\{\alpha_{\gamma}\}$ in $\mathcal{L}$. Then use this fact to show that

$$\| a \| = \sup_D \left\| \sum_{\gamma \in D} \alpha_{\gamma} x_{\gamma} \right\|,$$

where the indicated supremum is taken over all finite subsets $D$ of $\Gamma$, is a norm on $\mathcal{L}$ turning it into a Banach space; follow the proofs of Proposition 19.7 and Theorem 19.8.

(ii) Let $(X = \{x_{\gamma}\}_{\gamma \in \Gamma}, A = \{\alpha_{\gamma}\}_{\gamma \in \Gamma})$ be an indexed biorthogonal system for a Banach space $\mathcal{E}$, and for each finite subset $D$ of $\Gamma$ set

$$E_D x = \sum_{\gamma \in D} \alpha_{\gamma}(x) x_{\gamma}, \quad x \in \mathcal{E}.$$

Show that $X$ is an indexed basis for $\mathcal{E}$ if and only if $X$ spans $\mathcal{E}$ and the family of expansion operators $\{E_D\}$ is uniformly bounded.

S. Let $\{x_{\gamma}\}_{\gamma \in \Gamma}$

U. Let $\mathcal{E}$ be a Banach space, let $X = \{x_n\}_{n \in \mathbb{N}_0}$ be an indexed basis for $\mathcal{E}$, and let $A = \{\alpha_n\}_{n \in \mathbb{N}_0}$ be the corresponding sequence of coefficient functionals.

(i) Show that $(A, j(X))$ is an indexed biorthogonal system for $\mathcal{E}^*$ (Prob. R), and that the family of expansion operators

$$\tilde{E}_D f = \sum_{n \in D} f(x_n) \alpha_n$$

of this system is uniformly bounded. Conclude that if $f$ and $\varphi$ denote elements of $\mathcal{E}^*$ and $\mathcal{E}^{**}$, respectively, then

$$\sum_n |f(x_n)\varphi(\alpha_n)| < +\infty.$$

(Hint: Recall Problem P.)

(ii) Suppose now, in addition, that $\mathcal{E}^*$ is weakly sequentially complete (see Problem 15R). Show that for each $f$ in $\mathcal{E}^*$ the series

$$\sum_{n=0}^{\infty} f(x_n) \alpha_n$$

is unconditionally convergent to $f$, and conclude that the sequence $A$ is an indexed basis for $\mathcal{E}^*$. (Hint: If $\{N_k\}$ is an arbitrary strictly increasing sequence of nonnegative integers, then the subseries

$$\sum_{k=0}^{\infty} f(x_{N_k}) \alpha_{N_k}$$

is weakly summable by (10). Since $\mathcal{E}^*$ is weakly sequentially complete, it follows that $\sum_{n=0}^{\infty} f(x_n) \alpha_n$ is weakly subseries convergent in $\mathcal{E}^*$. Use the Orlicz–Pettis theorem (Prob. L.).

(iii) (Karlin [39]) Conclude, in summary, that if $\mathcal{E}$ is a separable Banach space that admits an indexed basis, and if $\mathcal{E}^*$ is weakly sequentially complete, then $\mathcal{E}^*$ is also a separable Ban

Let $\{x_\gamma\}$ be such an absolute basis, let $(\ell_1; \Gamma)$ denote the Banach space of all absolutely summable families of scalars indexed by $\Gamma$ (cf. Problem J), and define

$$Tx = \{\alpha_\gamma(x) \| x_\gamma\| \}_{ \gamma \in \Gamma}, \quad x \in \mathcal{E}.$$

Show that $T$ is a linear transformation of $\mathcal{E}$ onto $(\ell_1; \Gamma)$. Show further that $T$ is bounded, and is therefore an equivalence between $\mathcal{E}$ and $(\ell_1; \Gamma)$. Thus, in particular, a separable Banach space admits an absolute basis if and only if it is equivalent to $(\ell_1)$. (Hint: Use the continuity of the coefficient functionals $\alpha_\gamma$ to prove that $T$ is closed.)

1. Banach, S., Théorie des opérations linéaires, Warsaw, 1932.
2. Banach, S. and S. Mazur, Zur Theorie der linearen Dimension, Studia Math., 4 (1933), 100–112.
3. Bary, N. K., Trigonometric series, New York, 1964.
4. Bennett, G. and N. J. Kalton, Consistency theorems for almost convergence, Trans. Amer. Math. Soc., 198 (1974), 23–43.
5. Berberian, S. K., Measure and integration, New York, 1965.
6. Berberian, S. K., The product of two measures, Amer. Math. Monthly, 69 (1962), 961–968.
7. Berberian, S. K., Counterexamples in Haar measure, Amer. Math. Monthly, 73 (1966), 135–140.
8. Berberian, S. K. and J. F. Jakobsen, A note on Borel sets, Amer. Math. Monthly, 70 (1963), 55.
9. Bessaga, C. and A. Pelczynski, On bases and unconditional convergence of series in Banach spaces, Studia Math., 17 (1958), 151–164.
10. Bourbaki, N., Élèments de mathématique: Livre I, Théorie des ensembles, Paris, 1966.
11. Bourbaki, N., Élèments de mathématique: Livre III, Topologie générale, Paris, 1948.
12. Bourbaki, N., Élèments de mathématique: Livre V, Espaces vectoriels topologiques, Paris, 1967.
13. Brown, A., On the adjoint of a closed transformation, Proc. Amer. Math. Soc., 15 (1964), 239–240.
14. de

16. Dieudonné, J., Sur le théorème de Lebesgue–Nikodym (IV), J. Indian Math. Soc., N. S. 15 (1951), 77–86.

17. Dieudonné, J., Sur le théorème de Lebesgue–Nikodym (V), Canad. J. Math., 3 (1951), 129–139.

18. Dinculeanu, N., Vector measures, Berlin, 1966.

19. Dixon, J. D., A brief proof of Cauchy’s integral theorem, Proc. Amer. Math. Soc., 29 (1971), 625–626.

20. Dugundji, J., Topology, Boston, 1966.

21. Dunford, N., Spectral theory I. Convergence to projections, Trans. Amer. Math. Soc., 54 (1943), 185–217.

22. Dunford, N. and B. J. Pettis, Linear operations on summable functions, Trans. Amer. Math. Soc., 47 (1940), 323–392.

23. Dunford, N. and J. Schwartz, Linear operators Part I: General theory, New York, 1958.

24. Dvoretzky, A. and C. A. Rogers, Absolute and unconditional convergence in normed linear spaces, Proc. Nat. Acad. Sci., 36 (1950), 192–197.

25. Enflo, P., A counterexample to the approximation problem in Banach spaces, Acta Math., 130 (1973), 309–317.

26. Federer, H., Geometric measure theory, New York, 1969.

27. Gamelin, T. W., Uniform algebras, Englewood Cliffs, N.J., 1969.

28. Gelfand, I., Normierte Ringe, Mat. Sbornik, (N.S.) 9 (194

45. Luther, N. Y., Unique extension and product measures, Canad. J. Math., 19 (1967), 757–763.

46. Mackey, G. W., On convex topological linear spaces, Trans. Amer. Math. Soc., 60 (1946), 519–537.

47. MacLane, S., Homology, New York, 1975.

48. Mergel’yan, S. N., Uniform approximation to functions of a complex variable, Uspehi Mat. Nauk, 7 vyp. 2 (1952), 31–122 (A.M.S. Transl., Ser. 1., Vol. 3).

49. Mukherjea, A., A remark on Tonelli’s theorem on integration in product spaces, Pac. J. Math., 42 (1972), 177–185.

50. Mukherjea, A., Remark on Tonelli’s theorem on integration in product spaces—II, Ind. U. Math. J., 23 (1974), 679–684.

51. Orlicz, W., Beiträge zur Theorie der Orthogonalentwicklungen II, Studia Math., 1 (1929), 241–255.

52. Pettis, B. J., On integration in vector spaces, Trans. Amer. Math. Soc., 44 (1938), 277–304.

53. Riesz, F., Les systèmes d’équations linéaires à une infinité d’inconnues, Paris, 1913.

54. Riesz, F., Sur l’existence de la dérivée des fonctions monotones et sur quelques problèmes qui s’y rattachent, Acta Szeged, 5 (1930–2), 208–221.

55. Robertson, A. P. and W. Robertson, Topological vector spaces, Cambridge, 1964.

56. Rosenblum, M., On the operator equation $BX - XA =

Index

Abel's theorem 89
absolutely convex neighborhood of 0 295, 296, 321, 323, 334, 362
absolutely convex set 295, 308, 350, 362
absorbing 322, 323, 352, 362
closed 308, 349–351, 354, 356, 362
compact 355, 356, 362
weakly compact 361
absolutely summable family of vectors 431, 441, 443, 448
absorb 350, 351, 362
accumulation point 49, 51, 57, 71, 341
adherent point (of a collection of sets) 53, 54
adjoint 342–345, 361, 374, 446
admissible collection of sets 156, 157, 160
admissible collection of weakly bounded sets 353–356, 361, 363
Alaoglu–Bourbaki theorem 356
Alaoglu's theorem 319, 321, 333, 334, 357
algebra 253, 267, 270, 412
abelian 20
associative linear 19, 28, 111, 207
Banach, see Banach algebra
commutative 20, 133
homological 359
normed, see normed algebra
of polynomials 29, 415
quotient 28, 29
unital 20, 34, 106, 133, 392
analytic continuation 96–98, 33

Banach algebra valued mapping, locally analytic 317
Banach function space 278
Banach–Knaster–Tarski lemma 5
Banach, S. 448
Banach space 216–223, 227, 228, 238, 239, 242, 249, 250, 252, 253, 255–257, 261, 264–267, 270–272, 274, 278–280, 283, 285, 290, 304, 305, 315, 329, 330, 333, 337, 340–346, 354, 357, 363, 368, 370, 371, 374, 378, 386–389, 395, 400, 401, 403–406, 408–411, 423, 425, 429–438, 440–449
finite dimensional 249, 256, 259, 269, 337, 441
irreflexive 338
reflexive 337, 338, 346, 357, 358, 360, 422, 444
separable 257, 270, 332, 333, 338, 376, 379–382, 399–401, 422, 423, 432, 435, 443, 447–449
universal 423
weakly boundedly complete 33

240, 252, 256, 273, 277, 278, 299, 300, 368, 407, 434
Cauchy transform 202, 419
cell 137, 156, 157, 175
closed 35, 104, 110, 245, 325, 326
half-open 103
measurable 186
open 33, 110
center (of an algebra) 20, 404
chained
arcs 73, 92, 99
circle chains 97
collection of sets 37
chain rule 70
characteristic equation 30
circle
chain 96, 97
of convergence 71, 89
closed graph theorem 276–281
closed in the sense of Baire 207, 208
closure 32, 37, 46
cluster point 53
coarser
partition 8
σ-ring 103
topology 41, 238
coefficient
Fourier, see Fourier coefficient
with respect to a basis 432
with respect to an indexed basis 446
coefficient family, with respect to an indexed basis 446
coefficient functional, with respect to an indexed basis 446–449
coefficient sequence, with respect to a basis 432
cofinal (subset of a partially ordered set) 9, 135, 310, 334
commutant 402, 404
compact Hausdorff space 35, 41, 44, 49, 51, 54, 59, 197, 198, 203, 217–219, 238, 254, 356, 362, 406–

dimension (cont.)
of a linear space 14, 21, 26
Dirac mass 122, 198, 328, 336, 411, 424
direct sum
algebraic 323
full algebraic 14, 26, 225, 233, 243, 296, 298, 305, 323, 357
internal 27
of linear spaces 14, 15, 222, 223, 241, 271
of measurable spaces 143
of measures 143, 204, 205
of measure spaces 143, 161, 177, 189, 191, 366
of normed spaces 222, 223, 243, 266, 275, 304
of $\sigma$-rings 143
of topological spaces 204
disc algebra 416, 417
disc of convergence 71
distribution 324–327, 335, 336
infinitely differentiable 327
of order zero 325
regular 326–328, 336
singular 336
Dixon, J. D. 95
domain (in $\mathbb{C}$) 39, 70, 81, 96, 244, 309, 315, 317, 330, 340, 418
exterior 40
interior 40, 98
Jordan 40
simply connected 96, 98, 421, 426
dominate (of norms or quasinorms) 274, 280, 313
dominated convergence theorem 129, 134, 149, 162

91, 94, 105, 150–154, 188, 305, 325, 426
(see also mapping, continuous)
continuously differentiable 17, 34, 244, 274, 277, 278, 300, 327, 335, 371, 423
distribution 160
entire 83, 85, 86, 317, 392, 421
essentially bounded 125, 131, 133, 365, 375
generalized 326
harmonic 87, 88, 96, 98
having limit at infinity 423
Heaviside 328
holomorphic 70, 280 (see also analytic function)
infinitely differentiable 244, 300, 323, 324
integrable 114, 117, 120, 121, 124, 125, 128–135, 141–143, 146, 148, 153, 160, 162, 166, 325, 364, 370, 375
integrable over a period 370, 436
integrable simple 120, 121, 131, 132, 149, 179, 196, 376, 397
left [right] continuous 60, 139, 140, 149, 160, 162, 206, 305, 327, 401, 411, 422
Lipschitzian 163, 239
locally analytic 70

index (cont.)
(see also winding number)
of nilpotence 269
inductive limit 322, 323, 334
infimum 3, 173, 220, 306
essential 126
initial
point 73, 77, 92
value problem 275
integral 113
Cauchy 116
Cauchy–Riemann 137, 138
Darboux 158, 159
double 166, 184, 328
indefinite 168–170, 187–190, 336, 426, 437
iterated 166, 184, 328
Lebesgue, see Lebesgue integral
Lebesgue–Stieltjes 139, 147, 149, 158
line 73–78, 90, 150, 387, 389
product 166, 184
Riemann 116, 159, 385
Riemann–Stieltjes 159, 160, 163, 384–387, 400, 401
with respect to a measure 120, 122, 123, 125, 147
integrand 159, 385
integration by parts 189, 327
integrator 159, 385, 386
interior
domain, see domain, interior
of a set 32, 242, 290, 302
internal point 294, 295, 302
intertwine 402
inverse
element in an algebra 20
left [right] of a bounded linear transformation 254, 255, 360, 424

one-sided 44
ordinal 10, 33, 50, 207
line 13, 331, 416
linear combination 12, 331
linear extension 267, 286–288, 293, 382
linear functional 15, 16, 20, 31, 75, 92, 113–115, 149, 167, 203, 206, 304, 308, 347
bounded 284, 286, 290, 292, 293, 301, 304, 320, 324, 359, 372, 375, 383, 388, 400, 419, 422, 423, 434, 435, 445
continuous 283, 302–304, 308, 310, 324, 341, 353
positive 197, 198, 207, 306, 307, 310, 410, 424
self-conjugate 16, 116, 424
unbounded 249, 334
weak* continuous 331, 340
linearly ordered set 6 (see also simply ordered set)
linear operator, bounded 252
linear parametrization 75, 92
linear space 12–31, 113–116, 124, 134, 178, 191, 207, 318, 348, 364, 365, 377, 378, 406
finite dimensional 14, 27
free 14

measure (cont.)
absolutely continuous 169, 170, 172, 187, 188, 190, 328, 336, 372
accessible 189, 190
arc-length 142, 160, 195, 369, 382, 384, 418
atom-free 140, 181, 191
Baire 208
Borel, see Borel measure
complete 161
complex 144, 145, 147–149, 155, 162, 183, 184, 187, 326, 372, 406
counting 122, 144, 155, 165, 186, 189, 365, 443
defined by an outer measure 156, 157
Dirac, see Dirac mass
finite 118, 131, 145, 146, 169
finitely additive 119
induced 142, 160, 168
Lebesgue, see Lebesgue measure
Lebesgue–Borel 137–139, 142, 144, 165, 167, 168, 178, 181, 186, 188, 191, 205, 245, 303, 328
locally finite 141, 165, 169, 185, 186, 189, 190
outer, see outer measure
$\sigma$-finite 131, 145, 146, 164, 165, 169, 170, 172, 17

weakly Cauchy 333, 443
weak* Cauchy 334
norm 212–223, 228–230, 240, 245, 280, 290, 331, 350, 406, 407, 434, 445, 447
associated with a pseudonorm 230, 290, 365
of a functional with respect to a pseudonorm 290, 292, 307
of a linear transformation 248, 305, 306, 387
quadratic 214
quotient 222
sup 217, 218, 238, 239, 278, 280, 290, 292, 304, 329, 355, 412, 423
total variation 305, 406
normed algebra 253
unital 253
normed (linear) space 212–223, 225, 227, 228, 231, 238, 243, 251–254, 256, 257, 265–267, 279, 280, 283, 300–304, 311, 313, 314, 318, 319, 331–333, 338, 346, 348, 350, 352, 355, 356, 360, 364, 366, 377, 378, 384, 385, 406, 428, 429, 431, 440
associated with a pseud

principal (cont.)
part 85
value (of a two-way infinite series) 428, 439
problem of the existence of a measurable cardinal 189
product
algebraic tensor 12, 22–25, 31
Cartesian (or set-theoretic) 5
inner 286, 375, 439, 440
of linear transformations 19, 253
of measurable spaces 164, 186
of measures 165–167, 184, 186, 187
of topological linear spaces 233
of topological spaces 43, 44, 47, 48, 54, 182, 356
row by column 20, 27
projection 5, 27, 276, 445
natural 16, 18, 29, 222, 230, 232, 239, 249, 251, 290, 341, 345, 346, 358, 359, 371
projective limit 335
pseudometric 56, 64, 117, 124, 229, 313
invariant 229, 230, 245
pseudonorm 229, 230, 233–237, 239, 242–246, 290, 291, 293, 295–302, 305, 306, 311, 313, 318, 321–325, 332, 333, 350, 355, 364, 365, 377, 378, 397, 422, 434

ultimately periodic 306, 307
weakly convergent 314, 315, 321, 329, 422, 444
weak* convergent 422
weight 250, 251, 262, 268–270
series
absolutely convergent 239, 257, 262, 330
convergent 239, 428, 431, 433
convergent in the Cauchy sense 428, 429, 445
convergent in the primary sense 428, 429, 445
convergent in the secondary sense 428
Fourier, see Fourier series
subseries convergent 442
two-way infinite 428, 429, 437
unconditionally convergent 442, 447, 448
weakly convergent 444, 446
weakly subseries convergent 444, 445, 448
expansion with respect to a biorthogonal system 435, 436
Taylor, see Taylor series
sesquilinear functional 22, 375, 440
symmetric 22
set
absolutely convex, see absolutely convex set
absorbing 295, 321–323, 334, 350–352, 356
Borel 104, 105, 110, 111, 116, 137–139, 142, 144, 149, 155, 157, 158, 164–168, 175, 178, 182, 186, 193–196, 206, 326, 369, 407,

$\sigma$-ring (cont.)
of Lebesgue measurable sets 136, 137, 157, 174, 370

similar
bounded operators 269, 270
elements of a Banach algebra 269
matrices 22, 30

simple polygon 76, 79, 97

simply ordered set 6, 309, 332

singular measures 173, 187

Smul'yan criterion 346, 357, 358, 360

Sobolev space 371

space (see also under appropriate name)
Euclidean 62, 213, 368
pseudometric 57

quotient (modulo a linear manifold) 16, 124, 221, 222, 228, 232 (see also quotient space of a normed space)

quotient (modulo an equivalence relation) 51, 65

uniform 241

unitary 62, 213

vector 12, 31, 125 (see also linear space)

spanning set in a normed space 220, 221, 240, 309, 333, 398, 422, 437, 438, 444, 447

spectral radius
of an operator 269
with respect to a Banach algebra 269, 331

spectrum
left [right] of a bounded operator 259
left [right] with respect to a Banach algebra 260, 268
of a bounded operator 258–260, 344, 395, 399
with respect to a Banach algebra 260, 261, 263, 264, 317, 330, 389, 394, 402

sphere

Tietze extension theorem 218, 238, 239, 423
Tihonov, A. 49
Tihonov plank 54
Tihonov's theorem 44, 320
Tonelli theorem 166, 183, 185, 186, 367
topological embedding 49, 59, 334
topological linear space 230–234, 241, 242, 245, 249, 270, 283, 292, 295, 302, 303, 308, 313, 346
associated 233
finite dimensional 242, 323, 346, 360
locally convex, see locally convex space
metrizable 247, 297, 298, 300, 332
normable 331, 350
quasinormable 237, 247, 297
separable 241
separated 231–233, 235, 242, 247, 270, 302
topological space 32, 37, 41–44, 46–54, 56, 67, 69, 104, 105, 107, 110, 164, 193, 207, 238, 239
arcwise connected 38
compact 34, 50, 53, 59, 272, 320, 414
compact Hausdorff, see compact Hausdorff space
completely regular 36, 49, 54
connected 36–38
countably compact 34, 50, 53, 54

value 211, 213, 223, 224, 240
variation (see also function of bounded variation)
over a partition 7
positive and negative 8, 146, 162, 202
total 7, 60, 148, 160, 162, 184, 204, 289, 290, 305, 387, 406
vertex 93
vector space, see linear space
topological, see topological linear space
Vituškin, A. G. 422

weakly summable family of vectors 443, 444, 448
with sum 443, 444
weak* summable family of functionals 443
with sum 443

Weierstrass approximation theorem 111, 112, 371, 415, 425
weight (of a topological space) 49, 231, 331
well ordered set 6
well ordering principle 6
winding number 78–80, 92, 93, 101, 388, 391

Zermelo’s theorem 6
zero
class 425
of an analytic function 86
space 229, 230, 233, 235, 246, 290, 305, 365, 378, 422
Zorn’s lemma 5, 10, 25, 190, 287, 309

References to the examples, propositions, and problems

Ex.1A 8 Prop.2.2 24, 25, 31
Ex.1B 33, 45 Prop.2.3 25
Ex.1C 10 Prob.2A 13, 31, 249
Prob.1A 9, 10 Prop.2B 14
Prob.1C 6, 9 Prop.2C 26, 279
Prob.1D 74, 106, 116, 197, 413, 414 Prop.2D 30, 348
Prob.1F 69, 174, 175 Prop.2E 23, 31, 249
Prob.1G 8, 60, 154, 158, 385 Prop.2F 14
Prob.1H 158 Prop.2G 20, 28, 259, 338
Prob.1I 52, 60, 74, 147, 149, 154, 206, 289, 327, 387 Prop.2H 20, 29, 106, 265, 283, 343
Prob.1J 8, 147, 162 Prob.2L 20, 21, 29, 393, 401
Prob.1K 60, 146, 147, 154, 162 Prob.2M 20, 21
Prob.1L 106, 108, 179, 181, 381 Prob.20 259
Prob.1M 45 Prob.2P 269, 403
Prob.1P 11, 49, 135, 237, 243, 310

References (examples, propositions, problems)

Prop.3.4 35, 49, 50, 51, 54 Ex.5A 72, 73, 83, 268, 330
Prop.3.5 35, 54, 59, 63, 204, 218 Ex.5B 78
Prop.3.6 38, 39, 73 Ex.5C 91
Prop.3.7 38, 150, 157 Ex.5D 78, 392
Prop.3.8 99 Ex.5F 95
Prop.3.9 70 Ex.5I 94, 316
Th.3.11 76 Ex.5J 72, 84, 413
Prop.3.12 40, 93 Ex.5K 86, 95, 317
Prob.3.14 35, 51 Ex.5L 95
Th.3.15 35, 49, 54, 320, 356 Ex.5M 281, 417
Prop.3.17 46, 52 Th.5.1 86, 393
Prop.3.18 46, 47, 48, 51 Th.5.2 96, 341, 420
Cor.3.19 48, 215, 361 Prop.5.3 76, 90
Prop.3.20 48, 234, 235, 320 Th.5.4 77, 80, 85
Prop.3A 32, 231, 240, 331 Prop.5.5 80, 91
Prop.3B 51, 68, 71 Th.5.7 80, 83,

References (examples, propositions, problems)

Ex.7A 122 Th.8.6 162
Ex.7B 122 Prop.8.7 148, 162
Ex.7C 122 Prop.8.8 202
Ex.7D 115, 122, 217 Prop.8.9 151, 152
Ex.7E 123 Th.8.12 154, 155
Ex.7G 130 Th.8.13 154, 155, 163
Ex.7H 132, 136, 140 Prop.8.14 155
Ex.7I 136, 140, 198, 328, 424 Prob.8A 155, 157, 163, 168, 178, 183, 184, 326
Ex.7J 133, 136, 144, 165, 365, 443
Ex.7L 143 Prob.8C 153, 157, 161, 200
Ex.7M 143, 148 Prob.8D 160, 185, 199
Ex.7N 134, 191, 204 Prob.8E 136, 137, 153, 157
Prop.7.1 117, 127, 130, 132, 197 Prob.8F 136, 137, 138, 143, 369, 384
Prop.7.2 124, 127, 129, 130, 132, 133 Prob.8H 137, 138, 161,

References (examples, propositions, problems)

Prob.9X 181
Prob.9Y 192
Ex.10A 244, 300, 325
Ex.10C 204, 205, 411
Ex.10E 251, 411, 422
Ex.10F 419
Prop.10.1 195
Prop.10.3 204
Cor.10.6 202, 408
Prop.10.7 204, 205, 399
Prop.10.8 200, 204, 205
Th.10.9 198, 207, 410
