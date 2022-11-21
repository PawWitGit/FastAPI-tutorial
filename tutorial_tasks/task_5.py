from typing import List

Image = List[List[int]]

def flatten_image(image: Image) -> List:
    flat_list = []
    for sublist in image:
        for item in sublist:
            flat_list.append(item)

    return flat_list


image = [[1,2,3],[4,5,6]]
print(flatten_image(image))