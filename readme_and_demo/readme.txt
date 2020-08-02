
3DPW Dataset
============

The 3DPW dataset contains several motion sequences, which are organized into two folders: imageFiles and sequenceFiles.
The folder imageFiles contains the RGB-images for every sequence. 
The folder sequenceFiles provides synchronized motion data and SMPL model parameters in the form of .pkl-files. For each sequence, the .pkl-file contains a dictionary with the following fields:
- sequence: String containing the sequence name
- betas: SMPL shape parameters for each actor which has been used for tracking (List of 10x1 SMPL beta parameters)
- poses: SMPL body poses for each actor aligned with image data (List of Nx72 SMPL joint angles, N = #frames)
- trans: tranlations for each actor aligned with image data (List of Nx3 root translations)
- poses_60Hz: SMPL body poses for each actor at 60Hz (List of Nx72 SMPL joint angles, N = #frames)
- trans_60Hz: tranlations for each actor at 60Hz (List of Nx3 root translations)
- betas_clothed: SMPL shape parameters for each clothed actor (List of 10x1 SMPL beta parameters)
- v_template_clothed: 
- gender: actor genders (List of strings, either 'm' or 'f')
- texture_maps: texture maps for each actor
- poses2D: 2D joint detections in Coco-Format for each actor (only provided if at least 6 joints were detected correctly)
- jointPositions: 3D joint positions of each actor (List of Nx(24*3) XYZ coordinates of each SMPL joint)
- img_frame_ids: an index-array to down-sample 60 Hz 3D poses to corresponding image frame ids
- cam_poses: camera extrinsics for each image frame (Ix4x4 array, I frames times 4x4 homegenous rigid body motion matrices)
- campose_valid: a boolean index array indicating which camera pose has been aligned to the image
- cam_intrinsics: camera intrinsics (K = [f_x 0 c_x;0 f_y c_y; 0 0 1])

Each sequence has either one or two models, which corresponds to the list size of the model specific fields (e.g. betas, poses, trans, v_template, gender, texture_maps, jointPositions, poses2D). 
SMPL poses and translations are provided at 30 Hz. They are aligned to image dependent data (e.g. 2D poses, camera poses). In addition we provide 'poses_60Hz' and 'trans_60Hz' which corresponds to the recording frequency of 60Hz of the IMUs . You could use the 'img_frame_ids' to downsample and align 60Hz 3D and image dependent data, wich has been done to compute SMPL 'poses' and 'trans' variables. 
Please refer to the demo.py-file for loading a sequence, setup smpl-Models and camera, and to visualize an example frame.
