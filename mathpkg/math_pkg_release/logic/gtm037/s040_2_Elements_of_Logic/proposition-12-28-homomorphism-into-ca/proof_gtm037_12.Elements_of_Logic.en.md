---
role: proof
locale: en
of_concept: proposition-12-28-homomorphism-into-ca
source_book: gtm037
source_chapter: "12"
source_section: "Elements of Logic"
---

The proof is similar to that of 9.58, but is much more tedious. We first define a function $h \colon \operatorname{Fmla}_{\mathcal{L}} \to A$; $h\varphi$ is defined by induction on $\varphi$. The most complicated part of the definition is the case in which $\varphi$ is an atomic formula of the form $\mathbf{R}v_{i_0} \cdots v_{i_{m-1}}$. In this case, let $j_0, \ldots, j_{m-1}$ be the first $m$ integers in $\omega \sim \{i_0, \ldots, i_{m-1}, 0, \ldots, m-1\}$, and set

$$h\mathbf{R}v_{i_0} \cdots v_{i_{m-1}} = s_{i_0}^{j_0} \cdots s_{i_{m-1}}^{j_{m-1}} s_{j_0}^{0} \cdots s_{j_{m-1}}^{m-1} f_{\mathbf{R}};$$

for motivation, cf. the comments following 10.74. The inductive definition of $h\varphi$ proceeds very simply: $h(v_{\kappa} = v_{\lambda}) = d_{\kappa\lambda}$, while $h$ distributes over the sentential connectives $\neg$ and $\to$.

We consider the set $\Gamma$ of all formulas $\varphi$ such that $h\varphi = 1$. We aim to show that every logical theorem belongs to $\Gamma$. To verify that each logical axiom $\varphi$ satisfies $h\varphi = 1$, we need to check several cases. The case of equality axioms is straightforward using properties of diagonal elements $d_{\kappa\lambda}$.

Consider an instance of the substitution axiom: suppose $\varphi$ is

$$(v_{\kappa} = v_{\lambda} \to (\psi \to \chi))$$

where $\chi$ is obtained from $\psi$ by replacing some free occurrences of $v_{\kappa}$ by $v_{\lambda}$. If $\kappa = \lambda$, then $\varphi$ is $v_{\kappa} = v_{\kappa} \to (\psi \to \chi)$ with $\psi$ and $\chi$ identical, and clearly $h\varphi = 1$. If $\psi$ is $v_{\kappa} = v_{\mu}$ or $v_{\mu} = v_{\kappa}$ with $\kappa \neq \mu$, then $\chi$ is $v_{\lambda} = v_{\mu}$ or $v_{\mu} = v_{\lambda}$, and

$$d_{\kappa\lambda} \cdot d_{\kappa\mu} \leq c_{\kappa}(d_{\kappa\lambda} \cdot d_{\kappa\mu}) = d_{\lambda\mu};$$

hence

$$h\varphi = -d_{\kappa\lambda} + -d_{\lambda\mu} = 1.$$

So we may assume that $\psi$ has the form $\mathbf{R}v_{i_0} \cdots v_{i_{t-1}} v_{\kappa} v_{i_{t+1}} \cdots v_{i_{m-1}}$ and $\chi$ is $\mathbf{R}v_{i_0} \cdots v_{i_{t-1}} v_{\lambda} v_{i_{t+1}} \cdots v_{i_{m-1}}$. In this case we need several lemmas.

Let $j_0, \ldots, j_{m-1} \in \omega$, and let $k_0, \ldots, k_{m-1}, l$ be distinct integers in $\omega \sim \{j_0, \ldots, j_{m-1}, 0, \ldots, m-1\}$, and assume that $u < m$.

**(3)** Then

$$s_{j_0}^{k_0} \cdots s_{j_{m-1}}^{k_{m-1}} s_{k_0}^{0} \cdots s_{k_{m-1}}^{m-1} f_R = s_{j_0}^{k_0} \cdots s_{j_{u-1}}^{k_{u-1}} s_{j_u}^{l} s_{j_{u+1}}^{k_{u+1}} \cdots s_{j_{m-1}}^{k_{m-1}} s_{k_0}^{0} \cdots s_{k_{u-1}}^{u-1} s_{k_u}^{u} s_{k_{u+1}}^{u+1} \cdots s_{k_{m-1}}^{m-1} f_R.$$

Now we return to checking that $h\varphi = 1$ (see above prior to (3)). Choose $j_0, \ldots, j_{m-1} \in \omega \sim \{i_0, \ldots, i_{t-1}, i_{t+1}, \ldots, i_{m-1}, 0, \ldots, m-1, \kappa, \lambda\}$, and set

$$x = s_{i_0}^{j_0} \cdots s_{i_{t-1}}^{j_{t-1}} s_{i_{t+1}}^{j_{t+1}} \cdots s_{i_{m-1}}^{j_{m-1}} s_{j_0}^{0} \cdots s_{j_{m-1}}^{m-1} f_R.$$

Then by (5) and 12.6(x), $h\psi = s_{\kappa}^{j_t}x$ and $h\chi = s_{\lambda}^{j_t}x$. Now

$$d_{\kappa\lambda} \cdot s_{\kappa}^{j_t}x \leq s_{\lambda}^{j_t}x$$

by 12.6(v), so $h\varphi = -d_{\kappa\lambda} + -s_{\kappa}^{j_t}x + s_{\lambda}^{j_t}x = 1$, as desired.

We have now shown that $h\varphi = 1$ for each logical axiom $\varphi$, i.e., each logical axiom is in the set $\Gamma$ defined following (1). Obviously $\Gamma$ is closed under detachment and generalization. Thus each logical theorem is in $\Gamma$, and (1) follows.

Now if $\vdash \varphi \leftrightarrow \psi$, then $h(\varphi \leftrightarrow \psi) = 1$, and hence it follows easily that $h\varphi = h\psi$. Hence (since $\vdash$ is the logical equivalence relation) there is a function $g$ mapping $M_0^{\mathcal{L}}$ into $A$ such that $g[\varphi] = h\varphi$ for any $\varphi \in \operatorname{Fmla}_{\mathcal{L}}$. It is easily checked that $g$ is the desired homomorphism.
