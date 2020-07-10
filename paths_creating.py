import os

model_dir = r'C:\DisasterModel'

cyclone_dir = r'C:\DisasterModel\Cyclone_Wildfire_Flood_Earthquake_Database\cyclone'
earthquake_dir = r'C:\DisasterMode\Cyclone_Wildfire_Flood_Earthquake_Database\earthquake'
flood_dir = r'C:\DisasterModel\Cyclone_Wildfire_Flood_Earthquake_Database\flood'
wildfire_dir = r'C:\DisasterModel\Cyclone_Wildfire_Flood_Earthquake_Database\wildfire'

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

create_dirs = False  #False if path already exist

if create_dirs:
    os.mkdir(train_dir)
    os.mkdir(validation_dir)
    os.mkdir(test_dir)
    os.mkdir(train_dir_c)
    os.mkdir(train_dir_e)
    os.mkdir(train_dir_f)
    os.mkdir(train_dir_w)
    os.mkdir(validation_dir_c)
    os.mkdir(validation_dir_e)
    os.mkdir(validation_dir_f)
    os.mkdir(validation_dir_w)
    os.mkdir(test_dir_c)
    os.mkdir(test_dir_e)
    os.mkdir(test_dir_f)
    os.mkdir(test_dir_w)
