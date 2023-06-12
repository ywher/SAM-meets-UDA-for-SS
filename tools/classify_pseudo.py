import os
import shutil
import tqdm


def classify_pseudo_city(path_root):
    #get all the file names in the path_root
    images = os.listdir(path_root)
    #根据图片名称第一个下划线前的字符作为城市名进行分类
    city_names = []
    for img_name in images:
        city_name = img_name.split('_')[0]
        if city_name not in city_names:
            city_names.append(city_name)
    print('Get city names successfully!')
    
    #创建城市文件夹
    for city_name in city_names:
        city_folder = os.path.join(path_root, city_name)
        if not os.path.exists(city_folder):
            os.mkdir(city_folder)
    print('Create city folders successfully!')
    
    #将图片移动到对应的城市文件夹
    bar = tqdm.tqdm(total=len(images))
    for img_name in images:
        image_path = os.path.join(path_root, img_name)
        shutil.move(image_path, os.path.join(path_root, img_name.split('_')[0], img_name))
        bar.update(1)
    bar.close()
    print('Done!')
    
def change_img_suffix(dataset_path, original_suffix, new_suffix):
    folders = os.listdir(dataset_path)
    for folder in folders:
        print(folder, 'begin')
        images = os.listdir(os.path.join(dataset_path, folder))
        for image in images:
            image_path = os.path.join(dataset_path, folder, image)
            shutil.move(image_path, image_path.replace(original_suffix, new_suffix))
            
def change_img_suffix2(dataset_path, original_suffix, new_suffix):
    # folders = os.listdir(dataset_path)
    # for folder in folders:
        # print(folder, 'begin')
    images = os.listdir(dataset_path)
    for image in images:
        image_path = os.path.join(dataset_path, image)
        shutil.move(image_path, image_path.replace(original_suffix, new_suffix))
    

def main(path_root, original_suffix, new_suffix):
    # classify_pseudo_city(path_root)
    change_img_suffix2(path_root, original_suffix, new_suffix)

if __name__ == '__main__':
    # path_root = '/media/ywh/1/yanweihao/dataset/cityscapes_original/gtFine_trainvaltest/gtFine/train_pseudo_syn'
    # path_root = '/media/ywh/1/yanweihao/projects/uda/MIC/seg/data/acdc/gt/train_pseudo'
    path_root = '/media/ywh/1/yanweihao/projects/uda/MIC/seg/work_dirs/local-basic/230509_1455_gtaHR2csHR_mic_hrda_s2_108c1/pred_trainid'
    original_suffix = '_leftImg8bit_trainID.png'
    new_suffix = '_gtFine_labelTrainIds.png'
    main(path_root, original_suffix, new_suffix)