import cv2
import os


class CameraModel:

    def __init__(self, calib_dir: str) -> None:
        self._read_calib_files(calib_dir)

    def _read_calib_files(self, calib_dir: str) -> None:
        # check if files exist
        assert os.path.exists(calib_dir)
        cam0_intrinsics_file = os.path.join(calib_dir, 'cam0_intrinsics.xml')
        cam1_intrinsics_file = os.path.join(calib_dir, 'cam1_intrinsics.xml')
        cam0_distortion_file = os.path.join(calib_dir, 'cam0_distortion.xml')
        cam1_distortion_file = os.path.join(calib_dir, 'cam1_distortion.xml')
        assert all([os.path.exists(f) for f in [cam0_intrinsics_file, cam1_intrinsics_file, cam0_distortion_file, cam1_distortion_file]])

        # read intrinsics and distortion matrices from files
        fs = cv2.FileStorage(cam0_intrinsics_file, cv2.FILE_STORAGE_READ)
        self.cam0_intrinsics = fs.getNode('Intrinsics').mat()
        fs = cv2.FileStorage(cam1_intrinsics_file, cv2.FILE_STORAGE_READ)
        self.cam1_intrinsics = fs.getNode('Intrinsics').mat()
        fs = cv2.FileStorage(cam0_distortion_file, cv2.FILE_STORAGE_READ)
        self.cam0_distortion = fs.getNode('Distortion').mat()
        fs = cv2.FileStorage(cam1_distortion_file, cv2.FILE_STORAGE_READ)
        self.cam1_distortion = fs.getNode('Distortion').mat()

    def load_debayer_undistort(self, img_path: str):
        img = cv2.imread(img_path)
        img_debayered = cv2.cvtColor(img[:, :, 0], cv2.COLOR_BAYER_GB2RGB)
        if img_path.startswith('cam0_'):
            intrinsics = self.cam0_intrinsics
            distortion = self.cam0_distortion
        elif img_path.startswith('cam1_'):
            intrinsics = self.cam1_intrinsics
            distortion = self.cam1_distortion
        else:
            raise IOError(f'Could not process {img_path}, must start with cam0_ or cam1_')
        img_undistorted = cv2.undistort(img_debayered, intrinsics, distortion)
        return img_undistorted

    def undistort(self, img, cam: str):
        if cam == 'cam0':
            intrinsics = self.cam0_intrinsics
            distortion = self.cam0_distortion
        elif cam == 'cam1':
            intrinsics = self.cam1_intrinsics
            distortion = self.cam1_distortion
        else:
            raise IOError(f'cam should be cam0 or cam1')
        img_undistorted = cv2.undistort(img, intrinsics, distortion)
        return img_undistorted
