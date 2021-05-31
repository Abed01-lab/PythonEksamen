import pandas as pd
import matplotlib.pyplot as plt
class Metoder:

    def __init__(self, filename):
        self.filename = filename

    def avgPrice(self):
        df = pd.read_csv(self.filename)
        filtered_df = df[df["product_price"] > 0]
        mean = filtered_df["product_price"].mean()
        return mean

    def biggestAndSmallestDisplay(self):
        df = pd.read_csv(self.filename)
        filtered_df = df[df["product_price"] > 0]
        biggest = filtered_df[filtered_df.product_display == filtered_df.product_display.max()]
        smallest = filtered_df[filtered_df.product_display == filtered_df.product_display.min()]

        return biggest, smallest

    def bestPhoneWithBestSpecsIn(self):
        df = pd.read_csv(self.filename)
        filtered_df = df[df["product_price"] > 0]

        display = filtered_df[filtered_df.product_display == filtered_df.product_display.max()]
        camera = filtered_df[filtered_df.product_camera == filtered_df.product_camera.max()]
        storage = filtered_df[filtered_df.product_storage == filtered_df.product_storage.max()]
        ram = filtered_df[filtered_df.product_ram == filtered_df.product_ram.max()]
        battery = filtered_df[filtered_df.product_battery == filtered_df.product_battery.max()]

        return display, camera, storage, ram, battery

    def priceAndSpec(self):
        df = pd.read_csv("rating.csv")

        plt.scatter(df["product_rating"], df["product_price"], label = df["product_name"])
        plt.show()
        plt.close()    

    def bestPhoneForMoney(self):
        df = pd.read_csv("rating.csv")
        bestRatio = 0
        for element in df.values: 
            product_ratio = (float(element[1]) / float(element[2])) * 10000

            if product_ratio > bestRatio:
                best_product = element
                bestRatio = product_ratio

        return best_product

    def worstPhoneForMoney(self):
        df = pd.read_csv("rating.csv")
        worstRatio = 100000
        for element in df.values: 
            product_ratio = (float(element[1]) / float(element[2])) * 10000

            if product_ratio < worstRatio:
                worst_product = element
                worstRatio = product_ratio

        return worst_product

    def presentPhoneWthML(self):
        pass