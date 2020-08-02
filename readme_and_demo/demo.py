import os
# import cPickle as pkl
import _pickle as pkl
import numpy as np
import render_model
from smpl.smpl_webuser.serialization import load_model
import cv2

def renderImage(model,img_path,camPose,camIntrinsics):

    img = cv2.imread(img_path)
    class cam:
        pass
    cam.rt = cv2.Rodrigues(camPose[0:3,0:3])[0].ravel()
    cam.t = camPose[0:3,3]
    cam.f = np.array([camIntrinsics[0,0],camIntrinsics[1,1]])
    cam.c = camIntrinsics[0:2,2]
    h = int(2*cam.c[1])
    w = int(2*cam.c[0])
    im = (render_model.render_model(model, model.f, w, h, cam, img= img)* 255.).astype('uint8')
    return im

if __name__ == '__main__':
    seq_name = 'courtyard_basketball_00'
    datasetDir = '../sequenceFiles/train'
    file = os.path.join(datasetDir,'sequenceFiles',seq_name+'.pkl')
    seq = pkl.load(open(file,'rb'))

    models = list()
    for iModel in range(0,len(seq['v_templates'])):
        if seq['genders'][iModel] == 'm':
            model = load_model("smpl/models/basicmodel_m_lbs_10_207_0_v1.0.0.pkl")
        else:
            model = load_model("smpl/models/basicModel_f_lbs_10_207_0_v1.0.0.pkl")

        model.betas[:10] = seq['betas'][iModel][:10]
        models.append(model)

    iModel = 0
    iFrame = 25
    if seq['campose_valid'][iModel][iFrame]:
        models[iModel].pose[:] = seq['poses'][iModel][iFrame]
        models[iModel].trans[:] = seq['trans'][iModel][iFrame]
        img_path = os.path.join(datasetDir,'imageFiles',seq['sequence']+'/image_{:05d}.jpg'.format(iFrame))
        im = renderImage(models[iModel],img_path,seq['cam_poses'][iFrame],seq['cam_intrinsics'])
        cv2.imshow('3DPW Example',im)
        cv2.waitKey(0)
        cv2.waitKey(False)
        cv2.destroyAllWindows()
