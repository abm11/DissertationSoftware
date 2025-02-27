import networkx as nx
# GRAPH FROM PAPER
# Graph Nodes
graph1 = nx.DiGraph(name="Graph 1")
# Graph edges
graph1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 21), (0, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 21),
                      (0, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18,19), (19, 20), (20, 21)])
# Graph node activities
graph1.nodes[0]['Activity'] = 'DUMMY'
graph1.nodes[1]['Activity'] = 'DUMMY'
graph1.nodes[2]['Activity'] = 'DUMMY'
graph1.nodes[3]['Activity'] = 'DUMMY'
graph1.nodes[4]['Activity'] = 'DUMMY'
graph1.nodes[5]['Activity'] = 'DUMMY'
graph1.nodes[6]['Activity'] = 'DUMMY'
graph1.nodes[7]['Activity'] = 'DUMMY'
graph1.nodes[8]['Activity'] = 'DUMMY'
graph1.nodes[9]['Activity'] = 'DUMMY'
graph1.nodes[10]['Activity'] = 'DUMMY'
graph1.nodes[11]['Activity'] = 'DUMMY'
graph1.nodes[12]['Activity'] = 'DUMMY'
graph1.nodes[13]['Activity'] = 'DUMMY'
graph1.nodes[14]['Activity'] = 'DUMMY'
graph1.nodes[15]['Activity'] = 'DUMMY'
graph1.nodes[16]['Activity'] = 'DUMMY'
graph1.nodes[17]['Activity'] = 'DUMMY'
graph1.nodes[18]['Activity'] = 'DUMMY'
graph1.nodes[19]['Activity'] = 'DUMMY'
graph1.nodes[20]['Activity'] = 'DUMMY'
graph1.nodes[21]['Activity'] = 'DUMMY'

nx.write_yaml(graph1, str(graph1)+".YAML")
########################################################################################################################
# GRAPH FROM PAPER
graph2 = nx.DiGraph(name="Graph 2")

# Graph edges
graph2.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 21), (0, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 21),
                      (0, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18,19), (19, 20), (20, 21), (2, 9), (4, 11), (12, 7), (15, 9), (17, 11)])
# Graph node activities
graph2.nodes[0]['Activity'] = 'DUMMY'
graph2.nodes[1]['Activity'] = 'DUMMY'
graph2.nodes[2]['Activity'] = 'DUMMY'
graph2.nodes[3]['Activity'] = 'DUMMY'
graph2.nodes[4]['Activity'] = 'DUMMY'
graph2.nodes[5]['Activity'] = 'DUMMY'
graph2.nodes[6]['Activity'] = 'DUMMY'
graph2.nodes[7]['Activity'] = 'DUMMY'
graph2.nodes[8]['Activity'] = 'DUMMY'
graph2.nodes[9]['Activity'] = 'DUMMY'
graph2.nodes[10]['Activity'] = 'DUMMY'
graph2.nodes[11]['Activity'] = 'DUMMY'
graph2.nodes[12]['Activity'] = 'DUMMY'
graph2.nodes[13]['Activity'] = 'DUMMY'
graph2.nodes[14]['Activity'] = 'DUMMY'
graph2.nodes[15]['Activity'] = 'DUMMY'
graph2.nodes[16]['Activity'] = 'DUMMY'
graph2.nodes[17]['Activity'] = 'DUMMY'
graph2.nodes[18]['Activity'] = 'DUMMY'
graph2.nodes[19]['Activity'] = 'DUMMY'
graph2.nodes[20]['Activity'] = 'DUMMY'
graph2.nodes[21]['Activity'] = 'DUMMY'

nx.write_yaml(graph2, str(graph2)+".YAML")
########################################################################################################################
#Graph Nodes
GENS1 = nx.DiGraph(name="GENS1")
#Graph edges
GENS1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14),
(2, 19), (19, 20), (20, 14), (2, 16), (16, 17), (17, 18), (18, 14), (9, 21), (21, 14), (11, 23), (23, 14), (12, 22), (22, 14), (1, 15), (15, 14),
(12, 22), (22, 14), (1, 15), (15, 14)])
#Set yes/no edge labels
attrs = {(2, 19): {'choice': 'Yes'}, (2, 16): {'choice': 'Yes'}, (2, 3): {'choice': 'No'}, (2, 16): {'choice': 'Yes'},
         (11, 12): {'choice': 'Yes'}, (11, 23): {'choice': 'No'}}
nx.set_edge_attributes(GENS1, attrs)
# Graph node activities
GENS1.nodes[0]['Activity'] = 'Faeces samples processed as per PR2062 and associated process map as standard of care.'
GENS1.nodes[1]['Activity'] = 'Sample worklist prepared by either:•	WinPath worklists searched for known positive samples•	Selection of samples with suggestive clinical details•	NEQAS•	Spiking known culture negative stools with bacterial targets'
GENS1.nodes[2]['Activity'] = 'Any indication sample High Risk?'
GENS1.nodes[3]['Activity'] = 'Samples located in B floor walk in fridge'
GENS1.nodes[4]['Activity'] = 'Class 1 safety cabinet is cleaned with Trigene followed by DNAzap'
GENS1.nodes[5]['Activity'] = '1mL STAR buffer to a sterile molecular grade microcentrifuge tube.  Add 100uL liquid stool or rice sized portion if solid.  Vortex for 1 min'
GENS1.nodes[6]['Activity'] = 'Incubate for 15 min at RT, vortex after ~7 min and at 15 min.'
GENS1.nodes[7]['Activity'] = 'Centrifuge for 2 min at 6500rpm.'
GENS1.nodes[8]['Activity'] = 'Allow to stand at RT for 5 min'
GENS1.nodes[9]['Activity'] = 'Transfer 500uL of supernatant into a new a sterile molecular grade microcentrifuge tube.'
GENS1.nodes[10]['Activity'] = 'Store remaining buffer/stool mixtures in a rack inside a sealed container until PCR proves no CL3 pathogen present.'
GENS1.nodes[11]['Activity'] = 'PCR shows sample contains CL3 pathogen?'
GENS1.nodes[12]['Activity'] = 'Transfer sealed box into CL3 and dispose of samples in sharps bin.'
GENS1.nodes[13]['Activity'] = 'Disinfect transport box and rack with 10% distil before removal back into CL2'
GENS1.nodes[14]['Activity'] = 'ENDED'
GENS1.nodes[15]['Activity'] = 'For spiked stools include on current worklist – follow ENS2 process map.'
GENS1.nodes[16]['Activity'] = '1.	Cysticercosis1.	Cysticercosis\n2.	HUS\n3.	Paratyphi disease\n4.	Positive Widal test' \
                              '\n5.	Pyrexia &travel to typhoid endemic area\n6.	Typhoid Fever\n7.	Contact with E.coli 0157' \
                              '\n8.	Contact/ previous positive with Salm Typhi / Paratyphi' \
                              '\n9.	Contact/ previous positive with Shigella dysenteriae'

GENS1.nodes[17]['Activity'] = 'Samples located in CL3'
GENS1.nodes[18]['Activity'] = 'Process as per methods but within Cat 3 facility – follow ENS3 process map.'
GENS1.nodes[19]['Activity'] = '1.	Hydatid disease\n2.	Cysticercosis\n3.	Contact with Echinococcus' \
                              '\n4.	Contact / previous positive with Taenia solium' \
                              '\n5.	Patient with TB\n6.	Mycobacterium tuberculosis'

GENS1.nodes[20]['Activity'] = 'Do not include in this pathway'
GENS1.nodes[21]['Activity'] = 'Supernatants ready for use on the EasyMag'
GENS1.nodes[22]['Activity'] = 'Dispose using CL3 route'
GENS1.nodes[23]['Activity'] = 'Dispose using CL2 route'

nx.write_yaml(GENS1, str(GENS1)+".YAML")
########################################################################################################################
#Graph Nodes
GENS2 = nx.DiGraph(name="GENS2")
#Graph edges
GENS2.add_edges_from([(0, 1), (0, 7), (1, 2), (2, 3), (3, 4), (4, 6), (4, 5), (5, 16), (6, 8), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 14), (12, 13), (13, 16), (14, 15), (15, 16)])
# Graph node activities
GENS2.nodes[0]['Activity'] = 'START'
GENS2.nodes[1]['Activity'] = 'Culture negative stools spiked with CL2 pathogens from ENS1'
GENS2.nodes[2]['Activity'] = 'CL2 pathogen from -80 stocks inoculated onto CLED, incubated O2 for 24h'
GENS2.nodes[3]['Activity'] = 'Locate large volume culture negative stool and aliquot 0.5mL into a sterile microcentrifuge tube.'
GENS2.nodes[4]['Activity'] = 'Select 1 – 2 well isolated colonies and inoculate the stool using a swirling motion to mix the sample'
GENS2.nodes[5]['Activity'] = 'Freeze at -20°C for future use on BD Max'
GENS2.nodes[6]['Activity'] = 'Use sample preparation on the same day for EasyMag extraction'
GENS2.nodes[7]['Activity'] = 'Class 1 safety cabinet is cleaned with Trigene followed by DNAzap'
GENS2.nodes[8]['Activity'] = '1mL STAR buffer to a sterile molecular grade microcentrifuge tube.  Add 100uL liquid stool or rice sized portion if solid.  Vortex for 1 min'
GENS2.nodes[9]['Activity'] = 'Incubate for 15 min at room temperature, vortex after ~7 min and at 15 min.'
GENS2.nodes[10]['Activity'] = 'Centrifuge for 2 min at 6500rpm.'
GENS2.nodes[11]['Activity'] = 'Allow to stand at RT for 5 min'
GENS2.nodes[12]['Activity'] = 'Transfer 500uL of supernatant into a new a sterile molecular grade microcentrifuge tube.'
GENS2.nodes[13]['Activity'] = 'Supernatants ready for use on the EasyMag'
GENS2.nodes[14]['Activity'] = 'Dispose of remaining buffer/stool mixtures in bio-bin'
GENS2.nodes[15]['Activity'] = 'Dispose using CL2 route'
GENS2.nodes[16]['Activity'] = 'END'

nx.write_yaml(GENS2, str(GENS2)+".YAML")
########################################################################################################################

#Graph Nodes
GENS3 = nx.DiGraph(name="GENS3")
#Graph edges
GENS3.add_edges_from([(0, 1), (0, 18), (1, 2), (2, 3), (3, 4), (4, 6), (4, 5),(5, 19), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (12, 15), (13, 14),  (14, 19), (15, 16), (16,17), (17, 19), (18,7)])
# Graph node activities
GENS3.nodes[0]['Activity'] = 'START'
GENS3.nodes[1]['Activity'] = 'Culture negative stools spiked with CL3 pathogens'
GENS3.nodes[2]['Activity'] = 'CL3 pathogen inoculated onto CLED, incubated O2 for 24h'
GENS3.nodes[3]['Activity'] = 'Locate large volume culture negative stool and aliquot 0.5mL into a sterile microcentrifuge tube.'
GENS3.nodes[4]['Activity'] = 'Select 1 – 2 well isolated colonies and inoculate the stool using a swirling motion to mix the sample'
GENS3.nodes[5]['Activity'] = 'Freeze at -20°C for future use on BD Max'
GENS3.nodes[6]['Activity'] = 'Use sample preparation on the same day for EasyMag extraction'
GENS3.nodes[7]['Activity'] = 'Class 1 safety cabinet is cleaned with Trigene followed by DNAzap'
GENS3.nodes[8]['Activity'] = '1mL STAR buffer to a sterile molecular grade microcentrifuge tube.  Add 100uL liquid stool or rice sized portion if solid.  Vortex for 1 min'
GENS3.nodes[9]['Activity'] = 'Incubate for 15 min at 70°C, vortex after ~7 min and at 15 min.'
GENS3.nodes[10]['Activity'] = 'Centrifuge for 2 min at 6500rpm.'
GENS3.nodes[11]['Activity'] = 'Allow to stand at RT for 5 min'
GENS3.nodes[12]['Activity'] = 'Transfer 500uL of supernatant into a new a sterile molecular grade microcentrifuge tube.'
GENS3.nodes[13]['Activity'] = 'Dispose of remaining buffer/stool mixtures in sharps bin'
GENS3.nodes[14]['Activity'] = 'Dispose using CL3 route'
GENS3.nodes[15]['Activity'] = 'Supernatants ready for use on the EasyMag, place into sealed box'
GENS3.nodes[16]['Activity'] = 'Disinfect transport box and rack with 10% distil before removal back into CL2'
GENS3.nodes[17]['Activity'] = 'Transfer sealed box into CL2. Use supernatants on EasyMag'
GENS3.nodes[18]['Activity'] = 'Isolates identified as high-risk from ENS1'
GENS3.nodes[19]['Activity'] = 'END'

nx.write_yaml(GENS3, str(GENS3)+".YAML")
########################################################################################################################

#Graph Nodes
GPM1 = nx.DiGraph(name="GPM1")
#Graph edges
GPM1.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (3, 9), (4, 5), (4, 8), (5, 6), (6, 7), (6, 8), (7, 11), (8, 11), (9, 10), (10, 11)])
# Graph node activities
GPM1.nodes[0]['Activity'] ='Faeces / perianal swabs / artefacts arrive in reception placed in plastic box'
GPM1.nodes[1]['Activity'] = 'Box sealed and transported from reception through corridors on A-floor / up internal stairs to Enterics'
GPM1.nodes[2]['Activity'] ='MLA staff check specimen details against request and code sample'
GPM1.nodes[3]['Activity'] ='Any indication sample High Risk'
GPM1.nodes[4]['Activity'] ='Inpatient'
GPM1.nodes[5]['Activity'] ='From SRU ESSU/AMU/B3ED/LJU/CAU NG2/C31/D57 Toghill or Fletcher wards'
GPM1.nodes[6]['Activity'] ='Check on NOTIS Is date of admission greater than 3 days'
GPM1.nodes[7]['Activity'] ='Code for C diff only +extras (no culture) and follow C diff process'
GPM1.nodes[8]['Activity'] ='Follow routine Process'
GPM1.nodes[9]['Activity'] ='Transfer to Cat 3 in High risk transport box.'
GPM1.nodes[10]['Activity'] ='Process as per methods but within Cat 3 facility – C.diff separate method'
GPM1.nodes[11]['Activity'] ='END'

nx.write_yaml(GPM1, str(GPM1)+".YAML")
########################################################################################################################

#Graph Nodes
GPM2 = nx.DiGraph(name="GPM2")
#Graph edges
GPM2.add_edges_from([(0, 1), (1, 2), (1, 13), (1, 17), (1, 18), (1, 31), (2, 3), (3, 4), (4, 5), (4, 6), (5, 51), (6, 7), (6, 8), (7, 51), (8, 9), (9, 10), (9, 11), (10,12),
(11, 12), (12, 51), (13, 14), (14, 15), (15, 16), (16, 51), (17, 15), (18, 19), (19, 20), (20, 21), (21, 22), (21, 26), (22, 23), (23, 24), (24, 25), (25, 51),
(26, 27), (27, 28), (27, 29), (28, 51), (29, 30), (30, 51), (31, 32), (32, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39),(39, 40), (39, 41), (40, 51),
(41, 42), (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 48), (48, 49), (49, 50), (50, 51)])
#Set yes/no edge labels
attrs = {(4, 6): {'choice': 'Yes'}, (4, 5): {'choice': 'No'},
         (6, 8): {'choice': 'Yes'}, (6, 7): {'choice': 'No'},
         (9, 10): {'choice': 'Yes'}, (9, 11): {'choice': 'No'},
         (21, 26): {'choice': 'Yes'}, (21, 22): {'choice': 'No'},
         (27, 29): {'choice': 'Yes'}, (27, 28): {'choice': 'No'},
         (39, 41): {'choice': 'Yes'}, (39, 40): {'choice': 'No'},
         (49, 50): {'choice': 'POS'}}
nx.set_edge_attributes(GPM2, attrs)
# Graph node activities
GPM2.nodes[0]['Activity'] = 'Check sample not leaked – unbag and label sample & consumables then transfer into the safety cabinet. If leaking transfer to safety cabinet before un-bagging.'
GPM2.nodes[1]['Activity'] = 'Transfer 1g of faeces to 5ml ringers and vortex'
GPM2.nodes[2]['Activity'] = 'Inoculate ¼ CCDA and incubate MO2 for 48hrs'
GPM2.nodes[3]['Activity'] = 'Suspicious grey/white colonies'
GPM2.nodes[4]['Activity'] = 'Oxidase Positive'
GPM2.nodes[5]['Activity'] = 'Discard into plate tin'
GPM2.nodes[6]['Activity'] = 'Carbol fuchsin stain (G-ve curved bacilli'
GPM2.nodes[7]['Activity'] = 'Discard into plate tin'
GPM2.nodes[8]['Activity'] = 'Typical morphology'
GPM2.nodes[9]['Activity'] = 'In-patient?'
GPM2.nodes[10]['Activity'] = 'Perform EUCAST'
GPM2.nodes[11]['Activity'] = 'Report '
GPM2.nodes[12]['Activity'] = 'Stored 7 days in cold room then discarded in plate tin'
GPM2.nodes[13]['Activity'] = 'Decant 1ml suspension to Selenite broth incubate in O2 for 24 hrs'
GPM2.nodes[14]['Activity'] = 'Subculture to XLD & incubate in O2 for 24hrs'
GPM2.nodes[15]['Activity'] = 'Suspicious colonies\n1.	Pink colony (black centre)\n2.	Pink colony (oxidase negative)'
GPM2.nodes[16]['Activity'] = 'Follow appropriate process Map'
GPM2.nodes[17]['Activity'] = 'Inoculate ½ XLD and incubate in O2 for 24hrs'
GPM2.nodes[18]['Activity'] = 'Inoculate ½ CTSMAC and incubate in O2 for 24hrs'
GPM2.nodes[19]['Activity'] = 'Sorbitol negative, oxidase negative colonies on CTSMAC'
GPM2.nodes[20]['Activity'] = 'Transfer to Cat 3 B-floor Safety Cabinet in sealed box'
GPM2.nodes[21]['Activity'] = 'Transfer to Cat 3 B-floor Safety Cabinet in sealed box'
GPM2.nodes[22]['Activity'] = 'If Clinical details HUS then faeces sent to ref lab'
GPM2.nodes[23]['Activity'] = '1 x package in plastic HaysDx box. Decontaminate outside with 10% distil'
GPM2.nodes[24]['Activity'] = 'Transfer into cardboard outer box in CL2 (HaysDx box)'
GPM2.nodes[25]['Activity'] = 'Hays DX box transferred to bag outside micro reception.'
GPM2.nodes[26]['Activity'] = 'Subculture to chromogenic 0157 media incubate in O2 @37C for 24hrs'
GPM2.nodes[27]['Activity'] = 'Mauve colonies'
GPM2.nodes[28]['Activity'] = 'Discarded in plate tin CL3'
GPM2.nodes[29]['Activity'] = 'Make 2x NA slope & incubate 02 for 24hrs'
GPM2.nodes[30]['Activity'] = '1 x slope transfer to locked cabinet CL3 B Floor. Discard when ref lab report is completed'
GPM2.nodes[31]['Activity'] = 'Air dry suspension on to a Multispot slide '
GPM2.nodes[32]['Activity'] = 'Fix in Methanol for 3 mins'
GPM2.nodes[33]['Activity'] = 'Stain in Auramine phenol for 15 mins'
GPM2.nodes[34]['Activity'] = 'Wash in tap water'
GPM2.nodes[35]['Activity'] = 'Decolourise in acid/alcohol for 10 secs'
GPM2.nodes[36]['Activity'] = 'Wash in tap water'
GPM2.nodes[37]['Activity'] = 'Stain in Thiazine Red for 2 mins'
GPM2.nodes[38]['Activity'] = 'Air Dry & read on UV Microscope'
GPM2.nodes[39]['Activity'] = 'Positive'
GPM2.nodes[40]['Activity'] = 'Store Sample'
GPM2.nodes[41]['Activity'] = 'ZN Process Map'
GPM2.nodes[42]['Activity'] = 'Air dry suspension on to slide (medium thickness)'
GPM2.nodes[43]['Activity'] = 'Fix in Methanol for 3 mins'
GPM2.nodes[44]['Activity'] = 'Stain in cold Carbol fuchsin for 10 mins'
GPM2.nodes[45]['Activity'] = 'Wash in tap water'
GPM2.nodes[46]['Activity'] = 'Decolourise in 1% HCL for 10 seconds'
GPM2.nodes[47]['Activity'] = 'Wash in tap water'
GPM2.nodes[48]['Activity'] = 'Counterstain in 0.4% malachite green for 30 secs'
GPM2.nodes[49]['Activity'] = 'Read on Microscope'
GPM2.nodes[50]['Activity'] = 'Send original faeces to Ref lab in HaysDx box & report (CRY)'
GPM2.nodes[51]['Activity'] = 'END'

nx.write_yaml(GPM2, str(GPM2)+".YAML")
########################################################################################################################

GPM3 = nx.DiGraph(name="GPM3")
#Graph edges
GPM3.add_edges_from([(0, 1), (0,5), (0,16), (0,20), (0,29), (0,33), (0,42), (0,44), (1,2), (2,3), (3,4), (4,51), (5,6),
                    (6,7), (7,8), (8,9), (9,10), (9,11), (10, 51), (11,12), (11,13), (12,13), (13,14), (13,15), (14,51), (15,51), (16,17),
                    (17,18), (18,19), (19,51), (20,21), (21,22), (22,23), (23,24), (24,25), (25,26), (26,27), (27,28), (27,28), (28,51), (29,30), (30,31),
                    (31,32), (32,51), (33,34), (34,35), (35,36), (36,37), (37,38), (38,39), (38,40), (39,51), (40,41), (41,51), (42,43), (43,51),
                    (44,45), (45,46), (46,47), (47,48), (48,49), (48,50), (49,51), (50,51)])
#Set yes/no edge labels
attrs = {(48, 49): {'choice': 'Neg'}, (48, 50): {'choice': 'Pos'},
         (11, 12): {'choice': 'and'},
         (16, 18): {'choice': 'Cholera endemic area'}}
nx.set_edge_attributes(GPM3, attrs)
# Graph node activities
GPM3.nodes[0]['Activity'] = 'START'
GPM3.nodes[1]['Activity'] = 'Liquid sample from GP / Outpatient'
GPM3.nodes[2]['Activity'] = 'Direct Wet prep '
GPM3.nodes[3]['Activity'] = 'Read on microscope for parasites'
GPM3.nodes[4]['Activity'] = 'Report and discard slide in Sharps bin'
GPM3.nodes[5]['Activity'] = 'Consumption of sea Food/water sports '
GPM3.nodes[6]['Activity'] = 'Inoculate a TCBS and INCUBATE in O2 at 37°C for 24hrs'
GPM3.nodes[7]['Activity'] = 'Suspicious colonies (Yellow/Green)'
GPM3.nodes[8]['Activity'] = 'Purity to NA plate and incubate in O2 at 37°C for 24hrs'
GPM3.nodes[9]['Activity'] = 'Oxidase positive'
GPM3.nodes[10]['Activity'] = 'Oxidase negative Discard in tin'
GPM3.nodes[11]['Activity'] = 'API 20E      (use saline)'
GPM3.nodes[12]['Activity'] = 'Agglutinate with 01 & 0139 antisera'
GPM3.nodes[13]['Activity'] = 'If Vibrio save on NAx1 and bead at -80°C'
GPM3.nodes[14]['Activity'] = 'Report & store plate'
GPM3.nodes[15]['Activity'] = 'Package in HaysDx box and transfer to reception bag'
GPM3.nodes[16]['Activity'] = 'Foreign travel'
GPM3.nodes[17]['Activity'] = 'Inoculate MAC INCUBATE in O2 at 37°C for 24hrs'
GPM3.nodes[18]['Activity'] = 'Lactose negative, oxidase negative'
GPM3.nodes[19]['Activity'] = 'Follow process map'
GPM3.nodes[20]['Activity'] = 'Request OCP / Diarrhoea >2 weeks'
GPM3.nodes[21]['Activity'] = '1g of faeces into Parasep'
GPM3.nodes[22]['Activity'] = 'Add 2ml ethyl acetate and mix'
GPM3.nodes[23]['Activity'] = 'Invert sealed parasep and centrifuge 1200g for 3 mins'
GPM3.nodes[24]['Activity'] = 'Unscrew and discard mixing chamber in Biobin'
GPM3.nodes[25]['Activity'] = 'Loosen fat plug and decant liquid into dedicated bottle in BSC. Replace lid'
GPM3.nodes[26]['Activity'] = 'Mix deposit and make  thin slide prep'
GPM3.nodes[27]['Activity'] = 'Read on Microscope & discard slide in sharps bin'
GPM3.nodes[28]['Activity'] = 'Discard Paraseps into Biobin on bench'
GPM3.nodes[29]['Activity'] = 'Appendicitis / Arthritis/ mesenteric adenitis'
GPM3.nodes[30]['Activity'] = 'Direct inoculation of CIN agar Incubate in O2 at 30°Cfor 48hrs'
GPM3.nodes[31]['Activity'] = 'Suspicious bullseye colony'
GPM3.nodes[32]['Activity'] = 'MALDI-TOFF ID'
GPM3.nodes[33]['Activity'] = 'Children <5yrs or If requested and immunosuppressed/mesenteric adenitis/ outbreak'
GPM3.nodes[34]['Activity'] = 'Add 0.1g of faeces to extraction vial'
GPM3.nodes[35]['Activity'] = 'Vortex for 10 seconds'
GPM3.nodes[36]['Activity'] = 'Break off tip of vial'
GPM3.nodes[37]['Activity'] = 'Add 4 drops to Rota / adeno kit'
GPM3.nodes[38]['Activity'] = 'Incubate at RT for 10 minutes and read'
GPM3.nodes[39]['Activity'] = 'Discard into sharps bin'
GPM3.nodes[40]['Activity'] = 'If Rota +ve retrieve faeces and package in HaysDx box '
GPM3.nodes[41]['Activity'] = 'Transfer to bag outside reception'
GPM3.nodes[42]['Activity'] = 'Transfer to bag outside reception'
GPM3.nodes[43]['Activity'] = 'Norovirus Process '
GPM3.nodes[44]['Activity'] = 'C.diff if:\n1. Requested\n2. Inpatient >16yrs\n3. GP >65yrs\n4. Post antibiotics' \
                             '\n5. Pseudomembranous colitis'
GPM3.nodes[45]['Activity'] = 'Add 400ul GDH reagent + 100ul of faeces in Cryovial'
GPM3.nodes[46]['Activity'] = 'Centrifuge 5000g for 10 mins'
GPM3.nodes[47]['Activity'] = 'Transported in closed box DS2(VSM)'
GPM3.nodes[48]['Activity'] = 'Review GDH result'
GPM3.nodes[49]['Activity'] = 'Report and store sample'
GPM3.nodes[50]['Activity'] = 'GDH Positive Process Map'
GPM3.nodes[51]['Activity'] = 'END'

nx.write_yaml(GPM3, str(GPM3)+".YAML")
########################################################################################################################