# import csv
# import os
# import random
# import pandas


def dis_list3(text_path, train_rate=0.8):

    # The division of the training and test sets is randomly based on an 8 to 2 ratio.
    # The numbers in the list are the serial numbers corresponding to the images, and the serial numbers corresponding to the three datasets are also given.
    # win5
    train_dis = [2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 32, 33, 34, 35, 37, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 60, 61, 62, 63, 64, 65, 68, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 88, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 110, 111, 112, 113, 115, 116, 117, 118, 119, 124, 125, 128, 129, 131, 132, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 152, 154, 155, 156, 157, 158, 159, 160, 162, 163, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 183, 184, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 198, 199, 200, 201, 202, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 217, 219, 220]
    test_dis = [1, 3, 12, 24, 30, 31, 36, 38, 42, 50, 57, 58, 59, 66, 67, 69, 70, 75, 87, 89, 96, 103, 109, 114, 120, 121, 122, 123, 126, 127, 130, 133, 134, 151, 153, 161, 164, 181, 182, 185, 197, 203, 216, 218]

    # NBU
    # train_dis = [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 79, 80, 82, 83, 84, 85, 87, 88, 89, 91, 94, 95, 96, 97, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 128, 129, 131, 132, 134, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 154, 155, 157, 158, 160, 161, 163, 166, 167, 168, 169, 170, 171, 172, 173, 174, 176, 177, 178, 179, 180, 181, 182, 183, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 199, 200, 201, 202, 203, 204, 205, 206, 207, 209, 210] 
    # test_dis = [2, 6, 14, 21, 29, 35, 45, 47, 54, 63, 64, 77, 78, 81, 86, 90, 92, 93, 98, 101, 110, 112, 114, 125, 126, 127, 130, 133, 135, 151, 152, 153, 156, 159, 162, 164, 165, 175, 184, 185, 198, 208]

    # SHU
    # train_dis = [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 65, 66, 68, 69, 70, 71, 72, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 86, 87, 88, 89, 94, 95, 97, 98, 99, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 113, 114, 115, 116, 117, 119, 120, 124, 125, 126, 127, 128, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 142, 143, 144, 145, 146, 147, 148, 149, 152, 154, 155, 156, 157, 158, 159, 160, 162, 163, 166, 167, 168, 169, 171, 172, 174, 175, 176, 177, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 197, 198, 199, 200, 201, 203, 204, 205, 206, 207, 209, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 235, 236, 237, 239]
    # test_dis = [2, 6, 14, 21, 22, 29, 35, 45, 54, 63, 64, 67, 73, 74, 82, 90, 91, 92, 93, 96, 105, 107, 112, 118, 121, 122, 123, 129, 141, 150, 151, 153, 161, 164, 165, 170, 173, 178, 179, 195, 196, 202, 208, 210, 233, 234, 238, 240]

    return train_dis, test_dis
