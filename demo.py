from imagededup.methods import CNN

img_dir='tests/data/mixed_images'

cnn = CNN()
duplicates = cnn.find_duplicates(image_dir=img_dir, scores=True, min_similarity_threshold=0.9)

for img in duplicates:
    print(img + ':')
    for duplicate in duplicates[img]:
        print(duplicate[0] + ' (' + str(duplicate[1]) + ')')
    print('------------')
