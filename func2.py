import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def lum(img, imgname):
    userimg = mpimg.imread(img)
    print("Reading image.....")
    lum_img = userimg[:, :, 0]
    print("Getting lum")
    plt.plot(lum_img)
    print("Plotting....")
    plt.savefig(imgname)

