# Steps to run:

1. Clone the repository to your desktop

2. Set working directory by cd Desktop/shopping-cart

3. IF USING THIRD-PARTY PACKAGES, USE A NEW ENV:
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt # (after specifying desired packages inside)

4. If you would like to link to your own version of the products csv, copy to your own github repository, and replace the url in the existing code with your own local link. It could be helpful to make a new subdirectory in your repository called "Data" to keep that separated from the program itself.
Make sure once you have the csv uploaded, you link to the raw data, by going into the csv in github and looking for "raw" in the upper right corner (# url should look like: https://raw.githubusercontent.com/alexha1234/shopping_cart/main/Data/products.csv)

4. Call program with:
python shopping-cart.py

5. A note: this program allows you to input your own tax rate, in decimal form.