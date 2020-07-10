import os
import shutil
import paths_creating

train_dir = os.path.join(model_dir, 'train')
validation_dir = os.path.join(model_dir, 'validation')
test_dir = os.path.join(model_dir, 'test')

train_dir_c = os.path.join(train_dir, 'cyclone')
train_dir_e = os.path.join(train_dir, 'earthquake')
train_dir_f = os.path.join(train_dir, 'flood')
train_dir_w = os.path.join(train_dir, 'wildfire')

validation_dir_c = os.path.join(validation_dir, 'cyclone')
validation_dir_e = os.path.join(validation_dir, 'earthquake')
validation_dir_f = os.path.join(validation_dir, 'flood')
validation_dir_w = os.path.join(validation_dir, 'wildfire')

test_dir_c = os.path.join(test_dir, 'cyclone')
test_dir_e = os.path.join(test_dir, 'earthquake')
test_dir_f = os.path.join(test_dir, 'flood')
test_dir_w = os.path.join(test_dir, 'wildfire')


copy_images = False #False if images are already copied

if copy_images:

    # TRAIN

    names = ['{}.jpg'.format(i) for i in range(400)]
    for name in names:
        source = os.path.join(cyclone_dir, name)
        destination = os.path.join(train_dir_c, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(400)]
    for name in names:
        source = os.path.join(earthquake_dir, name)
        destination = os.path.join(train_dir_e, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(400)]
    for name in names:
        source = os.path.join(flood_dir, name)
        destination = os.path.join(train_dir_f, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(400)]
    for name in names:
        source = os.path.join(wildfire_dir, name)
        destination = os.path.join(train_dir_w, name)
        shutil.copyfile(source, destination)

    # VALIDATION

    names = ['{}.jpg'.format(i) for i in range(400, 500)]
    for name in names:
        source = os.path.join(cyclone_dir, name)
        destination = os.path.join(validation_dir_c, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(400, 500)]
    for name in names:
        source = os.path.join(earthquake_dir, name)
        destination = os.path.join(validation_dir_e, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(400, 500)]
    for name in names:
        source = os.path.join(flood_dir, name)
        destination = os.path.join(validation_dir_f, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(400, 500)]
    for name in names:
        source = os.path.join(wildfire_dir, name)
        destination = os.path.join(validation_dir_w, name)
        shutil.copyfile(source, destination)

    # TEST

    names = ['{}.jpg'.format(i) for i in range(500, 600)]
    for name in names:
        source = os.path.join(cyclone_dir, name)
        destination = os.path.join(test_dir_c, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(500, 600)]
    for name in names:
        source = os.path.join(earthquake_dir, name)
        destination = os.path.join(test_dir_e, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(500, 600)]
    for name in names:
        source = os.path.join(flood_dir, name)
        destination = os.path.join(test_dir_f, name)
        shutil.copyfile(source, destination)
    names = ['{}.jpg'.format(i) for i in range(500, 600)]
    for name in names:
        source = os.path.join(wildfire_dir, name)
        destination = os.path.join(test_dir_w, name)
        shutil.copyfile(source, destination)
