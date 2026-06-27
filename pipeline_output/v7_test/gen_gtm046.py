#!/usr/bin/env python3
"""Generate v7 concept files for GTM046 Probability Theory II by Loève."""
import os, yaml, hashlib

BASE = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM046__Probability_Theory_II__I_M__Lo_ve"
BOOK_ID = "GTM046"
AUTHOR = "Michel Loève"
TITLE = "Probability Theory II"
DATE = "2026-06-24"
AGENT = "v7-10books"

concepts = [
    # === Ch VIII: Conditioning ===
    {
        "slug": "conditional-expectation-given-sigma-field",
        "title_en": "Conditional Expectation Given a σ-field",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "27.2",
        "desc": "The conditional expectation E^ℬ X of a random variable X given a sub-σ-field ℬ is defined as the Radon-Nikodym derivative of the indefinite integral of X with respect to the restriction of P to ℬ. It is a ℬ-measurable function unique up to P_ℬ-equivalence satisfying ∫_B E^ℬ X dP = ∫_B X dP for all B ∈ ℬ.",
        "latex": r"""\begin{definition}[Conditional Expectation]
Let $(\Omega, \mathcal{A}, P)$ be a probability space and $\mathcal{B} \subset \mathcal{A}$ a sub-$\sigma$-field.
For a random variable $X$ whose expectation exists (i.e., $EX^+ < \infty$ or $EX^- < \infty$),
the \emph{conditional expectation of $X$ given $\mathcal{B}$}, denoted $E^{\mathcal{B}}X$, is the
$\mathcal{B}$-measurable function defined up to $P_{\mathcal{B}}$-equivalence such that
\[
\int_B E^{\mathcal{B}}X \, dP = \int_B X \, dP \quad \text{for every } B \in \mathcal{B}.
\]
It exists and is unique up to $P_{\mathcal{B}}$-equivalence.
\end{definition}"""
    },
    {
        "slug": "conditional-probability-given-sigma-field",
        "title_en": "Conditional Probability Given a σ-field",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "27.2",
        "desc": "The conditional probability P^ℬ A of an event A given a sub-σ-field ℬ is defined as E^ℬ I_A, the conditional expectation of its indicator. It satisfies P^ℬ Ω = 1 a.s., P^ℬ ∅ = 0 a.s., and is countably additive almost surely.",
        "latex": r"""\begin{definition}[Conditional Probability]
Let $(\Omega, \mathcal{A}, P)$ be a probability space and $\mathcal{B} \subset \mathcal{A}$ a sub-$\sigma$-field.
For any event $A \in \mathcal{A}$, the \emph{conditional probability of $A$ given $\mathcal{B}$} is
\[
P^{\mathcal{B}}A = E^{\mathcal{B}} I_A,
\]
where $I_A$ is the indicator of $A$. It satisfies almost surely:
\[
P^{\mathcal{B}}\Omega = 1, \quad P^{\mathcal{B}}\emptyset = 0, \quad P^{\mathcal{B}}A \geq 0,
\]
and $P^{\mathcal{B}}\left(\sum_{k=1}^{\infty} A_k\right) = \sum_{k=1}^{\infty} P^{\mathcal{B}}A_k$ a.s.
\end{definition}"""
    },
    {
        "slug": "conditional-expectation-is-linear-operation",
        "title_en": "Conditional Expectation is an Almost-Surely Linear Operation",
        "type": "proposition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.1",
        "desc": "The conditional expectation E^ℬ is an almost-surely linear operation: E^ℬ(cX + c'X') = c E^ℬ X + c' E^ℬ X' a.s. In particular, E^ℬ(∑ x_k I_{A_k}) = ∑ x_k P^ℬ A_k a.s.",
        "latex": r"""\begin{proposition}[Linearity of Conditional Expectation]
The conditional expectation $E^{\mathcal{B}}$ is an almost-surely linear operation:
\[
E^{\mathcal{B}}(cX + c'X') = cE^{\mathcal{B}}X + c'E^{\mathcal{B}}X' \quad \text{a.s.}
\]
In particular,
\[
E^{\mathcal{B}}\left(\sum_{k=1}^{n} x_k I_{A_k}\right) = \sum_{k=1}^{n} x_k P^{\mathcal{B}}A_k \quad \text{a.s.}
\]
\end{proposition}"""
    },
    {
        "slug": "conditional-inequalities-holder-minkowski",
        "title_en": "Conditional Hölder and Minkowski Inequalities",
        "type": "proposition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.1",
        "desc": "The c_r-, Minkowski, and Hölder inequalities, as well as their consequences and inequalities for convex functions, remain valid almost surely when expectations are replaced by conditional expectations.",
        "latex": r"""\begin{proposition}[Conditional Inequalities]
Upon replacing $E$ by $E^{\mathcal{B}}$, the $c_r$-, Minkowski, and H\"older inequalities,
as well as their consequences and the inequalities for convex functions, remain valid almost surely.
In particular, for $p, q > 1$ with $1/p + 1/q = 1$:
\[
E^{\mathcal{B}}|XY| \leq \left(E^{\mathcal{B}}|X|^p\right)^{1/p} \left(E^{\mathcal{B}}|Y|^q\right)^{1/q} \quad \text{a.s.}
\]
\end{proposition}"""
    },
    {
        "slug": "monotone-convergence-for-conditional-expectations",
        "title_en": "Monotone Convergence Theorem for Conditional Expectations",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.1",
        "desc": "If 0 ≤ X_n ↑ X a.s., then 0 ≤ E^ℬ X_n ↑ E^ℬ X a.s. In particular, P^ℬ(∑ A_k) = ∑ P^ℬ A_k a.s.",
        "latex": r"""\begin{theorem}[Monotone Convergence for Conditional Expectations]
If $0 \leq X_n \uparrow X$ a.s., then $0 \leq E^{\mathcal{B}}X_n \uparrow E^{\mathcal{B}}X$ a.s.
In particular, for any sequence of events $\{A_k\}$,
\[
P^{\mathcal{B}}\left(\sum_{k=1}^{\infty} A_k\right) = \sum_{k=1}^{\infty} P^{\mathcal{B}}A_k \quad \text{a.s.}
\]
\end{theorem}"""
    },
    {
        "slug": "fatou-lebesgue-convergence-for-conditional-expectations",
        "title_en": "Fatou-Lebesgue Convergence for Conditional Expectations",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.1",
        "desc": "The Fatou-Lebesgue convergence theorem extends to conditional expectations: under integrable domination, the conditional expectation of the limit inferior/superior is bounded by the limit inferior/superior of the conditional expectations.",
        "latex": r"""\begin{theorem}[Fatou-Lebesgue for Conditional Expectations]
Let $Y$ and $Z$ be integrable random variables. If $Y \leq X_n$ a.s. or $X_n \leq Z$ a.s., then
\[
E^{\mathcal{B}}(\liminf X_n) \leq \liminf E^{\mathcal{B}}X_n \leq \limsup E^{\mathcal{B}}X_n \leq E^{\mathcal{B}}(\limsup X_n) \quad \text{a.s.}
\]
\end{theorem}"""
    },
    {
        "slug": "smoothing-on-atoms-of-sigma-field",
        "title_en": "Smoothing Property on Atoms of a σ-field",
        "type": "proposition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.2",
        "desc": "On every nonnull atom B of ℬ, E^ℬ X is constant with value (1/PB) ∫_B X dP -- the average of X on B with respect to P. Thus E^ℬ X is a ℬ-smoothed version of X.",
        "latex": r"""\begin{proposition}[Smoothing on Atoms]
On every nonnull atom $B \in \mathcal{B}$ (i.e., $PB > 0$ and $B$ contains no proper nonempty $\mathcal{B}$-sets),
$E^{\mathcal{B}}X$ is constant and
\[
E_B X = \frac{1}{PB} \int_B X \, dP.
\]
If $\mathcal{B}$ is the minimal $\sigma$-field over a countable partition $\{B_j\}$, then
\[
E^{\mathcal{B}}X = \sum_j (E_{B_j}X) I_{B_j} \quad \text{a.s.}
\]
\end{proposition}"""
    },
    {
        "slug": "basic-smoothing-property",
        "title_en": "Basic Smoothing Property of Conditional Expectations",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.2",
        "desc": "If ℬ ⊂ ℬ' and X' is ℬ'-measurable, then E^ℬ(XX') = E^ℬ(X' E^{ℬ'} X). This generalizes the tower property and the commutation of conditional expectation with measurable factors.",
        "latex": r"""\begin{theorem}[Basic Smoothing Property]
If $\mathcal{B} \subset \mathcal{B}'$ and $X'$ is $\mathcal{B}'$-measurable, then
\[
E^{\mathcal{B}}(XX') = E^{\mathcal{B}}(X' E^{\mathcal{B}'}X).
\]
In particular, denoting by $E^{X',Y}$ the conditional expectation given $\mathcal{B}_{X',Y}$,
\[
E^{Y}(XX') = E^{Y}(X' E^{X',Y}X) \quad \text{a.s.}
\]
\end{theorem}"""
    },
    {
        "slug": "conditional-independence-of-sigma-fields",
        "title_en": "Conditional Independence of σ-fields",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.3",
        "desc": "Sub-σ-fields ℬ₁ and ℬ₂ are conditionally independent given ℬ if P^ℬ(B₁B₂) = P^ℬ B₁ · P^ℬ B₂ a.s. for all B₁ ∈ ℬ₁, B₂ ∈ ℬ₂. This generalizes independence (which is conditional independence given the trivial σ-field).",
        "latex": r"""\begin{definition}[Conditional Independence]
Let $\mathcal{B}, \mathcal{B}_1, \mathcal{B}_2$ be sub-$\sigma$-fields of $\mathcal{A}$.
$\mathcal{B}_1$ and $\mathcal{B}_2$ are \emph{conditionally independent} given $\mathcal{B}$ if, for every
$B_1 \in \mathcal{B}_1$ and $B_2 \in \mathcal{B}_2$,
\[
P^{\mathcal{B}}(B_1 B_2) = P^{\mathcal{B}}B_1 \cdot P^{\mathcal{B}}B_2 \quad \text{a.s.}
\]
If $\mathcal{B} = \mathcal{B}_0 = \{\emptyset, \Omega\}$, this reduces to ordinary independence.
\end{definition}"""
    },
    {
        "slug": "chain-of-sigma-fields",
        "title_en": "Chain of σ-fields (Chain Dependence)",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.3",
        "desc": "A sequence ℬ_n of sub-σ-fields is chained (or chain-dependent) if P^{ℬ_1⋯ℬ_n} B_{n+1}⋯B_{n+m} = P^{ℬ_n} B_{n+1}⋯B_{n+m} a.s. The future depends on the past only through the present.",
        "latex": r"""\begin{definition}[Chain of $\sigma$-fields]
A sequence $\{\mathcal{B}_n\}$ of sub-$\sigma$-fields of events is said to form a \emph{chain},
or to be \emph{chain-dependent}, if for every $n, m \geq 1$ and $B_{n+1}, \ldots, B_{n+m}$
with $B_k \in \mathcal{B}_k$,
\[
P^{\mathcal{B}_1 \cdots \mathcal{B}_n}(B_{n+1} \cdots B_{n+m}) = P^{\mathcal{B}_n}(B_{n+1} \cdots B_{n+m}) \quad \text{a.s.}
\]
\end{definition}"""
    },
    {
        "slug": "regular-conditional-probability",
        "title_en": "Regular Conditional Probability",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "29.1",
        "desc": "A conditional probability P^ℬ A is regular if, up to a null set in ω, it is a probability measure in A for every fixed ω. This allows conditional expectations to be genuine integrals with respect to a random measure.",
        "latex": r"""\begin{definition}[Regular Conditional Probability]
A conditional probability $P^{\mathcal{B}}A$ is \emph{regular} if there exists a function
$Q(\omega, A)$, $\mathcal{B}$-measurable in $\omega$ for fixed $A$ and a probability measure
in $A$ for fixed $\omega$, such that for every $A \in \mathcal{A}$,
\[
Q(\omega, A) = P^{\mathcal{B}}A(\omega) \quad \text{up to a } P_{\mathcal{B}}\text{-equivalence}.
\]
Then $E^{\mathcal{B}}X(\omega) = \int X(\omega') Q(\omega, d\omega')$ a.s.
\end{definition}"""
    },
    {
        "slug": "regularity-theorem-for-sample-spaces",
        "title_en": "Regularity Theorem for Conditional Probabilities on Sample Spaces",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "29.2",
        "desc": "Conditional probabilities in sample probability spaces of countable families of random variables can be regularized, and conditional distributions of their subfamilies always exist.",
        "latex": r"""\begin{theorem}[Regularity Theorem]
Conditional probabilities in sample probability spaces of countable families of random
variables can be regularized, and conditional distributions of their subfamilies always exist.
\end{theorem}"""
    },
    {
        "slug": "conditional-distribution",
        "title_en": "Conditional Distribution",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "30.1",
        "desc": "A conditional distribution (c.d.) of a random variable X given a σ-field ℬ is a regular conditional probability on the range space of X. Properties (CD₁) and (CD₂) characterize c.d.'s.",
        "latex": r"""\begin{definition}[Conditional Distribution]
A \emph{conditional distribution} (c.d.) of a random variable $X_2$ given $X_1$ is characterized by:
\begin{itemize}
\item[(CD$_1$)] $P(x_1, S_2)$ is an $\mathcal{A}_1$-measurable probability on $\mathcal{A}_2$,
\item[(CD$_2$)] $P(S_1 \times S_2) = \int_{S_1} P(dx_1) P(x_1, S_2)$.
\end{itemize}
\end{definition}"""
    },
    {
        "slug": "minimal-sufficient-sigma-field",
        "title_en": "Minimal Sufficient σ-field",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "27.4",
        "desc": "For a family of probability measures {μ_t} dominated by μ, there exists a minimal sufficient σ-field. The minimality criterion: write Z_t = g_t Z_0 a.s. with Z_0 such that Z_t = 0 a.s. for all t implies Z_0 = 0 a.s.",
        "latex": r"""\begin{theorem}[Minimal Sufficiency Criterion]
For a dominated family $\{\mu_t\}$, there exists $Z_0$ such that:
\begin{enumerate}
\item $\mu_0 A = 0 \iff \mu_t A = 0$ for every $t$;
\item Every sufficient $\sigma$-field with any $Z$ is also sufficient with $Z_0$,
  so the least fine sufficient $\sigma$-field with $Z_0$ is minimal.
\end{enumerate}
The corresponding factorization $Z_t = g_t Z_0$ a.s. satisfies
$Z_0 = 0$ a.s. $\iff$ every $Z_t = 0$ a.s.
\end{theorem}"""
    },
    {
        "slug": "constant-markov-chain",
        "title_en": "Constant Markov Chain",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "markov-chains",
        "chapter": "VIII", "section": "30.3",
        "desc": "A Markov chain is constant (time-homogeneous) if the transition probability P^{n,n+1}(x; S) = P(x; S) is independent of n. The n-step transition probability P^n(x; S) satisfies the Chapman-Kolmogorov equation.",
        "latex": r"""\begin{definition}[Constant Markov Chain]
If the one-step transition probability $P^{n,n+1}(x; S) = P(x; S)$ is independent of $n$,
the chain is \emph{constant} (time-homogeneous). The $n$-step transition probability is
\[
P^n(x; S) = \int P(x; dx_1) \int P(x_1; dx_2) \cdots \int P(x_{n-2}; dx_{n-1}) P(x_{n-1}; S),
\]
satisfying the Chapman-Kolmogorov equation
\[
P^{n+p}(x; S) = \int P^n(x; dx') P^p(x'; S), \quad n, p = 1, 2, \ldots
\]
\end{definition}"""
    },
    {
        "slug": "invariant-distribution-for-transition-probability",
        "title_en": "Invariant Distribution for a Transition Probability",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "markov-chains",
        "chapter": "VIII", "section": "30.3",
        "desc": "A probability distribution P₁ is invariant under the transition probability P(x; S) if P₁(S) = ∫ P₁(dx) P^n(x; S) for all n. A chain with invariant initial distribution is stationary.",
        "latex": r"""\begin{definition}[Invariant Distribution]
A distribution $P_1(S)$ is \emph{invariant} under the transition probability $P(x; S)$ if, for every $n$,
\[
P_1(S) = \int P_1(dx) P^n(x; S).
\]
It suffices that this holds for $n = 1$. A chain whose law is determined by an invariant
distribution and $P(x; S)$ is said to be \emph{stationary}.
\end{definition}"""
    },
    {
        "slug": "markov-measure-of-chain-dependence",
        "title_en": "Markov Measure of Chain Dependence",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "markov-chains",
        "chapter": "VIII", "section": "30.3",
        "desc": "The generalized Markov measure Δ_n = sup_{x,y} sup_S {P^n(x, S) - P^n(y, S)} quantifies chain dependence. It satisfies 0 ≤ Δ_n ≤ 1, with Δ_n = 0 for independence and Δ_n = 1 for determinism.",
        "latex": r"""\begin{definition}[Markov Measure of Dependence]
Let $\Delta_{n,n+m} = \sup_{x,y} \sup_{S} |P^n(x, S) - P^{n+m}(y, S)|$.
The \emph{Markov measure} is $\Delta_n = \Delta_{n,n}$. It satisfies:
\[
0 \leq \Delta_n \leq 1,
\]
with $\Delta_n = 0$ in the independence case and $\Delta_n = 1$ in the deterministic case.
\end{definition}"""
    },
    {
        "slug": "basic-inequalities-for-markov-measure",
        "title_en": "Basic Inequalities for the Markov Measure",
        "type": "proposition",
        "domain": "probability-theory",
        "subdomain": "markov-chains",
        "chapter": "VIII", "section": "30.3",
        "desc": "The Markov measure satisfies Δ_{n,n+m} ≤ Δ_n and the submultiplicative inequality Δ_{n+m} ≤ Δ_n Δ_m. These imply exponential convergence bounds under contraction conditions.",
        "latex": r"""\begin{proposition}[Basic Inequalities for Markov Measure]
For the generalized Markov measure:
\[
\Delta_{n,n+m} \leq \Delta_n \quad \text{and} \quad \Delta_{n+m} \leq \Delta_n \Delta_m.
\]
Consequently, if $\Delta_h < 1$ for some $h$, then
\[
|P^n(x, S) - \bar{P}(S)| \leq \Delta_h^{[n/h]},
\]
so exponential convergence holds.
\end{proposition}"""
    },
    # === Ch IX: From Independence to Dependence ===
    {
        "slug": "weighted-probability-law",
        "title_en": "Weighted Probability Law",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "limit-theorems",
        "chapter": "IX", "section": "31.3",
        "desc": "A weighted probability law over a family of laws {f_α} with weight W is f_W(u) = ∫ f_α(u) dW(α). Weighted normal, Poisson, and infinitely decomposable laws generalize their classical counterparts.",
        "latex": r"""\begin{definition}[Weighted Probability Law]
A \emph{weighted probability law} over a family $\{f_\alpha\}$ with weight distribution $W$ is
\[
f_W(u) = \int f_\alpha(u) \, dW(\alpha).
\]
Examples:
\begin{itemize}
\item Weighted normal: $f_W(u) = \int \exp[iu\alpha - \sigma^2 u^2/2] \, dW(\alpha, \sigma^2)$
\item Weighted Poisson: $f_W(u) = \int_0^\infty \exp[\lambda(e^{iu} - 1)] \, dW(\lambda)$
\item Weighted symmetric stable: $f_W(u) = \int_0^\infty \exp[-c|u|^\gamma/2] \, dW(c)$, $0 < \gamma \leq 2$
\end{itemize}
\end{definition}"""
    },
    {
        "slug": "weighted-symmetric-stable-law-uniqueness",
        "title_en": "Uniqueness of Weighted Symmetric Stable Laws",
        "type": "proposition",
        "domain": "probability-theory",
        "subdomain": "limit-theorems",
        "chapter": "IX", "section": "31.3",
        "desc": "There is a one-to-one correspondence between a weighted symmetric stable law and its weight d.f. defined up to additive constants. A weighted symmetric stable reduces to a symmetric stable iff the weight is degenerate.",
        "latex": r"""\begin{proposition}[Uniqueness of Weighted Symmetric Stable]
For weighted symmetric stable laws with exponent $0 < \gamma \leq 2$:
\begin{enumerate}
\item There is a one-to-one correspondence between $f_W$ and the weight d.f. $W$
      up to additive constants.
\item $f_W$ reduces to a symmetric stable law iff $W$ is degenerate.
\item If $f_{W_n} \to g$, then $g$ is weighted symmetric stable with the same exponent.
\end{enumerate}
\end{proposition}"""
    },
    {
        "slug": "extended-liapounov-theorem",
        "title_en": "Extended Liapounov Theorem (Dependent Case)",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "limit-theorems",
        "chapter": "IX", "section": "31.3",
        "desc": "For summands X_{nk} centered at conditional expectations, if ∑ E|X_{nk}|^{2+δ} → 0 for some δ > 0, then the law of the sum is asymptotically equivalent to a weighted symmetric normal law.",
        "latex": r"""\begin{theorem}[Extended Liapounov Theorem]
Let the $X_{nk}$ be centered at their conditional expectations. If
\[
\sum_k E|X_{nk}|^{2+\delta} \to 0
\]
for some $\delta > 0$, then
\[
\mathcal{L}\left(\sum_k X_{nk}\right) \sim \mathcal{L}\left(\sum_k Y_{nk}\right)
\]
where the $Y_{nk}$ are conditionally normal $\mathcal{N}(0, \sigma'^2_{nk})$.
\end{theorem}"""
    },
    {
        "slug": "conditional-median",
        "title_en": "Conditional Median",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "IX", "section": "32.1",
        "desc": "A conditional median μ^ℬ X of X given ℬ satisfies P^ℬ[X - μ^ℬ X ≥ 0] ≥ 1/2 ≤ P^ℬ[X - μ^ℬ X ≤ 0] a.s. This extends the concept of median to the conditional setting.",
        "latex": r"""\begin{definition}[Conditional Median]
A random variable $\mu^{\mathcal{B}}X$ is a \emph{conditional median} of $X$ given $\mathcal{B}$ if
\[
P^{\mathcal{B}}[X - \mu^{\mathcal{B}}X \geq 0] \geq \frac{1}{2}
\leq P^{\mathcal{B}}[X - \mu^{\mathcal{B}}X \leq 0] \quad \text{a.s.}
\]
\end{definition}"""
    },
    {
        "slug": "extended-levy-inequality",
        "title_en": "Extended P. Lévy Inequality",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.1",
        "desc": "For sums S_k centered at conditional medians, P[max_{k≤n} |S_k| ≥ ε] ≤ 2 P[|S_n| ≥ ε]. This extends Lévy's inequality from the independent to the dependent case.",
        "latex": r"""\begin{theorem}[Extended P.\ L\'evy Inequality]
If the sums $S_k$ are centered at conditional medians $\mu(S_k - S_n \mid S_1, \ldots, S_k)$, then
\[
P\left[\max_{k \leq n} |S_k| \geq \epsilon\right] \leq 2 P[|S_n| \geq \epsilon].
\]
\end{theorem}"""
    },
    {
        "slug": "martingale-sequence",
        "title_en": "Martingale Sequence",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.2",
        "desc": "A sequence X_n of integrable random variables is a martingale with respect to σ-fields ℬ_n if E^{ℬ_n} X_{n+1} = X_n a.s. A submartingale replaces equality with ≥ and a supermartingale with ≤.",
        "latex": r"""\begin{definition}[Martingale]
Let $\{\mathcal{B}_n\}$ be an increasing sequence of sub-$\sigma$-fields and $\{X_n\}$ integrable
random variables adapted to $\{\mathcal{B}_n\}$.
\begin{itemize}
\item $\{X_n\}$ is a \emph{martingale} if $E^{\mathcal{B}_n}X_{n+1} = X_n$ a.s.
\item $\{X_n\}$ is a \emph{submartingale} if $E^{\mathcal{B}_n}X_{n+1} \geq X_n$ a.s.
\item $\{X_n\}$ is a \emph{supermartingale} if $E^{\mathcal{B}_n}X_{n+1} \leq X_n$ a.s.
\end{itemize}
\end{definition}"""
    },
    {
        "slug": "submartingale-convergence-theorem",
        "title_en": "Submartingale Convergence Theorem",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.3",
        "desc": "For a submartingale sequence, if sup E|X_n| < ∞ then X_n converges almost surely to a finite limit. For martingales, convergence follows from sup EX_n^+ < ∞. Reversed submartingales also converge a.s.",
        "latex": r"""\begin{theorem}[Submartingale Convergence]
For a submartingale sequence $\{X_n\}$:
\begin{itemize}
\item If $\sup E|X_n| < \infty$, then $X_n \xrightarrow{a.s.} X$ finite.
\item If $\lim EX_n^+ < \infty$, then $X_n \xrightarrow{a.s.} X < \infty$.
\end{itemize}
For a martingale sequence, $\lim EX_n^+ < \infty$ or $\lim EX_n^- < \infty$
implies $X_n \xrightarrow{a.s.} X < +\infty$ or $> -\infty$ respectively.
\end{theorem}"""
    },
    {
        "slug": "submartingale-closure-theorem",
        "title_en": "Submartingale Closure Theorem",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.3",
        "desc": "Let r ≥ 1. For a (sub)martingale: (i) If Y ∈ L_r closes it on the right, then X_n →^r X. If sup E|X_n|^r < ∞ with r > 1, such Y exists. (ii) If X_n →^r X, then X_n →^{a.s.} X and X is the nearest closing r.v.",
        "latex": r"""\begin{theorem}[Submartingale Closure Theorem]
Let $r \geq 1$.
\begin{enumerate}
\item[(i)] Let $\{X_n\}$ be a martingale or nonnegative submartingale sequence or reversed sequence.
  If $Y \in L_r$ closes it on the right, then $X_n \xrightarrow{r} X$.
  If $\sup E|X_n|^r < \infty$ with $r > 1$, such $Y$ exists.
\item[(ii)] Let $\{X_n\}$ be a (sub)martingale sequence or reversed sequence.
  If $X_n \xrightarrow{r} X$, then $X_n \xrightarrow{a.s.} X$ and $X$ closes the (sub)martingale;
  $X$ is the nearest of the closing random variables.
\end{enumerate}
\end{theorem}"""
    },
    {
        "slug": "zero-one-laws-for-martingales",
        "title_en": "Zero-One Laws for Martingales",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.4",
        "desc": "If EY < ∞, then E(Y | Y_1, ..., Y_n) →^{a.s.} Z < ∞. If E|Y|^r < ∞ (r ≥ 1), then Z = E(Y | Y_1, Y_2, ...), which reduces to Y when Y is defined on the Y_n. This generalizes the zero-one laws of independent sequences.",
        "latex": r"""\begin{theorem}[Zero-One Laws for Martingales]
Let $Y, Y_1, Y_2, \ldots$ be random variables.
\begin{enumerate}
\item If $EY < \infty$, then $E(Y \mid Y_1, \ldots, Y_n) \xrightarrow{a.s.} Z < \infty$.
\item If $E|Y|^r < \infty$ for some $r \geq 1$, then
  $E(Y \mid Y_1, \ldots, Y_n) \xrightarrow{a.s.} E(Y \mid Y_1, Y_2, \ldots)$,
  which reduces a.s.\ to $Y$ when $Y$ is defined on the $Y_n$.
\end{enumerate}
\end{theorem}"""
    },
    {
        "slug": "extended-kolmogorov-inequality",
        "title_en": "Extended Kolmogorov Inequality for Martingales",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.4",
        "desc": "For a martingale sequence X_n = ∑ Y_k, the inequality P[sup_{k≤n} |X_k| > c] ≤ E|X_n|^r / c^r holds for r ≥ 1. For r = 2, this reduces to the classical Kolmogorov inequality.",
        "latex": r"""\begin{theorem}[Extended Kolmogorov Inequality]
Let $X_n = \sum_{k=1}^{n} Y_k$ form a martingale sequence. Then for $r \geq 1$,
\[
P\left[\sup_{k \leq n} |X_k| > c\right] \leq \frac{E|X_n|^r}{c^r}.
\]
For $r = 2$, the summands are orthogonal and this reduces to the classical Kolmogorov inequality.
\end{theorem}"""
    },
    {
        "slug": "marcinkiewicz-theorem-for-independent-sums",
        "title_en": "Marcinkiewicz Theorem for Independent Sums",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "limit-theorems",
        "chapter": "IX", "section": "32.4",
        "desc": "For consecutive sums X_n of independent r.v.'s centered at expectations: X_n →^{a.s.} X ∈ L_r iff X_n →^r X (r ≥ 1). This connects almost-sure and L_r convergence for independent summands.",
        "latex": r"""\begin{theorem}[Marcinkiewicz]
Let $X_n = \sum_{k=1}^{n} Y_k$ be consecutive sums of independent random variables centered
at expectations, and let $r \geq 1$. Then
\[
X_n \xrightarrow{a.s.} X \in L_r \quad \text{if and only if} \quad X_n \xrightarrow{r} X.
\]
\end{theorem}"""
    },
    {
        "slug": "doob-decomposition-of-submartingale",
        "title_en": "Doob Decomposition of Submartingales",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.4",
        "desc": "A submartingale sequence with sup E|X_n| < ∞ decomposes as X_n = X'_n + X''_n where X'_n is a martingale with sup E|X'_n| < ∞ and 0 ≤ X''_n ↑ X'' finite a.s. Thus submartingale convergence follows from martingale convergence.",
        "latex": r"""\begin{theorem}[Doob Decomposition of Submartingales]
Let $X_1, X_2, \ldots$ be a submartingale sequence with $\sup E|X_n| < \infty$.
Then $X_n = X'_n + X''_n$ where:
\begin{itemize}
\item $X'_1, X'_2, \ldots$ is a martingale sequence with $\sup E|X'_n| < \infty$,
\item $0 \leq X''_n \uparrow X''$ finite a.s.
\end{itemize}
Therefore $X'_n \xrightarrow{a.s.} X'$ finite and $X_n \xrightarrow{a.s.} X = X' + X''$ finite.
\end{theorem}"""
    },
    # === Ch X: Ergodic Theorems ===
    {
        "slug": "riesz-lemma-on-m-positive-terms",
        "title_en": "F. Riesz's Lemma on m-positive Terms",
        "type": "lemma",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "33.2",
        "desc": "If there exist terms that are m-positive (i.e., all partial sums starting from that term up to length m are positive), then their total sum is positive. The successive m-positive terms form disjoint stretches of positive sums.",
        "latex": r"""\begin{lemma}[F.\ Riesz]
If there exist $m$-positive terms in a finite sequence $\{a_k\}$, then their sum is positive.
Moreover, successive $m$-positive terms form disjoint stretches of positive sums.
\end{lemma}"""
    },
    {
        "slug": "basic-ergodic-inequality",
        "title_en": "Basic Ergodic Inequality",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "33.2",
        "desc": "For ratios X^j/Y^j of sums of translates, with Y_n > 0, the basic inequality bounds integrals over the event where the supremum exceeds a threshold. It is the key tool for proving almost sure convergence in ergodic theorems.",
        "latex": r"""\begin{theorem}[Basic Ergodic Inequality]
Let $B^m = [\sup_{j \leq m} X^j/Y^j > b]$ and $Z^n > 0$. For every integer $n$ and invariant event $C$,
\[
\sum_{k=1}^{n} \int_{B_k^m C} \left(\frac{X_k}{Z^n} - b\frac{Y_k}{Z^n}\right)
+ \sum_{k=n+1}^{n+m} \int_C \left(\frac{X_k}{Z^n} - b\frac{Y_k}{Z^n}\right)^+ \geq 0,
\]
provided the sums exist. Here $B_k^m$ is the translate by $k-1$ of $B^m$.
\end{theorem}"""
    },
    {
        "slug": "basic-ergodic-theorem",
        "title_en": "Basic Ergodic Theorem (Hopf-Riesz)",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "33.2",
        "desc": "Under conditions (i) ∫|X_{n+k}|/Y^n → 0 and (ii) ∫ Y_{n+k}/Y^n → 0 for each fixed k, the ratio X^n/Y^n of sums of translates converges almost surely.",
        "latex": r"""\begin{theorem}[Basic Ergodic Theorem]
Let $\{X_n\}, \{Y_n\}$ be sequences of random variables with $Y_n > 0$ and $Y^n = \sum_{k=1}^{n} Y_k \uparrow \infty$.
Assume for every fixed $k$ as $n \to \infty$:
\[
\text{(i) } \int \frac{|X_{n+k}|}{Y^n} \to 0, \qquad
\text{(ii) } \int \frac{Y_{n+k}}{Y^n} \to 0.
\]
Then the sequence $X^n/Y^n$ converges almost surely.
\end{theorem}"""
    },
    {
        "slug": "integral-stationarity",
        "title_en": "Integral Stationarity",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "33.3",
        "desc": "A random variable ξ defined on a family of sequences is integral invariant (or the sequence of translates ξ_k is integral stationary) if ∫_{A_k} ξ_k = ∫_{A_1} ξ_1 for every event A and every k.",
        "latex": r"""\begin{definition}[Integral Stationarity]
Let $\{X_n\}, \{Y_n\}$ be a family of random variables on which translations are defined.
A random variable $\xi$ is \emph{integral invariant} (or the sequence $\{\xi_k\}$ is
\emph{integral stationary}) if the integrals exist and for every event $A$ and every $k$,
\[
\int_{A_k} \xi_k = \int_{A_1} \xi_1,
\]
where $A_k$ and $\xi_k$ denote the translates by $k-1$ of $A$ and $\xi$ respectively.
\end{definition}"""
    },
    {
        "slug": "singular-transition-probability-lemma",
        "title_en": "Singular Transition Probability Lemma",
        "type": "lemma",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "33.5",
        "desc": "For every fixed x, the sequence P_s^n(x, R) of singular transition probabilities is nonincreasing and hence converges. The limit is called the singular transition probability.",
        "latex": r"""\begin{lemma}[Singular Transition Probability]
For every fixed $x \in R$, the sequence $P_s^n(x, R)$ is nonincreasing and hence converges.
The limit $\bar{P}_s(x, R) = \lim P_s^n(x, R) = \lim P^n(x, S_n)$ is called the
\emph{singular transition probability}.
\end{lemma}"""
    },
    {
        "slug": "vanishing-singular-transition-probability-theorem",
        "title_en": "Vanishing Singular Transition Probability Theorem",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "33.5",
        "desc": "For x with vanishing singular tr.pr., the Cesàro average of n-step transition probabilities converges to an idempotent, P-continuous limit function satisfying the invariance relation.",
        "latex": r"""\begin{theorem}[Vanishing Singular Transition Probability]
For every $x$ such that $\bar{P}_s(x, R) = 0$ and for every Borel set $S$,
\[
\frac{1}{n} \sum_{k=1}^{n} P^k(x, S) \to \bar{P}(x, S),
\]
where $\bar{P}(x, S)$ is $\bar{P}$-continuous and satisfies
\[
\bar{P}(x, S) = \int \bar{P}(x, dy) P(y, S).
\]
If $\bar{P}_s(\cdot, R) = 0$ $\bar{P}$-a.e., then $\bar{P}(x, S)$ is idempotent:
\[
\bar{P}(x, S) = \int \bar{P}(x, dy) \bar{P}(y, S).
\]
\end{theorem}"""
    },
    {
        "slug": "translation-on-sigma-fields",
        "title_en": "Translation on σ-fields",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "34.1",
        "desc": "A translation T on a σ-field α is a transformation preserving all countable set operations, with TΩ = Ω and T∅ = ∅. It extends uniquely to measurable functions, preserving linearity, continuity, and multiplicative structure.",
        "latex": r"""\begin{definition}[Translation on $\sigma$-fields]
A single-valued transformation $T$ on a $\sigma$-field $\mathcal{A}$ into itself is a
\emph{translation} (by 1) if it preserves all countable operations on events:
\[
T\left(\bigcup A_j\right) = \bigcup T A_j, \quad
T\left(\bigcap A_j\right) = \bigcap T A_j, \quad
T A^c = (T A)^c,
\]
and $T\Omega = \Omega$, $T\emptyset = \emptyset$. The $k$th iterate is $T^k$.
\end{definition}"""
    },
    {
        "slug": "translation-extension-to-measurable-functions",
        "title_en": "Extension of Translation to Measurable Functions",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "34.1",
        "desc": "A translation T on indicator functions has a unique extension to a linear continuous transformation on all measurable functions, with T1 = 1 and TI_{AB} = TI_A · TI_B. The translate of a simple function ∑ x_k I_{A_k} is ∑ x_k I_{TA_k}.",
        "latex": r"""\begin{theorem}[Extension of Translation]
A translation $T$ on $I_{\mathcal{A}}$ (indicators of events) has a unique extension
to a translation $T$ on $\mathfrak{M}$ (measurable functions) satisfying:
\begin{enumerate}
\item Linearity: $T(c\xi + c'\xi') = c T\xi + c' T\xi'$,
\item Continuity: $T(\sup \xi^{(n)}) = \sup T\xi^{(n)}$,
\item $T1 = 1$ and $T I_{AB} = T I_A \cdot T I_B$.
\end{enumerate}
The translate of a simple function is $T(\sum x_k I_{A_k}) = \sum x_k I_{T A_k}$.
\end{theorem}"""
    },
    {
        "slug": "ergodic-lemma",
        "title_en": "Ergodic Lemma",
        "type": "lemma",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "34.2",
        "desc": "If limsup P̄^n A → 0 as A ↓ ∅, then T̄^n X →^{a.s.} T̄ X invariant for every X with certain integrability conditions. In particular, this holds for all bounded random variables.",
        "latex": r"""\begin{lemma}[Ergodic Lemma]
Assume $\limsup \overline{P}^n A \to 0$ as $A \downarrow \emptyset$, where
$\overline{P}^n A = \frac{1}{n}\sum_{k=1}^{n} P T^{k-1} A$.
Then $\overline{T}^n X \xrightarrow{a.s.} \overline{T}X$ invariant, for every $X$ such that
\[
\frac{1}{n} \int |T^{n-1}X| \to 0 \quad\text{and}\quad
\frac{1}{n} \sum_{k=1}^{n} \int_{T^{k-1}A} T^{k-1}X \to 0
\]
as $n \to \infty$ and then $A \downarrow \emptyset$. In particular, this holds for every bounded $X$.
\end{lemma}"""
    },
    {
        "slug": "invariant-probability-lemma",
        "title_en": "Invariant Probability Lemma",
        "type": "lemma",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "34.2",
        "desc": "Three equivalent conditions: (i) limsup P̄^n A → 0 as A↓∅, (ii) lim P̄^n = P̄ exists and is a probability on α, (iii) there exists a T-invariant probability P̄ coinciding with P on the σ-field C of invariant events.",
        "latex": r"""\begin{lemma}[Invariant Probability]
The following properties are equivalent:
\begin{enumerate}
\item[(i)] $\limsup \overline{P}^n A \to 0$ as $A \downarrow \emptyset$.
\item[(ii)] $\lim \overline{P}^n = \overline{P}$ exists and is a probability on $\mathcal{A}$.
\item[(iii)] There exists on $\mathcal{A}$ a probability $\overline{P}$ invariant under $T$
  and coinciding with $P$ on the $\sigma$-field $\mathcal{C}$ of invariant events.
  In this case, $\lim \overline{P}^n = \overline{P}$.
\end{enumerate}
\end{lemma}"""
    },
    {
        "slug": "birkhoff-ergodic-theorem",
        "title_en": "Birkhoff's Ergodic Theorem",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "34.2",
        "desc": "If X ∈ L_1, then the time average (1/n)∑_{k=1}^n X(T_1^{k-1}ω) converges almost surely to an invariant limit. This is the foundational almost-sure ergodic theorem for measure-preserving transformations.",
        "latex": r"""\begin{theorem}[Birkhoff's Ergodic Theorem]
Let $T_1$ be a measure-preserving transformation on $(\Omega, \mathcal{A}, P)$ and
$X \in L_1(\Omega, \mathcal{A}, P)$. Then
\[
\frac{1}{n} \sum_{k=1}^{n} X(T_1^{k-1}\omega) \xrightarrow{a.s.} \overline{X}(\omega),
\]
where $\overline{X}$ is $T_1$-invariant and $E\overline{X} = EX$.
\end{theorem}"""
    },
    {
        "slug": "von-neumann-ergodic-theorem",
        "title_en": "von Neumann's Ergodic Theorem (Mean Ergodic Theorem)",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "34.2",
        "desc": "If X ∈ L_2, then the time average (1/n)∑_{k=1}^n X(T_1^{k-1}ω) converges in quadratic mean to an invariant limit. This is the L_2 ergodic theorem, predating Birkhoff's almost-sure result.",
        "latex": r"""\begin{theorem}[von Neumann's Mean Ergodic Theorem]
Let $T_1$ be a measure-preserving transformation on $(\Omega, \mathcal{A}, P)$ and
$X \in L_2(\Omega, \mathcal{A}, P)$. Then
\[
\frac{1}{n} \sum_{k=1}^{n} X(T_1^{k-1}\omega) \xrightarrow{q.m.} \overline{X},
\]
where $\overline{X}$ is $T_1$-invariant.
\end{theorem}"""
    },
    # === Ch XI: Second Order Properties ===
    {
        "slug": "orthogonal-random-variables",
        "title_en": "Orthogonal Random Variables",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "second-order-properties",
        "chapter": "XI", "section": "36.1",
        "desc": "Two random variables X, Y ∈ L_2 are orthogonal if EXȲ = 0. A sequence of orthogonal r.v.'s has uncorrelated summands, and sums of orthogonal r.v.'s enjoy stability properties.",
        "latex": r"""\begin{definition}[Orthogonal Random Variables]
Random variables $X, Y \in L_2$ are \emph{orthogonal} if $EX\overline{Y} = 0$.
A sequence $\{X_n\}$ is orthogonal if $EX_m \overline{X}_n = 0$ for $m \neq n$.
\end{definition}"""
    },
    {
        "slug": "elementary-orthogonal-decomposition",
        "title_en": "Elementary Orthogonal Decomposition",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "second-order-properties",
        "chapter": "XI", "section": "36.2",
        "desc": "A second-order random function X(t) admits an orthogonal decomposition in terms of orthonormalized proper functions of its covariance. This yields a Karhunen-Loève-type expansion with optimal approximation properties.",
        "latex": r"""\begin{theorem}[Elementary Orthogonal Decomposition]
Let $X(t)$ be a second-order random function with continuous covariance $\Gamma(t, t')$.
Let $\{\psi_n\}$ be the orthonormalized proper functions of $\Gamma$ and
$\lambda_n \xi_n = \int X(t) \overline{\psi}_n(t) \, dt$.
Then the $\xi_n$ are orthonormal ($E\xi_m \overline{\xi}_n = \delta_{mn}$) and
$E|X(t) - X_n(t)|^2 \to 0$ uniformly, where $X_n(t) = \sum_{k=1}^{n} \xi_k \psi_k(t)$.
\end{theorem}"""
    },
    {
        "slug": "covariance-function-of-second-order-random-function",
        "title_en": "Covariance Function of a Second-Order Random Function",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "second-order-properties",
        "chapter": "XI", "section": "37.1",
        "desc": "The covariance function Γ(t, t') = E X(t) X̄(t') - EX(t) EX̄(t') of a second-order random function X(t) is nonnegative-definite and determines the second-order structure of the process.",
        "latex": r"""\begin{definition}[Covariance Function]
The \emph{covariance function} of a second-order random function $X(t)$ is
\[
\Gamma(t, t') = E X(t) \overline{X}(t') - EX(t) E\overline{X}(t').
\]
It is nonnegative-definite: for any finite set $\{t_j\}$ and complex numbers $\{c_j\}$,
\[
\sum_{j,k} c_j \overline{c}_k \Gamma(t_j, t_k) \geq 0.
\]
\end{definition}"""
    },
    {
        "slug": "quadratic-mean-calculus-continuity-and-differentiation",
        "title_en": "Calculus in Quadratic Mean: Continuity and Differentiation",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "second-order-properties",
        "chapter": "XI", "section": "37.2",
        "desc": "A second-order random function X(t) is continuous (resp. differentiable) in quadratic mean at t if E|X(t+h) - X(t)|^2 → 0 (resp. the q.m. limit of (X(t+h) - X(t))/h exists) as h → 0.",
        "latex": r"""\begin{definition}[Quadratic Mean Calculus]
A second-order random function $X(t)$ is:
\begin{itemize}
\item \emph{continuous in q.m.} at $t$ if $\lim_{h \to 0} E|X(t+h) - X(t)|^2 = 0$;
\item \emph{differentiable in q.m.} at $t$ if the q.m.\ limit
  $X'(t) = \operatorname{q.m.\!}\lim_{h \to 0} \frac{X(t+h) - X(t)}{h}$ exists.
\end{itemize}
Continuity in q.m.\ is equivalent to continuity of the covariance $\Gamma(t, t')$ on the diagonal.
\end{definition}"""
    },
    {
        "slug": "orthogonal-increments",
        "title_en": "Second-Order Random Function with Orthogonal Increments",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "second-order-properties",
        "chapter": "XI", "section": "37.2",
        "desc": "A second-order random function ξ(t) has orthogonal increments if E ξ[a,b] ξ̄[a',b'] = 0 for disjoint intervals [a,b) and [a',b'). The increment function is additive: ξ[a,b] + ξ[b,c] = ξ[a,c).",
        "latex": r"""\begin{definition}[Orthogonal Increments]
A second-order random function $\xi(t)$ has \emph{orthogonal increments} if for disjoint intervals,
\[
E\,\xi[a,b]\,\overline{\xi}[a',b'] = 0,
\]
where $\xi[a,b] = \xi(b) - \xi(a)$. The increment function is characterized by additivity:
\[
\xi[a,b] + \xi[b,c] = \xi[a,c).
\]
Then $E|\xi[a,b]|^2$ is a nondecreasing function defining the associated spectral measure.
\end{definition}"""
    },
    {
        "slug": "fourier-stieltjes-transform-in-quadratic-mean",
        "title_en": "Fourier-Stieltjes Transform in Quadratic Mean",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "second-order-properties",
        "chapter": "XI", "section": "37.4",
        "desc": "A second-order stationary random function admits a spectral representation via a Fourier-Stieltjes integral in quadratic mean with orthogonal increments, generalizing the classical spectral decomposition.",
        "latex": r"""\begin{theorem}[Fourier-Stieltjes Transform in q.m.]
For a second-order stationary random function $X(t)$ with covariance $\Gamma(t)$,
there exists a random function $\xi(\lambda)$ with orthogonal increments such that
\[
X(t) = \int e^{it\lambda} \, d\xi(\lambda) \quad \text{(in q.m.)},
\]
and the covariance has the spectral representation
\[
\Gamma(t) = \int e^{it\lambda} \, dF(\lambda),
\]
where $F(\lambda) = E|\xi(\lambda)|^2$ is the spectral distribution function.
\end{theorem}"""
    },
    {
        "slug": "conditional-expectation-commutes-with-measurable-functions",
        "title_en": "Conditional Expectation Commutes with ℬ-measurable Factors",
        "type": "proposition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.2",
        "desc": "If X is ℬ-measurable, then E^ℬ(XY) = X E^ℬ Y a.s. More generally, ℬ-measurable factors can be pulled out of conditional expectations.",
        "latex": r"""\begin{proposition}[Commutation with Measurable Factors]
If $X$ is $\mathcal{B}$-measurable, then
\[
E^{\mathcal{B}}(XY) = X E^{\mathcal{B}}Y \quad \text{a.s.}
\]
\end{proposition}"""
    },
    {
        "slug": "tower-property-of-conditional-expectations",
        "title_en": "Tower Property of Conditional Expectations",
        "type": "proposition",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "28.2",
        "desc": "If ℬ ⊂ ℬ', then E^ℬ(E^{ℬ'} X) = E^ℬ X a.s. This is the iterated conditioning (tower) property central to martingale theory.",
        "latex": r"""\begin{proposition}[Tower Property]
If $\mathcal{B} \subset \mathcal{B}'$, then
\[
E^{\mathcal{B}}(E^{\mathcal{B}'}X) = E^{\mathcal{B}}X \quad \text{a.s.}
\]
\end{proposition}"""
    },
    {
        "slug": "de-finetti-exchangeability-theorem",
        "title_en": "de Finetti's Exchangeability Theorem",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "30.3",
        "desc": "The concept of exchangeability of a sequence of random variables is equivalent to conditional independence with common conditional distribution. Exchangeable sequences are mixtures of i.i.d. sequences.",
        "latex": r"""\begin{theorem}[de Finetti's Exchangeability]
The concept of exchangeability of a sequence of random variables is equivalent to that of
conditional independence with common conditional distribution function.
Specifically, $\{X_n\}$ is exchangeable iff there exists a $\sigma$-field $\mathcal{B}$ such that,
conditionally on $\mathcal{B}$, the $X_n$ are independent with common conditional distribution.
\end{theorem}"""
    },
    {
        "slug": "law-of-countable-family-by-conditional-distributions",
        "title_en": "Law of a Countable Family Determined by Conditional Distributions",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "conditioning",
        "chapter": "VIII", "section": "30.2",
        "desc": "The law of a countable family X_1, X_2, ... determines and is determined by a family P(S_1), P(x_1; S_2), P(x_1, x_2; S_3), ... of conditional distribution functions -- a nonsuperabundant parametrization.",
        "latex": r"""\begin{theorem}[Law by Conditional Distributions]
The law of the countable family $X_1, X_2, \ldots$ determines and is determined by a family
\[
P(S_1),\; P(x_1; S_2),\; P(x_1, x_2; S_3),\; \ldots
\]
of conditional distribution functions. This parametrization is nonsuperabundant (no consistency
relations are required between members).
\end{theorem}"""
    },
    {
        "slug": "martingale-convergence-of-conditional-expectations",
        "title_en": "Martingale Convergence of Conditional Expectations",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "martingales",
        "chapter": "IX", "section": "32.4",
        "desc": "The sequence Z_n = E(Y | Y_1, ..., Y_n) is a martingale closed on the right by Y. If E|Y|^r < ∞ for r ≥ 1, then Z_n →^{a.s.} E(Y | Y_1, Y_2, ...). This provides martingale proofs of zero-one laws.",
        "latex": r"""\begin{theorem}[Martingale Convergence of Conditional Expectations]
Let $Y, Y_1, Y_2, \ldots$ be random variables. The sequence
$Z_n = E(Y \mid Y_1, \ldots, Y_n)$ is a martingale closed on the right by $Y$ (provided
the expectation exists, e.g., $EY^+ < \infty$). Then:
\begin{enumerate}
\item $Z_n \xrightarrow{a.s.} Z < \infty$;
\item If $E|Y|^r < \infty$ for some $r \geq 1$, then
  $Z_n \xrightarrow{a.s.} Z = E(Y \mid Y_1, Y_2, \ldots)$;
\item If $Y$ is defined on the $Y_n$, then $Z_n \xrightarrow{a.s.} Y$.
\end{enumerate}
\end{theorem}"""
    },
    {
        "slug": "exponential-convergence-for-markov-chains",
        "title_en": "Exponential Convergence for Markov Chains",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "markov-chains",
        "chapter": "VIII", "section": "30.3",
        "desc": "If the h-step transition density has a positive lower bound on a μ-positive set, then the n-step transition probabilities converge exponentially fast to an invariant limit, with rate governed by the Markov measure.",
        "latex": r"""\begin{theorem}[Exponential Convergence for Chains]
Let $\mu$ be a $\sigma$-finite measure and
$P^h(x, S) = \int p^h(x, y) \mu(dy) + P_s^h(x, S)$
where $p^h(x, y) \geq 0$ and $P_s^h$ is $\mu$-singular.
If $\inf_x p^h(x, y) \geq \delta > 0$ for all $y$ in some $\mu$-positive set, then
\[
|P^n(x, S) - \bar{P}(S)| \leq a e^{-b n}
\]
for some constants $a, b > 0$, i.e., exponential convergence holds.
\end{theorem}"""
    },
    {
        "slug": "svan-condition",
        "title_en": "Uniformly Asymptotically Negligible (UAN) Condition",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "limit-theorems",
        "chapter": "IX", "section": "31.3",
        "desc": "A triangular array X_{nk} satisfies the UAN (uniform asymptotic negligibility) condition if max_k P[|X_{nk}| ≥ ε] → 0 for every ε > 0. This generalizes the classical Lindeberg-Feller condition to the dependent setting.",
        "latex": r"""\begin{definition}[UAN Condition]
A triangular array $\{X_{nk}\}$ satisfies the \emph{uniform asymptotic negligibility} (uan) condition if,
for every $\epsilon > 0$,
\[
\max_k P[|X_{nk}| \geq \epsilon] \to 0 \quad \text{as } n \to \infty.
\]
Under the uan condition and with centering at conditional expectations, for every $\epsilon > 0$:
\begin{enumerate}
\item[(i)] $\max_k \int_{|x|<\epsilon} |x|^s \, dF'_{nk} \xrightarrow{P} 0$ for $s > 0$;
\item[(ii)] $\max_k \int_{|x|<\epsilon} |x - \alpha'_{nk}(\epsilon)|^s \, dF'_{nk} \xrightarrow{P} 0$ for $s \geq 1$;
\item[(iii)] $\max_k |\gamma'_{nk}(u)| \xrightarrow{P} 0$.
\end{enumerate}
\end{definition}"""
    },
    {
        "slug": "comparison-theorem-for-dependent-summands",
        "title_en": "Comparison Theorem for Dependent Summands",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "limit-theorems",
        "chapter": "IX", "section": "31.2",
        "desc": "Under suitable moment conditions, the law of a sum of dependent summands is asymptotically equivalent to the law of a sum of conditionally independent summands with matching conditional moments.",
        "latex": r"""\begin{theorem}[Comparison Theorem]
Under the uan condition and centering at conditional expectations, for suitable $S, l, m, \delta$,
the law of $\sum_k X_{nk}$ is asymptotically equivalent to that of $\sum_k Y_{nk}$ where the $Y_{nk}$
are conditionally infinitely divisible with characteristic functions $g'_{nk}$ derived from the
conditional moments of $X_{nk}$. In particular,
\[
\left|E\exp\left[iu\sum_k X_{nk}\right] - E\exp\left[iu\sum_k Y_{nk}\right]\right| \to 0.
\]
\end{theorem}"""
    },
    {
        "slug": "basic-ergodic-theorem-extension",
        "title_en": "Basic Ergodic Theorem with Condition (C)",
        "type": "theorem",
        "domain": "probability-theory",
        "subdomain": "ergodic-theory",
        "chapter": "X", "section": "33.2",
        "desc": "The basic ergodic theorem remains valid if Y^n is replaced by Z^n satisfying condition (C): for every invariant event C, liminf ∫_C Y^n/Z^n = 0 implies PC = 0.",
        "latex": r"""\begin{theorem}[Basic Ergodic Theorem with Condition (C)]
The basic ergodic theorem remains valid if $Y^n$ is replaced by positive random variables $Z^n$
satisfying condition (C):
\[
\liminf \int_C \frac{Y^n}{Z^n} = 0 \implies PC = 0
\]
for every invariant event $C$ defined on $\{X_n\}, \{Y_n\}$.
\end{theorem}"""
    },
    {
        "slug": "stationary-chain-and-invariant-distribution",
        "title_en": "Stationary Chain and Invariant Distribution",
        "type": "definition",
        "domain": "probability-theory",
        "subdomain": "markov-chains",
        "chapter": "VIII", "section": "30.3",
        "desc": "A constant Markov chain is stationary if its initial distribution P_1 is invariant: P_1(S) = ∫ P_1(dx) P(x; S). Then the joint distribution of (X_m, ..., X_{m+n}) is independent of m for all n.",
        "latex": r"""\begin{definition}[Stationary Chain]
A transition probability $P(x, S)$ possesses an \emph{invariant distribution} $P_1(S)$ if
\[
P_1(S) = \int P_1(dx) P(x; S) \quad \text{for every Borel } S.
\]
The chain determined by $P_1(S)$ and $P(x, S)$ is \emph{stationary}: for every $n$,
the distribution of $(X_m, \ldots, X_{m+n})$ is independent of $m$.
\end{definition}"""
    },
]

os.makedirs(BASE, exist_ok=True)
total = 0

for c in concepts:
    slug = c["slug"]
    dirpath = os.path.join(BASE, slug)
    os.makedirs(dirpath, exist_ok=True)

    # concept.yaml
    yaml_data = {
        "id": slug,
        "title_en": c["title_en"],
        "title_zh": "",
        "type": c["type"],
        "domain": c["domain"],
        "subdomain": c["subdomain"],
        "difficulty": "basic",
        "tags": [],
        "depends_on": {"required": [], "recommended": [], "suggested": []},
        "proof_deps": {},
        "source_books": [{
            "book_id": BOOK_ID,
            "author": AUTHOR,
            "title": TITLE,
            "chapter": c["chapter"],
            "section": c["section"],
            "pages": "",
            "role_in_book": "source"
        }],
        "content_hash": hashlib.sha256(c["latex"].encode()).hexdigest()[:16],
        "extraction_date": DATE,
        "extraction_agent": AGENT
    }
    with open(os.path.join(dirpath, "concept.yaml"), "w") as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # theorem.tex - pure LaTeX
    with open(os.path.join(dirpath, "theorem.tex"), "w") as f:
        f.write(c["latex"].strip() + "\n")

    # introduce.en.md - YAML frontmatter + description
    md = f"""---
id: {slug}
title: "{c['title_en']}"
type: {c['type']}
domain: {c['domain']}
subdomain: {c['subdomain']}
source: {BOOK_ID} Ch.{c['chapter']} Sec.{c['section']}
---

{c['desc']}
"""
    with open(os.path.join(dirpath, "introduce.en.md"), "w") as f:
        f.write(md.strip() + "\n")

    total += 1

# Write .done
with open(os.path.join(BASE, ".done"), "w") as f:
    f.write("DONE\n")

print(f"Created {total} concepts in {BASE}")
