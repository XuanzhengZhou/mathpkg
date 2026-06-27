---
role: proof
locale: en
of_concept: lemma-8-2
source_book: gtm040
source_chapter: "8"
source_section: "2"
---

**Proof:** We have

$$N_{ij} = H_{ij} N_{jj} \leq N_{jj}.$$

Thus

$$|(\mu N)_j| \leq \sum_i |\mu_i

Theorem 8-3: If $\alpha f$ is finite, then $f$ is a charge and its potential is $g = Nf$.

Proof: By Lemma 8-2, $Nf$ is well defined and finite-valued. Hence so are both $Nf^+$ and $Nf^-$. By monotone convergence,

$$\lim_n [(I + P + \cdots + P^{n-1})f^+] = Nf^+$$

and

$$\lim_n [(I + P + \cdots + P^{n-1})f^-] = Nf^-.$$

Thus

$$\lim_n [(I + P + \cdots + P^{n-1})f] = Nf^+ - Nf^- = Nf.$$

Thus $f$ is a charge if and only if it is integrable with respect to $\alpha$, and $N$ is the potential operator that transforms a charge into its potential. In particular, $f$ is a charge for $P$ if and only if it is a charge for $\hat{P}$. We shall now show that $I - P$ is the inverse operator.

Theorem 8-4: If $g$ is a potential, then $(I - P)g$ is its charge.

Proof: Let $f$ be a charge with potential $g$. By Theorem 8-3, $g = Nf$. Hence, by Lemma 5-9, $(I - P)g = f$.

Therefore, there is a one-to-one correspondence between charges and potentials. Note that Theorem 8-4 implies that a potential is regular at all states where the charge is zero.

The method used to derive the second half of Lemma 8-2 is of general importance. We prove a result for all our $P$'s for signed measures (or functions). We apply the result to $\hat{P}$ and obtain a corresponding result for functions (or signed measures). Then since $\hat{P}$ is the form of the most general transient chain being considered, the new result holds for all $P$'s. Such results will loosely be described as duals.

The duals of Theorems 8-3 and 8-4 state that a signed measure $\mu$ is a charge

Proposition 8-5: There exists a strictly positive pure potential.

Proof: Number the states and let $f_j = 2^{-j}/\alpha_j$. Then

$$\alpha f = \sum_j \alpha_j (2^{-j}/\alpha_j) = 1,$$

so that $f$ is the charge of a pure potential $g$, by Theorem 8-3. Furthermore,

$$g_i = \sum_j N_{ij} f_j \geq N_{ii} f_i \geq f_i > 0,$$

so that $g$ is strictly positive.

For many purposes it is sufficient in studying potentials to consider only pure potentials. The reason for this simplification is the following.

Proposition 8-6: Any potential may be represented as the difference of two pure potentials.

Proof: Write $g = Nf = Nf^+ - Nf^-$.

Note by Theorem 8-4 that a potential is superregular if and only if it is a pure potential.

We recall from Theorem 5-10 that a non-negative superregular function $h$ is uniquely representable as $h = Nf + r$ with $r$ regular. In the representation, $r = \lim_n P^n h \geq 0$ and $f = (I - P)h \geq 0$. (The dual of this result allows the unique representation of a non-negative superregular measure $\pi$ as $\pi = \mu N + \rho$ with $\rho$ regular. In this representation, $\rho = \lim_n \pi P^n \geq 0$ and $\mu = \pi(I - P)$.) This result is the analog of a classical theorem due to F. Riesz: In any open set of Euclidean space which corresponds to a transient version of Brownian motion, any non-negative superharmonic function is uniquely the sum of a pure potential for the region and a non-negative harmonic function. The pure potential may have infinite total charge. We now generalize the Markov chain result, and in so doing we obtain a useful necessary condition that potentials must satisfy.

Proposition 8-7: If $(I - P)h = f$, if $h$ is finite-valued, and if $Nf$ is

PROOF: Set $r = h - Nf$. Then

$$ (I - P)(h - Nf) = (I - P)h - (I - P)(Nf) $$
$$ = (I - P)h - f \text{ by Lemma 5-9} $$
$$ = f - f = 0. $$

Hence $r$ is regular. Now

$$ f = (I - P)h = h - Ph $$

or

$$ h = Ph + f. $$

Since $Nf$ is finite-valued and since $P^n f^+ \leq Nf^+$ and $P^n f^- \leq Nf^-$, $P^n f$ is finite-valued for every $n$. By induction we see that

$$ P^{k-1}h = P^kh + P^{k-1}f $$

and that $P^k h$ is finite-valued. Summing for $k = 1, \ldots, n$, we obtain

$$ h = P^n h + (I + P + \cdots + P^{n-1})f. $$

By dominated convergence the second term tends to $Nf$. Hence

$$ h = \lim_n P^n h + Nf. $$

Corollary 8-8: If $(I - P)h = f$, if $h$ is finite-valued, and if $\alpha f$ is finite, then $h$ is a potential if and only if $\lim_n P^n h = 0$.

PROOF: By Theorem 8-3, $f$ is a charge and $Nf$ is its potential. Apply Proposition 8-7 and write

$$ h = Nf + \lim P^n h. $$

If $\lim P^n h = 0$, then $h$ is the potential of $f$. Conversely, if $\lim P^n h \neq 0$, then $h$ cannot be a potential because, by Theorem 8-4, it would have to have $f$ as its charge.

Corollary 8-9: If $g$ is a potential, then $\lim_n P^n g = 0$.

PROOF: Take $h = g$ in Coroll

and $N_{ii}$ is independent of $i$. Hence, $\alpha_i \geq kN_{ii}$ for some positive constant $k$. Furthermore, $\lim_i N_{ij} = 0$ by Proposition 7-10.
