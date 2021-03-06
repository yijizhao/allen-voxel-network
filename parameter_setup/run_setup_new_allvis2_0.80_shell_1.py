import os

save_stem='new_allvis_0.80_shell_1'
lambda_list=np.logspace(-3,5,10)**2
scale_lambda=True
min_vox=5
# save_file_name='visual_output.hdf5'
source_coverage=0.80
source_shell=1
save_dir=os.path.join('../connectivities',save_stem)
data_dir='../../pull_new_data/data_all'
experiments_fn=None
source_acronyms=['VISp','VISal','VISam','VISpm','VISpl']
#source_acronyms=['VISp']
target_acronyms=['VISp', 'VISal', 'VISpm', 'VISam', 'VISpl']
#target_acronyms=['VISal','VISam','VISpm','VISpl']
solver=os.path.abspath('../smoothness_c/solve')
cmdfile=os.path.join(save_dir,'model_fitting_cmds')
selected_fit_cmds=os.path.join(save_dir,'model_fitting_after_selection_cmds')
save_mtx=True
cross_val_matrices=True
cross_val=5
fit_gaussian=False
select_one_lambda=False
if select_one_lambda:
    lambda_fn='lambda_opt'
else:
    lambda_fn='lambda_ipsi_contra_opt'
