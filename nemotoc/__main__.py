import optparse 
def genConf():
    parse=optparse.OptionParser(usage='"Usage:nemotocGen --getConf"')  
    parse.add_option('-g','--getConf',dest='getConf', type=int, help='if generate configure file. 1:yes/0:no')  
    parse.set_defaults(g=1) 
    options,args=parse.parse_args()
    if options.getConf:
        print('generate configure file')
        f = open('conf.py', 'a+')
        print('import numpy as np', file = f)
        print('import os', file = f)
        print('', file = f)
        print('from nemotoc.polysome_class.polysome import Polysome', file = f)
        print('', file = f)
        print('#####BASIC PARAMTERS SETTING########', file = f)
        print("input_star =  'data/all_particles_neuron_warp.star' #the star", file = f)
        print("project_folder = 'cluster-all_particles_neuron_warp' #the folder to store all runs.", file = f)
        print("run_time = 'threshold20_relink01percent' #the folder storing the results of each run", file = f) 
        print('pixel_size = 3.42 #in Ang, the pixel size of input starfile', file = f)
        print('particle_radius = 50*pixel_size #in Ang, the radius of the input particle', file = f)
        print('cluster_threshold = 20 #the threshold to cut-off the dendrogram tree for clustering', file = f) 
        print('minNumTransform_ratio = 0.01  #select clusters with at least minNumTransformRatio transforms. -1:keep any cluster regardless of the #transforms', file = f)
        print('remove_branches = 0 #1:branch removal; 0:switch off', file = f)
        print('average_particles = 1 #average particles from each cluster. 1:switch on, 0:switch off', file = f)
        print('search_radius = particle_radius*2 #in Ang. The searching range for neighbors. Two neighbors will be linked within this range.', file = f)
        print('', file = f)
        print('#####PREPROCESS PARAMETERS####', file = f)
        print('min_dist = particle_radius/pixel_size #in pixeles, the minmum distance to remove repeat particles', file = f)
        print('if_stopgap = 0 #if input a stopgap starfile, then transfer into relion2. 0:input is not stopgap file type', file = f) 
        print("subtomo_path = 'subtomograms' #if input is stopgap file, need specify the path pointing to subtomograms", file = f) 
        print("ctf_file =  'miss30Wedge.mrc' #if input is stopgap file, need specify the missing wedge file", file = f) 
        print('', file = f)
        print('####PARALLEL COMPUTATION PARAMETERS####', file = f)
        print('cpuN = 15 #number of CPU for parallel computation. 1:switch off parallel computation', file = f)
        print('gpu_list = None  #leave None if no gpu available. Else offer gpuID list like [0]//[0,1]', file = f)
        print('avg_cpuN = 35 #the number of CPUs when average particles by relion if average_particles == 1', file = f)
        print('', file = f)
        print('#####VISUAL PARAMETERS######', file = f)
        print("vectorfield_plotting = 'basic' #advance:show detailed information of polysomes in the vector field figure", file = f)
        print('show_longestPoly = 1 #plot and save the longest polysome in each cluster 0:switch off', file = f)
        print('', file = f)
        print('#####AVERAGE PARAMETERS#####', file = f)
        print('if_avg = 1  #if average particles 0:switch off', file = f) 
        print('avg_pixS = 3.42  #the pixel size of particles for relion averaging', file = f)
        print('avg_minPart = 50 #the minmual number of particles requirement for average of each cluster', file = f)
        print('avg_maxRes = 20 #the maximum resolution for relion averaging', file = f)
        print('avg_callByPython = 0 #if use python to call relion_reconstruct command 0: generate linux scripts to run relion_reconstruct, 1:use python to call relion', file = f)
        print('                     #if set to 1, you should make sure the relion_reconstruct command is searchable in the system pathway', file = f)
        print('', file = f)              
        print('#####ADVANCED PARAMETERS SETTING######', file = f)
        print('link_depth = 2 #the searching depth for linking adjacent transforms into longer polysomes. 0:remove branches', file = f)
        print('fillUpPoly_addN = 1 #number of particles added in each tail of polysome to fill up gaps   0:switch off filling up step', file = f)
        print("fillUpPoly_model = 'lognorm' #the type of fitted distribution for filling up step(genFit:based on experimental data; lognorm:base on lognorm model; max:no model fitting)", file = f)
        print('fillUpPoly_threshold = 0.05 #threshold to accept filled up particles. The smaller, the more convinced of accepted interpolated particles', file = f) 
        print('', file = f)
        print('', file = f)
        print('def runPoly(input_star, run_time, project_folder, pixel_size, min_dist, if_stopgap, subtomo_path, ctf_file,', file = f)
        print('            search_radius, link_depth, cluster_threshold, minNumTransform_ratio, fillUpPoly, cpuN, gpu_list, remove_branches,', file = f) 
        print('            vectorfield_plotting, show_longestPoly, if_avg, average_particles, avg):', file = f)
        print('    #check the type of input parameters', file = f) 
        print('    assert isinstance(input_star, str)', file = f)
        print('    assert isinstance(run_time, str)', file = f)
        print('    assert isinstance(project_folder, str)', file = f)
        print('    assert isinstance(pixel_size, (int, float))', file = f)
        print('    assert isinstance(min_dist, (int, float))', file = f)
        print('    assert isinstance(if_stopgap, (int, float))', file = f)
        print('    assert isinstance(subtomo_path, str)', file = f)
        print('    assert isinstance(ctf_file, str)', file = f)
        print('    assert isinstance(search_radius, (int, float))', file = f)
        print('    assert isinstance(link_depth, (int, float))', file = f)
        print('    assert isinstance(cluster_threshold, (int, float))', file = f)
        print('    assert isinstance(minNumTransform_ratio, (int, float))', file = f)
        print('    assert isinstance(fillUpPoly, dict)', file = f)
        print('    assert isinstance(cpuN, int)', file = f)
        print('    assert isinstance(gpu_list, (list, type(None)))', file = f)
        print('    assert isinstance(remove_branches, int)', file = f)
        print('    assert isinstance(vectorfield_plotting, str)', file = f)  
        print('    assert isinstance(show_longestPoly, int)', file = f)
        print('    assert isinstance(if_avg, (int, float))', file = f)
        print('    assert isinstance(average_particles, int)', file = f)
        print('    assert isinstance(avg, dict)', file = f)
        print('    #check if the project_folder exist', file = f)
        print('    if not os.path.exists(project_folder):', file = f)
        print('        os.mkdir(project_folder)', file = f)
        print('', file = f)            
        print('    polysome1 = Polysome(input_star = input_star, run_time = run_time)', file = f)
        print('    #calculate transformations', file = f)
        print("    polysome1.transForm['pixS'] = pixel_size", file = f) 
        print("    polysome1.transForm['maxDist'] = search_radius", file = f) 
        print("    polysome1.transForm['branchDepth'] = link_depth", file = f)
        print('    #do clustering and filtering', file = f)
        print("    polysome1.classify['clustThr'] = cluster_threshold", file = f)
        print("    polysome1.sel[0]['minNumTransform'] = minNumTransform_ratio", file = f)
        print('', file = f)       
        print('    polysome1.creatOutputFolder()  #create folder to store the result', file = f)
        print('    polysome1.preProcess(if_stopgap, subtomo_path, ctf_file, min_dist) #preprocess', file = f)   
        print('    polysome1.calcTransForms(worker_n = cpuN) #calculate transformations', file = f)
        print('    polysome1.groupTransForms(worker_n = cpuN, gpu_list = gpu_list)  #cluster transformations', file = f) 
        print('    transListSel, selFolds = polysome1.selectTransFormClasses() #filter clusters', file = f) 
        print('    polysome1.genOutputList(transListSel, selFolds) #save the filtered clusters', file = f) 
        print('    polysome1.alignTransforms() #align the transformationsto the same direction', file = f)
        print("    polysome1.analyseTransFromPopulation('','',1, 0)  #summary the clusters but w/o any polysome information", file = f)       
        print('    polysome1.fillPoly = fillUpPoly #fill up the gaps', file = f) 
        print('    polysome1.link_ShortPoly(remove_branches, cpuN) #link transforms into a long linear chain', file = f)
        print("    polysome1.analyseTransFromPopulation('','',0, 1) #summary the clusters", file = f)     
        print('    polysome1.noiseEstimate() #estimate the purity of each cluster', file = f)
        print('', file = f)    
        print("    polysome1.vis['vectField']['type'] = vectorfield_plotting", file = f)
        print("    polysome1.vis['longestPoly']['render'] = show_longestPoly", file = f)
        print('    polysome1.visResult()', file = f)   
        print('    polysome1.visLongestPoly()', file = f)
        print('', file = f)      
        print('    #average particles subset using relion_reconstruct', file = f)
        print('    if if_avg:', file = f)
        print('        polysome1.avg = avg', file = f)
        print('        polysome1.generateTrClassAverages()', file = f)
        print('', file = f)    
        print("if __name__ == '__main__': ", file = f)  
        print('', file = f)    
        print('    fillUpPoly = { }', file = f)
        print("    fillUpPoly['addNum'] = fillUpPoly_addN", file = f)
        print("    fillUpPoly['fitModel'] = fillUpPoly_model", file = f) 
        print("    fillUpPoly['threshold'] = fillUpPoly_threshold", file = f)
        print('', file = f)
        print('    avg = { }', file = f)
        print("    avg['filt'] = { }", file = f)
        print("    avg['filt']['minNumPart'] = avg_minPart", file = f) 
        print("    avg['filt']['maxNumPart'] = np.inf", file = f)
        print("    avg['pixS'] = avg_pixS", file = f)
        print("    avg['maxRes'] = avg_maxRes", file = f)
        print("    avg['cpuNr'] = avg_cpuN", file = f)
        print("    avg['callByPython'] = avg_callByPython", file = f)
        print('', file = f)   
        print('    runPoly(input_star, run_time, project_folder,', file = f) 
        print('            pixel_size, min_dist, if_stopgap, subtomo_path, ctf_file,', file = f) 
        print('            search_radius, link_depth, cluster_threshold,', file = f) 
        print('            minNumTransform_ratio, fillUpPoly, cpuN, gpu_list, remove_branches, vectorfield_plotting,', file = f) 
        print('            show_longestPoly, if_avg, average_particles, avg)', file = f) 
        print("    print('Successfully finish NEMO-TOC')", file = f)
        
        print('the generated configure file is named conf.py')
    else:
        print('no configure file will be generated')

if __name__ == '__main__': 
    genConf()
    
    
