---
role: proof
locale: en
of_concept: closure-under-pointwise-convergence
source_book: gtm095
source_chapter: "4"
source_section: "4"
---

# Proof of Closure of Extended Random Variables under Pointwise Convergence

## Part 1: Closure under $\sup$, $\inf$, $\limsup$, $\liminf$

We note first that if $\xi_1, \xi_2, \ldots$ is a sequence of extended random variables, then $\sup \xi_n$, $\inf \xi_n$, $\limsup \xi_n$ and $\liminf \xi_n$ are also random variables (possibly extended). This follows immediately from

$$\{\omega : \sup_n \xi_n > x\} = \bigcup_n \{\omega : \xi_n > x\} \in \mathcal{F},$$

$$\{\omega : \inf_n \xi_n < x\} = \bigcup_n \{\omega : \xi_n < x\} \in \mathcal{F},$$

and the relations

$$\limsup_n \xi_n = \inf_n \sup_{k \geq n} \xi_k, \qquad \liminf_n \xi_n = \sup_n \inf_{k \geq n} \xi_k.$$

Consequently, if $\lim \xi_n$ exists (finite or infinite), it is also a random variable.

## Part 2: Closure under algebraic operations

If $\xi$ and $\eta$ are random variables, $\xi + \eta$, $\xi - \eta$, $\xi \eta$, and $\xi/\eta$ are also random variables (assuming that they are defined, i.e., that no indeterminate forms like $\infty - \infty$, $\infty/\infty$, $a/0$ occur).

In fact, let $\{\xi_n\}$ and $\{\eta_n\}$ be sequences of simple random variables converging to $\xi$ and $\eta$ (see Theorem 1). Then

$$\xi_n \pm \eta_n \to \xi \pm \eta,$$
$$\xi_n \eta_n \to \xi \eta,$$
$$\frac{\xi_n}{\eta_n + \frac{1}{n} I_{\{\eta_n=0\}}(\omega)} \to \frac{\xi}{\eta}.$$

The functions on the left-hand sides of these relations are simple random variables. Therefore, by the closure under pointwise limits established in Part 1, the limit functions $\xi \pm \eta$, $\xi \eta$ and $\xi/\eta$ are also random variables.
