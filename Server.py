from flask import Flask, jsonify, abort, request
from metoder import Metoder
app = Flask(__name__)

@app.route('/flask_app/')
def index():
    return "Hello, Welcome to our server!"

@app.route('/avgprice/', methods=['GET'])
def get_avg_price_phone():
    mt = Metoder("mobil_telefoner.csv")
    avg_price = mt.avgPrice()
    return jsonify({'msg' : "today the average phone cost " + str(avg_price)})

@app.route('/bestphonebestspecs/', methods=['GET'])
def get_best_phone_best_specs():
    mt = Metoder("mobil_telefoner.csv")
    display, camera, storage, ram, battery = mt.bestPhoneWithBestSpecsIn()
    display_json = {}
    camera_json = {}
    storage_json = {}
    ram_json = {}
    battery_json = {}
    for index, row in enumerate(display.values):
        a_dict = {
            "product_name" : str(row[0]),
            "product_display" : str(row[1]),
            "product_camera" : str(row[2]),
            "product_storage" : str(row[3]),
            "product_ram" : str(row[4]),
            "product_battery" : str(row[5]),
            "product_price" : str(row[6]),
        }
        display_json[index] = a_dict

    for index, row in enumerate(camera.values):
        a_dict = {
            "product_name" : str(row[0]),
            "product_display" : str(row[1]),
            "product_camera" : str(row[2]),
            "product_storage" : str(row[3]),
            "product_ram" : str(row[4]),
            "product_battery" : str(row[5]),
            "product_price" : str(row[6]),
        }
        camera_json[index] = a_dict

    for index, row in enumerate(storage.values):
        a_dict = {
            "product_name" : str(row[0]),
            "product_display" : str(row[1]),
            "product_camera" : str(row[2]),
            "product_storage" : str(row[3]),
            "product_ram" : str(row[4]),
            "product_battery" : str(row[5]),
            "product_price" : str(row[6]),
        }
        storage_json[index] = a_dict

    for index, row in enumerate(ram.values):
        a_dict = {
            "product_name" : str(row[0]),
            "product_display" : str(row[1]),
            "product_camera" : str(row[2]),
            "product_storage" : str(row[3]),
            "product_ram" : str(row[4]),
            "product_battery" : str(row[5]),
            "product_price" : str(row[6]),
        }
        ram_json[index] = a_dict

    for index, row in enumerate(battery.values):
        a_dict = {
            "product_name" : str(row[0]),
            "product_display" : str(row[1]),
            "product_camera" : str(row[2]),
            "product_storage" : str(row[3]),
            "product_ram" : str(row[4]),
            "product_battery" : str(row[5]),
            "product_price" : str(row[6])
        }
        battery_json[index] = a_dict


    result = {
        "display" : display_json,
        "camera" : camera_json,
        "storage" : storage_json,
        "ram" : ram_json,
        "battery" : battery_json
    }
    
    return jsonify(result)
    

@app.route('/bestphoneformoney/', methods=['GET'])
def get_best_phone_for_money():
    mt = Metoder("mobil_telefoner.csv")
    best_phone = mt.bestPhoneForMoney()
    name = str(best_phone[0])
    rating = str(best_phone[1])
    price = str(best_phone[2])
    
    return jsonify({"msg" : "The best phone to buy is: " + name + ", it has a rating of: " + rating + ", for the price of: " + price})
    
@app.route('/worstphoneformoney/', methods=['GET'])
def get_worst_phone_for_money():
    mt = Metoder("mobil_telefoner.csv")
    worst_phone = mt.worstPhoneForMoney()
    name = str(worst_phone[0])
    rating = str(worst_phone[1])
    price = str(worst_phone[2])
    
    return jsonify({"msg" : "The worst phone to buy is: " + name + ", it has a rating of: " + rating + ", for the price of: " + price})


@app.route('/biggestandsmallest/', methods=['GET'])
def get_biggest_smallest():
    mt = Metoder("mobil_telefoner.csv")
    biggest, smallest = mt.biggestAndSmallestDisplay()
    biggest_json = {}
    smallest_json = {}

    for index, row in enumerate(biggest.values):
        a_dict = {
            "product_name" : str(row[0]),
            "product_display" : str(row[1]),
            "product_camera" : str(row[2]),
            "product_storage" : str(row[3]),
            "product_ram" : str(row[4]),
            "product_battery" : str(row[5]),
            "product_price" : str(row[6]),
        }
        biggest_json[index] = a_dict


    for index, row in enumerate(smallest.values):
        a_dict = {
            "product_name" : str(row[0]),
            "product_display" : str(row[1]),
            "product_camera" : str(row[2]),
            "product_storage" : str(row[3]),
            "product_ram" : str(row[4]),
            "product_battery" : str(row[5]),
            "product_price" : str(row[6]),
        }
        smallest_json[index] = a_dict

    result = {
        "biggest" : biggest_json,
        "smallest" : smallest_json 
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)