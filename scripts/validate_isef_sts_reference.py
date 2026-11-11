#!/usr/bin/env python3
"""Validate the proposed reference edition using Python's standard library.

No network, writes, external packages, or private preservation inputs are used.
Run from a standalone overlay, or use --integrated in the destination repository.
These are mechanical checks, not external audit or publication authorization.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit, parse_qsl, unquote

PREFIX = 'datasets/isef-sts-reference/v1.0-rc3'
COMMIT = '72b2128d8dfb68f2eed099dc50b0024c2de87fa3'
RULE_VERSION = 'VISIBILITY_REFERENCE_GATE_2026-11-09_v2'
APPROVED_PUBLIC_PB_COHORT = '53612b7d2a6c24f4bbe3adbd869961d3e9e7569b3ba35c8134c1a8cd4e314a03'
APPROVED_PUBLIC_ASSET_COHORT = 'f80c3c06a6de405e3e66e151d0e1b13e052d6b4ff07a1ff8a50178b6d3184dce'
CONTRACT = {
 'scientific_projects': ('scientific_project_id identity_basis', 'scientific_project_id'),
 'project_records': ('project_record_id scientific_project_id identity_status','project_record_id'),
 'competition_appearances': ('appearance_id project_record_id competition year participation_status category_state award_state title_state entrant_state','appearance_id'),
 'collection_memberships': ('collection_id appearance_id source_record_id','collection_id appearance_id source_record_id'),
 'source_records': ('source_record_id appearance_id namespace original_identifier source_url cited_source_url capture_version link_status','source_record_id'),
 'aliases': ('namespace external_id appearance_id source_record_id link_status','namespace external_id'),
 'assertions': ('assertion_id appearance_id source_record_id field source_state export_state verification_status','assertion_id'),
 'preferred_assertions': ('appearance_id field assertion_id','appearance_id field'),
 'awards': ('award_assertion_id appearance_id assertion_id sequence segmentation_status amount currency award_level description_export_state','award_assertion_id'),
 'annotations': ('annotation_id appearance_id source_record_id annotation_kind text claim_status attribution_id','annotation_id'),
 'asset_fingerprints': ('sha256 bytes mime_type availability','sha256'),
 'asset_occurrences': ('occurrence_id appearance_id projectboard_id sha256 artifact_type source_url identity_status','occurrence_id'),
 'corrections': ('correction_id appearance_id field preferred_assertion_id old_assertion_id prior_value_state corrected_value_state evidence_url','correction_id'),
 'unresolved_issues': ('issue_id appearance_id field issue_type disposition','issue_id'),
 'project_identity_links': ('from_project_record_id to_project_record_id relationship evidence_status','from_project_record_id to_project_record_id'),
}
NULLABLE = {'scientific_project_id','cited_source_url','old_assertion_id','amount','currency','award_level'}
FIELDS = set('abstract award_program_flags awards booth category category_code cited_source_url competition_level country entrants location partner_data_sources partner_lesson partner_methods partner_relevance partner_summary partner_tags province school state title'.split())
ANNOTATIONS = set('partner_data_sources partner_lesson partner_methods partner_tags'.split())
HOSTS = set('abstracts.societyforscience.org github.com investor.regeneron.com isef.net newsroom.regeneron.com societyforscience.org sspcdn.blob.core.windows.net www.intc.com www.prnewswire.com www.regeneron.com www.science.columbia.edu www.sciencenews.org www.societyforscience.org'.split())
SOURCE_STATES = {'PRESENT','MISSING_NULL','MISSING_EMPTY'}
PRESENCE = {'NO_SOURCE_ASSERTION','MISSING_IN_SOURCE','PRESENT_VALUE_WITHHELD'}
LINK_STATES = set('SOURCE_IDENTITY_SUPPORTED VERIFIED_YEAR_BOOTH_AND_ABSTRACT UNIQUE_YEAR_BOOTH_LINK_TITLE_VARIANT VERIFIED_YEAR_BOOTH_AND_TITLE EXACT_ABSTRACT_YEAR_LINK_BOOTH_DIFFERENCE PRIMARY_PERSON_EVENT_CORROBORATED'.split())
SHA = re.compile(r'^[0-9a-f]{64}$')

def require(ok, message):
 if not ok: raise ValueError(message)

def digest(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def decode(text):
 for _ in range(3):text=unquote(text)
 return text

def check_url(value):
 require(isinstance(value,str),'URL type')
 u=urlsplit(decode(value))
 require(u.scheme=='https' and u.hostname in HOSTS and not u.username and not u.password and u.port in (None,443),'Unapproved public URL')
 require(not re.search(r'/(?:login|signin|account|private)(?:/|$)',u.path,re.I),'Private URL path')
 require(not any(re.search(r'token|secret|signature|credential|password|auth|session|api.?key|^sig$',k,re.I) for k,v in parse_qsl(u.query)),'Sensitive URL query')

def scan_text(text):
 text=decode(text)
 patterns=[r'(?:file|smb)://',r'/(?:'+'Users'+r'|home)/[^\s/]+/',r'\.co'+'dex/',r'-----BEGIN [A-Z ]*PRIVATE KEY-----',r'\bgh[pousr]_[A-Za-z0-9]{20,}',r'\bAKIA[A-Z0-9]{16}\b',r'(?i)\b(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)\s*[=:]\s*[A-Za-z0-9_/-]{8,}']
 require(not any(re.search(x,text) for x in patterns),'Potential private content or credential')

def validate_rows(data, metadata):
 require(set(data)==set(CONTRACT),'Table allowlist')
 indices={}
 for name,rows in data.items():
  columns,pk=(x.split() for x in CONTRACT[name]);seen={};previous=None
  for r in rows:
   require(set(r)==set(columns),'Unexpected or missing column: '+name)
   for k,v in r.items():
    if v is None:require(k in NULLABLE or (name=='unresolved_issues' and k=='field'),'Unexpected NULL: '+name+'.'+k)
    elif k in ('bytes','year','sequence'):require(type(v) is int,'Expected integer: '+name+'.'+k)
    else:require(isinstance(v,str),'Expected string: '+name+'.'+k)
   key=tuple(str(r[k]) for k in pk)
   require(key not in seen,'Duplicate primary key: '+name)
   require(previous is None or previous<key,'Noncanonical row order: '+name)
   seen[key]=r;previous=key
  indices[name]=seen
 require({k:len(v) for k,v in data.items()}==metadata['counts'],'Count metadata reconciliation')
 require(metadata['publication_authorized'] is False and metadata['bulk_payload_files']==0,'Publication boundary')
 require(metadata['pinned_azaan_commit']==COMMIT,'Pinned source commit')
 require(not data['scientific_projects'] and not data['project_identity_links'],'Unadjudicated project-family merge')
 pr={r['project_record_id']:r for r in data['project_records']}
 apps={r['appearance_id']:r for r in data['competition_appearances']}
 require(len(pr)==len(apps)==17667,'Appearance/project-record count')
 require(Counter(r['competition'] for r in apps.values())=={'ISEF':17563,'STS':104},'Competition counts')
 for r in pr.values():require(r['scientific_project_id'] is None and r['identity_status']=='SOURCE_SCOPED_MENTION_NOT_A_DISTINCT_PROJECT_CLAIM','False scientific identity')
 for eid,r in apps.items():
  require(r['project_record_id']=='PROJECT:'+eid and r['project_record_id'] in pr,'Appearance-project reference')
  require((r['competition']=='ISEF' and eid.startswith('ISEF:SOCIETY:')) or (r['competition']=='STS' and eid.startswith('STS:')),'Source-scoped appearance identifier')
  require(1900<=r['year']<=2100,'Competition year')
  require(r['participation_status']=='SOURCE_RECORDED_COMPETITION_ENTRY','Participation claim')
  require(r['award_state'] in {'NOT_RECORDED_IN_BASE_SOURCE','SOURCE_ASSERTION_PRESENT'},'Missing award inference')
  require(all(r[k] in PRESENCE for k in ('category_state','title_state','entrant_state')),'Missing or withheld state')
 sources={r['source_record_id']:r for r in data['source_records']}
 for rid,r in sources.items():
  require(r['appearance_id'] in apps and r['link_status'] in LINK_STATES,'Source appearance crosswalk')
  require(r['namespace'] in {'native','azaan','pb','sts-proof','correction'} and rid.startswith(r['namespace']+':'),'Source namespace')
  check_url(r['source_url'])
  if r['cited_source_url'] is not None:check_url(r['cited_source_url'])
  if r['namespace']=='azaan':require(COMMIT in r['source_url'] and r['capture_version']==COMMIT,'Unpinned curated source')
 def same_source(row):
  require(row['appearance_id'] in apps,'Dangling appearance reference')
  require(row['source_record_id'] in sources,'Dangling source reference')
  require(sources[row['source_record_id']]['appearance_id']==row['appearance_id'],'Source belongs to a different appearance')
 for name in ('collection_memberships','aliases','assertions','annotations'):
  for row in data[name]:same_source(row)
 membership=Counter(x['collection_id'] for x in data['collection_memberships'])
 require(membership=={'HISTORICAL_ISEF_SOURCE':17563,'AZAAN_CURATED_ISEF_STS':433},'Broad/curated collection counts')
 mem={r['source_record_id']:r['appearance_id'] for r in data['collection_memberships']}
 require(len(mem)==17996,'Duplicate collection source membership')
 require(len({r['appearance_id'] for r in data['collection_memberships'] if r['collection_id']=='AZAAN_CURATED_ISEF_STS'})==433,'Duplicate curated appearances')
 aliases={}
 for r in data['aliases']:
  require(r['namespace'] in {'society_abstract','azaan_repository','projectboard'} and r['link_status'] in LINK_STATES,'Alias evidence status')
  aliases[r['namespace'],r['external_id']]=r
 for r in data['assertions']:
  require(r['field'] in FIELDS and r['source_state'] in SOURCE_STATES,'Assertion field/state')
  require(r['verification_status'] in {'ATTRIBUTED_PARTNER_CLAIM','EXPLICIT_PARTNER_INFERENCE','AUTHENTICATED_SOURCE_CLAIM','REVIEWED_SOURCE_SUPPORTED'},'Unreviewed assertion promotion')
  require(r['export_state'] in {'LICENSED_ANNOTATION_SEPARATE_TABLE','NO_VALUE_IN_SOURCE','VALUE_WITHHELD_REFERENCE_EDITION'},'Public value policy')
  require((r['source_state']!='PRESENT')==(r['export_state']=='NO_VALUE_IN_SOURCE'),'Missing/present value semantics')
  if r['source_record_id'] in mem:require(mem[r['source_record_id']]==r['appearance_id'],'Source assigned to different appearance')
 assertions={r['assertion_id']:r for r in data['assertions']}
 preferred={}
 for r in data['preferred_assertions']:
  a=assertions.get(r['assertion_id']);require(a is not None and (a['appearance_id'],a['field'])==(r['appearance_id'],r['field']),'Dangling or inconsistent preferred assertion')
  preferred[r['appearance_id'],r['field']]=r['assertion_id']
 for r in data['annotations']:
  require(r['annotation_kind'] in ANNOTATIONS and r['source_record_id'].startswith('azaan:'),'Annotation source/field')
  require(r['attribution_id']=='AZAAN_CC_BY_4_0','Annotation attribution')
  expected='EXPLICIT_INFERENCE_NOT_VERIFIED' if 'likely' in r['text'].lower() else 'ATTRIBUTED_ANALYSIS_NOT_VERIFIED_FACT'
  require(r['claim_status']==expected,'Unverified annotation promoted to fact')
  a=assertions.get(r['annotation_id']);require(a is not None and a['appearance_id']==r['appearance_id'] and a['source_record_id']==r['source_record_id'] and a['field']==r['annotation_kind'] and a['export_state']=='LICENSED_ANNOTATION_SEPARATE_TABLE','Annotation assertion reference')
  scan_text(r['text'])
 require(Counter(r['annotation_kind'] for r in data['annotations'])=={'partner_methods':429,'partner_data_sources':194,'partner_tags':358,'partner_lesson':67},'Reviewed annotation inclusion')
 require({r['annotation_id'] for r in data['annotations']}=={r['assertion_id'] for r in data['assertions'] if r['export_state']=='LICENSED_ANNOTATION_SEPARATE_TABLE'},'Annotation state crosswalk')
 sequences=set()
 for r in data['awards']:
  a=assertions.get(r['assertion_id']);require(a is not None and a['appearance_id']==r['appearance_id'] and a['field']=='awards' and a['source_state']=='PRESENT','Award source assertion')
  require(r['sequence']>0 and (r['assertion_id'],r['sequence']) not in sequences,'Duplicate award sequence');sequences.add((r['assertion_id'],r['sequence']))
  require(all(r[k] is None for k in ('amount','currency','award_level')) and r['description_export_state']=='WITHHELD_THIRD_PARTY_AWARD_TEXT','Invented or copied award value')
  require(r['segmentation_status'] in {'UNSEGMENTED_SOURCE_TEXT','EXPLICIT_PIPE_DELIMITER'},'Award segmentation')
 fingerprints={r['sha256']:r for r in data['asset_fingerprints']};used=set()
 for h,r in fingerprints.items():require(SHA.fullmatch(h) and r['bytes']>0 and r['availability']=='SOURCE_PROJECT_LINK_ONLY_NO_PAYLOAD','Asset fingerprint')
 for r in data['asset_occurrences']:
  require(r['appearance_id'] in apps and r['sha256'] in fingerprints,'Asset reference')
  a=aliases.get(('projectboard',r['projectboard_id']));require(a is not None and a['appearance_id']==r['appearance_id'] and a['link_status']==r['identity_status'],'Asset identity crosswalk')
  require(r['source_url']=='https://isef.net/project/'+r['projectboard_id'],'Asset public source link');check_url(r['source_url']);used.add(r['sha256'])
  require(r['artifact_type'] in {'presentations','quad_charts','supplementary_presentations'},'Asset type')
 require(used==set(fingerprints),'Unlinked fingerprint')
 require(len(data['asset_occurrences'])==31950,'Asset occurrence reconciliation')
 require({r['correction_id'] for r in data['corrections']}=={'C001','C002','C003','C004','C005'},'Correction count')
 for r in data['corrections']:
  require(preferred.get((r['appearance_id'],r['field']))==r['preferred_assertion_id'],'Correction not preferred')
  a=assertions.get(r['old_assertion_id']) if r['old_assertion_id'] else None
  require(r['old_assertion_id'] is None or (a and a['appearance_id']==r['appearance_id']),'Correction original reference')
  check_url(r['evidence_url'])
 for r in data['unresolved_issues']:
  require(r['appearance_id'] in apps,'Issue appearance reference')
  require(r['disposition'] in {'LINK_WITH_EXPLICIT_CORROBORATION_LIMIT','PRESERVE_NULL_WITH_REASON','PRESERVE_SOURCE_LABELS; CANONICAL_TAXONOMY_UNRESOLVED'},'Unresolved issue disposition')
 # Positive commitments contain only retained public records, not excluded identifiers.
 def cohort(rows,key):
  raw=''.join(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n' for r in sorted(rows,key=key))
  return hashlib.sha256(raw.encode()).hexdigest()
 gate=metadata.get('visibility_gate',{})
 require(gate.get('rule_version')==RULE_VERSION and gate.get('restricted_or_unverified_references_included')==0,'Visibility gate metadata')
 require(gate.get('payload_redistribution_permission_claimed') is False,'Unsupported payload permission claim')
 require(cohort([r for r in data['source_records'] if r['namespace']=='pb'],lambda r:r['source_record_id'])==APPROVED_PUBLIC_PB_COHORT==gate.get('projectboard_source_cohort_sha256'),'Unapproved ProjectBoard source cohort')
 require(cohort(data['asset_occurrences'],lambda r:r['occurrence_id'])==APPROVED_PUBLIC_ASSET_COHORT==gate.get('asset_occurrence_cohort_sha256'),'Unapproved asset reference cohort')
 require(len(data['unresolved_issues'])==2501,'Corrected source-specific issue scope')
 return {'schema_and_keys':True,'referential_integrity':True,'project_identity':True,'collections_and_overlap':True,'source_and_annotation_status':True,'missing_values_and_awards':True,'asset_provenance':True,'approved_visibility_cohorts':True,'correction_provenance':True,'unresolved_issues':True}

def load_dataset(root):
 schema=json.loads((root/PREFIX/'schema.json').read_text());data={};paths=[]
 require(set(schema['tables'])==set(CONTRACT),'Schema table allowlist')
 for name,definition in schema['tables'].items():
  columns,pk=(x.split() for x in CONTRACT[name]);require(definition['columns']==columns and definition['primary_key']==pk,'Schema column/key contract')
  data[name]=[]
  for n,p in enumerate(definition['files'],1):
   require(p==PREFIX+'/data/'+name+'-'+str(n).zfill(3)+'.jsonl','Nonallowlisted table file')
   file=root/p;require(file.is_file() and not file.is_symlink(),'Missing or symlinked data file');paths.append(p)
   with file.open() as f:
    lines=0
    for line in f:
     r=json.loads(line);require(line==json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n','Noncanonical JSON row')
     data[name].append(r);lines+=1
   require(lines<=40000,'Oversized data chunk')
  require(bool(definition['files']),'Missing empty-table file')
 return data,json.loads((root/PREFIX/'RELEASE_METADATA.json').read_text()),paths

def validate_coverage(root,data,metadata):
 import csv
 from decimal import Decimal, ROUND_HALF_UP
 columns=['competition','year','artifact_type','baseline_references','retained_references','withheld_references','retention_percent','withheld_percent','restricted_references','unverified_audience_references','unverified_parent_references']
 path=root/PREFIX/'COVERAGE.csv'
 with path.open(newline='') as f:
  reader=csv.DictReader(f);require(reader.fieldnames==columns,'Coverage columns');rows=list(reader)
 apps={r['appearance_id']:r for r in data['competition_appearances']}
 competitions=sorted({r['competition'] for r in apps.values()});years=sorted({r['year'] for r in apps.values()});types=['presentations','quad_charts','supplementary_presentations']
 expected={(c,y,t) for c in competitions for y in years for t in types};seen=set();totals=Counter();byyear={};bytype={};year2025=Counter()
 actual=Counter((apps[a['appearance_id']]['competition'],apps[a['appearance_id']]['year'],a['artifact_type']) for a in data['asset_occurrences'])
 def percentage(n,d):return '' if d==0 else format((Decimal(n)*100/Decimal(d)).quantize(Decimal('0.000001'),rounding=ROUND_HALF_UP),'f')
 for r in rows:
  for name in ['year','baseline_references','retained_references','withheld_references','restricted_references','unverified_audience_references','unverified_parent_references']:
   value=int(r[name]);require(value>=0 and str(value)==r[name],'Coverage nonnegative canonical integer');r[name]=value
  key=(r['competition'],r['year'],r['artifact_type']);require(key in expected and key not in seen,'Coverage cell identity');seen.add(key)
  b,k,w=r['baseline_references'],r['retained_references'],r['withheld_references']
  require(b==k+w and w==r['restricted_references']+r['unverified_audience_references']+r['unverified_parent_references'],'Coverage reference partition')
  require(k==actual[key],'Coverage actual retained references')
  require(r['retention_percent']==percentage(k,b) and r['withheld_percent']==percentage(w,b),'Coverage denominator/rounding')
  names=['baseline_references','retained_references','withheld_references','restricted_references','unverified_audience_references','unverified_parent_references']
  nums={n:r[n] for n in names};totals.update(nums);byyear.setdefault(r['year'],Counter()).update(nums);bytype.setdefault(r['artifact_type'],Counter()).update(nums)
  if r['year']==2025:year2025.update(nums)
 require(seen==expected and len(rows)==84,'Coverage complete competition/year/type grid')
 require([totals[k] for k in ['baseline_references','retained_references','withheld_references']]==[54706,31950,22756],'Coverage global reconciliation')
 require([totals[k] for k in ['restricted_references','unverified_audience_references','unverified_parent_references']]==[9108,13636,12],'Coverage reason partition')
 require([year2025[k] for k in ['baseline_references','retained_references','withheld_references','restricted_references','unverified_audience_references']]==[16190,502,15688,2052,13636],'Coverage2025 explanation')
 cov=metadata['coverage'];require(cov['coverage_csv_sha256']==digest(path),'Coverage file identity')
 require(cov['counts']==dict(totals),'Coverage metadata totals')
 for field,groups,label in [('by_year',byyear,'year'),('by_artifact_type',bytype,'artifact_type')]:
  require(len(cov[field])==len(groups),'Coverage summary group count')
  for r in cov[field]:
   v=groups[r[label]];require(all(r[k]==v[k] for k in v),'Coverage summary counts')
   require(r['retention_percent']==(percentage(v['retained_references'],v['baseline_references']) or None) and r['withheld_percent']==(percentage(v['withheld_references'],v['baseline_references']) or None),'Coverage summary percentages')
 require(cov['unit']=='ASSET_REFERENCE_OCCURRENCE' and cov['baseline_is_full_private_archive'] is False and cov['zero_denominator_percentage']=='CSV empty; JSON null; documentation N/A','Coverage denominator semantics')
 return {'coverage_counts_and_denominators':True,'coverage_complete_year_type_grid':True,'coverage2025_reason_partition':True,'coverage_matches_retained_data':True}


def validate(root,integrated=False):
 root=Path(root).resolve();data,metadata,paths=load_dataset(root)
 results=validate_rows(data,metadata)
 results.update(validate_coverage(root,data,metadata))
 expected=set(paths)|{PREFIX+'/'+x for x in ['README.md','ATTRIBUTION.md','SOURCE_RIGHTS.md','PUBLIC_EXPORT_POLICY.json','RELEASE_METADATA.json','schema.json','COVERAGE.csv']}|{'scripts/validate_isef_sts_reference.py','.github/workflows/validate-isef-sts-reference.yml'}
 manifests={}
 for line in (root/'PUBLIC_CANDIDATE_SHA256SUMS.txt').read_text().splitlines():
  h,p=line.split('  ',1);require(SHA.fullmatch(h) and p not in manifests,'Manifest record');require(not PurePosixPath(p).is_absolute() and '..' not in PurePosixPath(p).parts,'Manifest path traversal');manifests[p]=h
 require(set(manifests)==expected,'Manifest allowlist')
 actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
 required=expected|{'PUBLIC_CANDIDATE_SHA256SUMS.txt'}
 require(required<=actual,'Missing public file')
 require({p for p in actual if p.startswith(PREFIX+'/')}=={p for p in required if p.startswith(PREFIX+'/')},'Unexpected dataset content')
 if not integrated:require(actual==required,'Unexpected standalone overlay file')
 for p,h in manifests.items():
  f=root/p;require(not f.is_symlink() and digest(f)==h,'SHA-256 mismatch: '+p)
  scan_text(f.read_text())
  if p.endswith('.md'):require('<!-- BEGIN '+'GENERATED:' not in f.read_text(),'Legacy generator marker in new document')
 results.update({'file_allowlist':True,'sha256_manifest':True,'actual_file_privacy_patterns':True,'legacy_generator_isolation':True})
 return {'pass':True,'checks':results,'counts':metadata['counts'],'files':len(required),'mode':'integrated' if integrated else 'standalone'}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--integrated',action='store_true');args=ap.parse_args()
 print(json.dumps(validate(args.root,args.integrated),indent=2))

if __name__=='__main__':main()
