from PIL import Image
import os
def rea(path, pdf_name):
    file_list = os.listdir(path)
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)
    pic_name.sort()
    new_pic = []
    for x in pic_name:
        if "jpg" in x:
            new_pic.append(x)
    for x in pic_name:
        if "png" in x:
            new_pic.append(x)
    print("hec", new_pic)
    im1 = Image.open(os.path.join(path, new_pic[0]))
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open(os.path.join(path, i))
        # im_list.append(Image.open(i))
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)
    im1.save(pdf_name, "PDF", resolution=100.0,
             save_all=True, append_images=im_list)
    print("输出文件名称：", pdf_name)
if __name__ == '__main__':
    pdf_name = 'gracexxxxx.pdf'
    mypath = r"E:/workspace/grace/新建文件夹/kangjunru423-21-03-03-171630-9424/A4杂志册26P不覆膜_1853747924_"
    if ".pdf" in pdf_name:
        rea(mypath, pdf_name=pdf_name)
    else:
        rea(mypath, pdf_name="{}.pdf".format(pdf_name))
