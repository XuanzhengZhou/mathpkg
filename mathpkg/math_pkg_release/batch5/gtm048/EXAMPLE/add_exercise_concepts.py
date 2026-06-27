#!/usr/bin/env python3
"""Add concept.yaml, theorem.tex, introduce.en.md for exercise concepts."""
import os, json

BASE = '/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch5/gtm048/EXAMPLE'

# === Exercise concept 1: functions-of-rapid-decay ===
d = os.path.join(BASE, 'functions-of-rapid-decay')

yaml_data = {
    'id': 'functions-of-rapid-decay',
    'title_en': 'Exercise 5.6.6: Functions of Rapid Decay',
    'title_zh': '',
    'type': 'proposition',
    'domain': 'geometry',
    'subdomain': 'differential-geometry',
    'difficulty': 'advanced',
    'tags': ['general-relativity', 'lightcone', 'rapid-decay', 'integration', 'photon-gas', 'exercise'],
    'depends_on': {
        'required': ['rapid-decay-function-on-lightcone', 'instantaneous-observer', 'future-lightcone'],
        'recommended': ['photon-distribution-function'],
        'suggested': []
    },
    'source_books': [{
        'book_id': 'gtm048',
        'author': 'Rainer K. Sachs, Hung-Hsi Wu',
        'title': 'General Relativity for Mathematicians',
        'chapter': '5',
        'section': '5.6',
        'pages': '',
        'role_in_book': 'Exercise on functions of rapid decay on future lightcones'
    }],
    'content_hash': '',
    'extraction_date': '2026-06-27',
    'extraction_agent': 'v8-full-extract'
}
with open(os.path.join(d, 'concept.yaml'), 'w') as f:
    json.dump(yaml_data, f, indent=2, ensure_ascii=False)
    f.write('\n')

theorem_tex = r"""Let $(x, X)$ be an instantaneous observer, $\chi \in M_x^*$ be physically equivalent to $X$, $\pi_X: P_X \to \mathcal{L}_x^+$, and $\Lambda_x$ be the natural volume element on $\mathcal{L}_x^+$.

\begin{enumerate}
    \item[(a)] Suppose $\ell: (0, \infty) \to (0, \infty)$ is a function such that, for all non-negative integers $L, N$,
    $$\int_0^\infty e^N \left|\frac{d^L(e\ell)}{de^L}\right| de < \infty.$$
    With $a, b \in (0, \infty)$, define $f = a\ell \circ (-b\tilde{\chi}): \mathcal{L}_x^+ \to (0, \infty)$; thus $f(Y) = a\ell(-b g(X, Y))$ for all $Y \in \mathcal{L}_x^+$. Show that $f$ is a function of rapid decay.

    \item[(b)] Let $F_X$ be a photon distribution function for $(x, X)$; suppose $F_X$ is Planck. Show from (a) that $F_X \circ \pi_X^{-1}$ is a function of rapid decay.

    \item[(c)] Let $f: \mathcal{L}_x^+ \to [0, \infty)$ be a function of rapid decay and suppose $\omega \in M_x^*$. Show that $\omega$ can be written as the sum of two causal 1-forms and then that $\int_{\mathcal{L}_x^+} \tilde{\omega} f \Lambda_x$ exists and is finite.

    \item[(d)] In (c), show that $f \circ \pi_X$ is a photon distribution function for $(x, X)$ and that the total energy density $\lim_{a \to 0, b \to \infty} u[a, b]$ in Section 5.5.3a is finite.

    \item[(e)] In (c), suppose $\eta \in M_x^*$. Show that $\int_{\mathcal{L}_x^+} \tilde{\omega} \tilde{\eta} f \Lambda_x$ exists and is finite.

    \item[(f)] In (e), suppose $f$ is not identically zero on $\mathcal{L}_x^+$. Show that if $\omega$ and $\eta$ are future-pointing, then $\int_{\mathcal{L}_x^+} \tilde{\omega} \tilde{\eta} f \Lambda_x > 0$.
\end{enumerate}"""
with open(os.path.join(d, 'theorem.tex'), 'w') as f:
    f.write(theorem_tex.strip() + '\n')

intro = """---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Exercise 5.6.6 from Sachs and Wu's *General Relativity for Mathematicians* consists of six parts that develop the theory of functions of rapid decay on future lightcones. Part (a) shows that a wide class of radial functions constructed from a rapidly decaying profile on (0, infinity) are of rapid decay. Part (b) verifies that Planck photon distribution functions are of rapid decay. Parts (c)-(f) establish that integrals involving rapid decay functions and causal 1-forms converge, with positivity for future-pointing covectors. These results are essential for the construction of the stress-energy tensor of a photon gas in Proposition 5.7.2."""
with open(os.path.join(d, 'introduce.en.md'), 'w') as f:
    f.write(intro + '\n')

print('Done exercise 5.6.6')

# === Exercise concept 2: photon-gas-counterexamples ===
d = os.path.join(BASE, 'photon-gas-counterexamples')

yaml_data = {
    'id': 'photon-gas-counterexamples',
    'title_en': 'Exercise 5.7.8: Photon Gas Counterexamples',
    'title_zh': '',
    'type': 'proposition',
    'domain': 'geometry',
    'subdomain': 'differential-geometry',
    'difficulty': 'advanced',
    'tags': ['general-relativity', 'photon-gas', 'stress-energy-tensor', 'counterexample', 'exercise'],
    'depends_on': {
        'required': ['stress-energy-tensor-of-photon-gas', 'spatial-isotropy-of-stress-energy-tensor'],
        'recommended': ['conserved-photon-gas', 'number-density'],
        'suggested': []
    },
    'source_books': [{
        'book_id': 'gtm048',
        'author': 'Rainer K. Sachs, Hung-Hsi Wu',
        'title': 'General Relativity for Mathematicians',
        'chapter': '5',
        'section': '5.7',
        'pages': '',
        'role_in_book': 'Exercise constructing photon gas counterexamples'
    }],
    'content_hash': '',
    'extraction_date': '2026-06-27',
    'extraction_agent': 'v8-full-extract'
}
with open(os.path.join(d, 'concept.yaml'), 'w') as f:
    json.dump(yaml_data, f, indent=2, ensure_ascii=False)
    f.write('\n')

theorem_tex = r"""A photon gas $F$ has many properties in addition to those described by its stress-energy tensor $\hat{T}$ and number density $N$. Construct two examples:

\begin{enumerate}
    \item[(a)] Find photon gases $F, F'$ on Minkowski space such that $F \neq F'$, $\hat{T} = \hat{T}'$, and $N = N'$.
    \item[(b)] Find a photon gas $F$ on Minkowski space $M$ such that $\operatorname{div} \hat{T} = 0 = \operatorname{div} N$ but $F$ is not conserved on $M$.
\end{enumerate}"""
with open(os.path.join(d, 'theorem.tex'), 'w') as f:
    f.write(theorem_tex.strip() + '\n')

intro = """---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Exercise 5.7.8 from Sachs and Wu asks the reader to construct two counterexamples for photon gases. Part (a) shows that distinct photon gas distributions can share the same stress-energy tensor and number density. Part (b) demonstrates that vanishing divergence of the stress-energy tensor and number density does not imply the photon gas is conserved, showing the converse of the heuristic principle is false."""
with open(os.path.join(d, 'introduce.en.md'), 'w') as f:
    f.write(intro + '\n')

print('Done exercise 5.7.8')

# === Exercise concept 3: spatial-isotropy-perfect-fluid ===
d = os.path.join(BASE, 'spatial-isotropy-perfect-fluid')

yaml_data = {
    'id': 'spatial-isotropy-perfect-fluid',
    'title_en': 'Exercise 5.7.9: Spatial Isotropy and Perfect Fluid Correspondence',
    'title_zh': '',
    'type': 'proposition',
    'domain': 'geometry',
    'subdomain': 'differential-geometry',
    'difficulty': 'advanced',
    'tags': ['general-relativity', 'photon-gas', 'spatial-isotropy', 'perfect-fluid', 'exercise'],
    'depends_on': {
        'required': ['spatial-isotropy-of-stress-energy-tensor', 'stress-energy-tensor-of-photon-gas'],
        'recommended': ['perfect-fluid', 'timelike-convergence-condition'],
        'suggested': []
    },
    'source_books': [{
        'book_id': 'gtm048',
        'author': 'Rainer K. Sachs, Hung-Hsi Wu',
        'title': 'General Relativity for Mathematicians',
        'chapter': '5',
        'section': '5.7',
        'pages': '',
        'role_in_book': 'Exercise on spatial isotropy characterization and perfect fluid correspondence'
    }],
    'content_hash': '',
    'extraction_date': '2026-06-27',
    'extraction_agent': 'v8-full-extract'
}
with open(os.path.join(d, 'concept.yaml'), 'w') as f:
    json.dump(yaml_data, f, indent=2, ensure_ascii=False)
    f.write('\n')

theorem_tex = r"""Suppose that, for all $x \in M$, the restriction of $F$ to $\mathcal{L}_x^+$ is somewhere nonzero.

\begin{enumerate}
    \item[(a)] Show that $F$ is spatially isotropic for $(z, Z)$ if and only if $F \circ \pi_Z$ is independent of the direction $U$ in $\mathcal{S}_Z$, and that then $F$ is not spatially isotropic for $(z, Z')$ if $Z' \neq Z$.
    \item[(b)] Show that $\hat{T}$ obeys the timelike convergence condition.
    \item[(c)] Suppose there is a reference frame $X$ such that, for all $x \in M$, $F$ is spatially isotropic for $(x, Xx)$; define $\rho = T(X, X)$. Show that $(\rho, \rho/3, X)$ is a rest-mass zero perfect fluid with the same stress-energy tensor as $F$.
\end{enumerate}"""
with open(os.path.join(d, 'theorem.tex'), 'w') as f:
    f.write(theorem_tex.strip() + '\n')

intro = """---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Exercise 5.7.9 from Sachs and Wu characterizes spatial isotropy in terms of direction-independence on the spatial sphere, proves the timelike convergence condition for the stress-energy tensor, and establishes the equivalence between a spatially isotropic photon gas and a rest-mass zero perfect fluid with pressure equal to one-third the energy density."""
with open(os.path.join(d, 'introduce.en.md'), 'w') as f:
    f.write(intro + '\n')

print('Done exercise 5.7.9')
print('All exercise concepts now have full v8 format files.')
