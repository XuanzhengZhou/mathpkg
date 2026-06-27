---
role: proof
locale: en
of_concept: radon-nikodym-theorem
source_book: gtm018
source_chapter: "VI"
source_section: "31"
---

Since $X$ is a countable, disjoint union of measurable sets on which both $\mu$ and $\nu$ are finite, there is no loss of generality (for both the existence and the uniqueness proofs) in assuming finiteness in the first place. Since if $\nu$ is finite, $f$ is integrable, uniqueness follows from 25.E. Since, finally, the assumption $\nu \ll \mu$ is equivalent to the simultaneous validity of the conditions

$$\nu^+ \ll \mu \text{ and } \nu^- \ll \mu,$$

it remains only to prove the existence of $f$ in the case in which both $\mu$ and $\nu$ are finite measures.

Let $\mathcal{K}$ be the class of all non negative functions $f$, integrable with respect to $\mu$, such that $\int_E f d\mu \leq \nu(E)$ for every measurable set $E$, and write

$$\alpha = \sup \left\{ \int f d\mu : f \in \mathcal{K} \right\}.$$

Let $\{f_n\}$ be a sequence of functions in $\mathcal{K}$ such that

$$\lim_n \int f_n d\mu = \alpha.$$

If $E$ is any fixed measurable set, $n$ is any fixed positive integer, and $g_n = f_1 \cup \cdots \cup f_n$, then $E$ may be written as a finite, disjoint union of measurable sets, $E = E_1 \cup \cdots \cup E_n$, so that $g_n(x) = f_j(x)$ for $x$ in $E_j$, $j = 1, \cdots, n$. Consequently we have

$$\int_E g_n d\mu = \sum_{j=1}^{n} \int_{E_j} f_j d\mu \leq \sum_{j=1}^{n} \nu(E_j) = \nu(E).$$

If we write $f_0(x) = \sup \{f_n(x) : n = 1, 2, \cdots\}$, then $f_0(x) = \lim_n g_n(x)$ and it follows from 27.B that $f_0 \in \mathcal{K}$ and $\int f_0 d\mu = \alpha$. Since $f_0$ is integrable, there exists a finite valued function $f$ such that $f_0 = f[\mu]$; we shall prove that if $\nu_0(E) = \nu(E) - \int_E f d\mu$, then the measure $\nu_0$ is identically zero.

If $\nu_0$ is not identically zero, then, by Theorem A, there exists a positive number $\epsilon$ and a measurable set $A$ such that $\mu(A) > 0$ and such that

$$\epsilon \mu(E \cap A) \leq \nu_0(E \cap A) = \nu(E \cap A) - \int_E f d\mu$$

for every measurable set $E$. If $g = f + \epsilon \chi_A$, then

$$\int_E g d\mu = \int_E f d\mu + \epsilon \mu(E \cap A) \leq \int_{E-A} f d\mu + \nu(E \cap A) \leq \nu(E)$$

for every measurable set $E$, so that $g \in \mathcal{K}$. Since, however,

$$\int g d\mu = \int f d\mu + \epsilon \mu(A) > \alpha,$$

this contradicts the maximality of $\int f d\mu$, and the proof of the theorem is complete.
