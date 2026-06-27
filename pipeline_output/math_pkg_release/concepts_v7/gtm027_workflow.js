export const meta = {
  name: 'v7-extract-gtm027',
  description: 'GTM027: 32 sections → concept extraction',
  phases: [{ title: 'Extract', detail: 'One agent per section' }]
}

var SECTIONS = ["/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s001_ACKNOWLEDGMENTS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s002_ALGEBRAIC_CONCEPTS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s003_TOPOLOGICAL_SPACES\n\nTOPOLOGIES_AND_NEIGHBORHOODS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s004_INTERIOR_AND_BOUNDARY.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s005_BASES_AND_SUBBASES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s006_E_KURATOWSKI_CLOSURE_AND_COMPLEMENT_PROBLEM.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s007_S_LOCALLY_CONNECTED_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s008_DIRECTED_SETS_AND_NETS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s009_SEQUENCES_AND_SUBSEQUENCES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s00_preface.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s010_PRODUCT_AND_QUOTIENT_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s011_QUOTIENT_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s012_PROBLEMS\n\nA_CONNECTED_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s013_S_TOPOLOGICAL_GROUPS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s014_U_FACTOR_GROUPS_AND_HOMOMORPHISMS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s015_EXISTENCE_OF_CONTINUOUS_FUNCTIONS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s016_B_CONTINUITY_OF_FUNCTIONS_ON_A_METRIC_SPACE.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s017_J_THE_SET_OF_ZEROS_OF_A_REAL_CONTINUOUS_FUNCTION.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s018_PRODUCTS_OF_COMPACT_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s019_LOCALLY_COMPACT_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s020_COMPACTIFICATION.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s021_G_PROBLEM_ON_LOCAL_COMPACTNESS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s022_N_EXAMPLES_ON_CLOSED_MAPS_AND_LOCAL_COMPACTNESS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s023_R_THE_WALLMAN_COMPACTIFICATION.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s024_V_POINT_FINITE_COVERS_AND_METACOMPACT_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s025_FOR_METRIC_SPACES_ONLY.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s026_F_THE_SUBBASE_THEOREM_FOR_TOTAL_BOUNDEDNESS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s027_J_UNIFORM_COVERING_SYSTEMS.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s028_FUNCTION_SPACES.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s029_COMPACT_OPEN_TOPOLOGY_AND_JOINT_CONTINUITY.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s030_F_CONTINUITY_OF_AN_INDUCED_MAP.md", "/home/a123/\u6587\u6863/mathpkg/pipeline_output/stitched_sections/(GTM027)General Topology( Kelley, John L.1975 )/s031_THE_CLASSIFICATION_AXIOM_SCHEME.md"]
var STAGING = '/home/a123/文档/mathpkg/pipeline_output/concepts_v7/gtm027'
var BOOK_SLUG = 'gtm027'

phase('Extract')
log(BOOK_SLUG + ': ' + SECTIONS.length + ' sections')

var results = await pipeline(SECTIONS, function(prev, sp) {
  return async function() {
    var sn = sp.split('/').pop().replace('.md','')
    var dd = STAGING + '/' + sn
    
    var prompt = '=== V7 CONCEPT EXTRACTOR (Per-Section) ===\n\n' +
      'READ: ' + sp + '\n\n' +
      'Extract EVERY theorem, definition, lemma, proposition, corollary, axiom.\n' +
      'For EACH concept, write 3 files in: ' + dd + '/{SLUG}/\n\n' +
      '1. concept.yaml: id,title_en,title_zh:"",type,domain,subdomain,difficulty,tags,depends_on,source_books,content_hash:"",extraction_date:"2026-06-25",extraction_agent:"v7-test"\n' +
      '2. theorem.tex: PURE LaTeX STATEMENT only. NO proof.\n' +
      '3. introduce.en.md: YAML frontmatter(role:introduce,locale:en,content_hash:"",written_against:"") + 2-4 English sentences.\n\n' +
      'CRITICAL: slug = semantic-english-lowercase-hyphen (kummers-theorem NOT ' + key.lower() + '-thm-3-2). ' +
      'source_books = array of OBJECTS. theorem.tex = ZERO natural language.\n\n' +
      'Write .done: echo DONE > ' + dd + '/.done\n' +
      'Write .fail if stuck: echo FAIL > ' + dd + '/.fail'
    
    try { await agent(prompt, { label: sn.substring(0,40), phase: 'Extract' }) } catch(e) {}
    
    // Count on disk
    var cnt = 0
    try {
      var cr = await agent(
        'python3 -c "import os; d=\'' + dd + '\'; print(len([x for x in os.listdir(d) if os.path.isdir(os.path.join(d,x))]) if os.path.exists(d) else 0)"',
        { label: 'cnt-'+sn.substring(0,25), phase: 'Extract' }
      )
      cnt = cr ? parseInt(cr.trim()) || 0 : 0
    } catch(e) {}
    
    return { section: sn.substring(0,50), concepts: cnt }
  }
})

var valid = results.filter(function(r) { return r !== null })
var total = valid.reduce(function(s, r) { return s + (r.concepts || 0) }, 0)
log(BOOK_SLUG + ': ' + total + ' concepts from ' + valid.length + '/' + SECTIONS.length + ' sections')
return { book: BOOK_SLUG, sections: SECTIONS.length, sections_done: valid.length, concepts: total }
