export const meta = {
  name: 'v7-extract-test',
  description: 'Test: extract concepts from GTM073 Chapter I in V7 format',
  phases: [{ title: 'Extract', detail: 'One agent extracts concepts from chapter into V7 staging format' }]
}

phase('Extract')

var chapter_file = '/home/a123/文档/mathpkg/pipeline_output/stitched/(GTM073)Algebra/06_CHAPTER_I.md'
var staging = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073/gtm-0073_ch01_concepts'

var result = await agent([
  '=== CONCEPT EXTRACTOR (V7 Format) ===',
  '',
  'Read the chapter text:',
  'Read ' + chapter_file,
  '',
  'Extract ALL mathematical concepts (theorems, definitions, lemmas, propositions, corollaries).',
  '',
  'For EACH concept, create a folder and write these files:',
  '',
  '1. concept.yaml with: id, title_en, title_zh (""), type (theorem|definition|lemma|proposition|corollary), domain (algebra), subdomain (group-theory), difficulty (basic), tags ([]), depends_on (required/recommended/suggested arrays), source_books array (gtm-0073, Hungerford, Algebra, ch I), content_hash (""), extraction_date (2026-06-24), extraction_agent (workflow-test)',
  '',
  '2. theorem.tex or definition.tex: PURE LaTeX statement. ZERO markdown. ZERO YAML. ZERO natural language. Example: "Let $G$ be a finite group, $H \\leq G$. Then $|H| \\mid |G|$."',
  '',
  '3. introduce.en.md: YAML frontmatter (role: introduce, locale: en, content_hash: "", written_against: "") then natural language description.',
  '',
  '4. For each proof: proof_gtm-0073_I_SECTION_TECHNIQUE.en.md with YAML frontmatter.',
  '',
  'CRITICAL RULES:',
  '- theorem.tex = PURE LaTeX ONLY. ZERO natural language.',
  '- All natural language goes in introduce.en.md',
  '- ONE concept per folder',
  '- Slug = title_en lowercased, hyphenated',
  '- depends_on = best guess at concept slugs from this chapter',
  '- Folder path: ' + staging + '/{slug}/',
  '- Extract at most 8 concepts for this test, focus on the most important group theory concepts',
  '',
  'Write .done file when complete: echo "DONE" > ' + staging + '/.done'
].join('\n'), {
  label: 'extract-gtm073-ch1',
  phase: 'Extract'
})

log('Done: ' + (result ? 'got output' : 'null'))
return { result_length: result ? result.length : 0 }
